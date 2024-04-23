# Add whatever it is needed to interface with the DB Table corso

from database.DB_connect import get_connection
from model.corso import Corso
from model.studente import Studente

class CorsoDAO:

    @staticmethod
    def getListaCorsi():
        lista_corsi = []
        cnx = get_connection()
        cursor = cnx.cursor()
        query = """
                SELECT * 
                FROM corso"""
        cursor.execute(query)
        for riga in cursor:
            lista_corsi.append(Corso(riga[0], riga[1], riga[2], riga[3]))
        cursor.close()
        return lista_corsi

    @staticmethod
    def get_iscritti_corso(codins) -> list[Studente]:
        lista_iscritti = []
        cnx = get_connection()
        cursor = cnx.cursor()
        query = """
                SELECT studente.*
                FROM iscrizione, studente
                WHERE iscrizione.matricola=studente.matricola AND iscrizione.codins=%s """
        cursor.execute(query, (codins,))
        for riga in cursor:
            lista_iscritti.append(Studente(riga[0], riga[1], riga[2], riga[3]))
        cursor.close()
        return lista_iscritti
