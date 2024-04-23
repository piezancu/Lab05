# Add whatever it is needed to interface with the DB Table studente
from database.DB_connect import get_connection
from model.studente import Studente
from model.corso import Corso
class StudenteDAO:

    @staticmethod
    def cerca_studente(matricola):
        """
                Funzione che data una matricola ricerca nel database lo studente corrispondente (se presente)
                :param matricola: la matricola dello studente da ricercare
                :return: uno studente, se presente
                """
        cnx = get_connection()
        if cnx is not None:
            cursor = cnx.cursor(dictionary=True)
            cursor.execute("SELECT * FROM studente WHERE matricola = %s", (matricola,))
            row = cursor.fetchone()
            if row is not None:
                result = Studente(row["matricola"], row["cognome"], row["nome"], row["CDS"])
            else:
                result = None
            cursor.close()
            cnx.close()
            return result
        else:
            print("Could not connect")
            return None

    @staticmethod
    def get_corsi_studente(matricola) -> list[Corso]:
        lista_corsi = []
        cnx = get_connection()
        cursor = cnx.cursor()
        query = """
                    SELECT corso.*
                    FROM iscrizione, corso
                    WHERE iscrizione.codins=corso.codins AND iscrizione.matricola=%s """
        cursor.execute(query, (matricola,))
        for riga in cursor:
            lista_corsi.append(Corso(riga[0], riga[1], riga[2], riga[3]))
        cursor.close()
        return lista_corsi