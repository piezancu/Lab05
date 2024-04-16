# Add whatever it is needed to interface with the DB Table corso

from database.DB_connect import get_connection
import mysql.connector
from model.corso import Corso

class CorsoDAO:
    # inizializzo la classe con un oggetto MySQLConnection, sul quale
    # potrò iterare grazie alla struttura Cursor (che utilizzerò in model.corso)


    @staticmethod
    def getListaCorsi():
        lista = []
        cnx = get_connection()
        cursor = cnx.cursor()
        query = """
                SELECT * 
                FROM corso"""
        cursor.execute(query)
        for riga in cursor:
            print(riga)
            lista.append(Corso(riga[0], riga[1], riga[2], riga[3]))
        cursor.close()
        return lista

