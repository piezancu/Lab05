from database.corso_DAO import CorsoDAO
from model import corso
class Model:

    def get_corsi(self):
        return CorsoDAO.getListaCorsi()
