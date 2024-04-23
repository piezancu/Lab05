from database.corso_DAO import CorsoDAO
from database.studente_DAO import StudenteDAO

class Model:

    def get_corsi(self):
        return CorsoDAO.getListaCorsi()

    def get_studenti_corso(self,codins):
        return CorsoDAO.get_iscritti_corso(codins)

    def cerca_studente(self, matricola):
        return StudenteDAO.cerca_studente(matricola)

    def get_corsi_studente(self,matricola):
        return StudenteDAO.get_corsi_studente(matricola)