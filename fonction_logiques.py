""""""
"""
IMPORTS_________________________________________________________________________________________________________________
"""

from settings import *

import sqlite3 as lite
import datetime

"""
FONCTIONS D'AJOUT DE COMMANDES__________________________________________________________________________________________
"""

#création de la commande
def create_command_bdd(quantities_list):
    #quantities_list se réfere au nombre de pièces commandées pour chaque pièces du catalogue
    con = lite.connect("BDD.db")
    cur = con.cursor()
    #création de la commande
    cur.execute("INSERT INTO Commandes (ETAT, Date) VALUES(?,?)", (command_passed, date()))
    id_part = 1
    id_command = cur.execute("SELECT max(ID) FROM Commandes").fetchall()[0][0]
    print("INFO CONSOLE: Création de la commande numéro {}".format(id_command))
    #ajout de des pièces de la commande dans l'onglet liens
    for quantity in quantities_list:
        id_part += 1
        if quantity != 0:
            print("INFO CONSOLE: Ajout de la pièce {} avec un quantité de {}".format(id_part, quantity))
            cur.execute("INSERT INTO liens (ID_COMMANDE, ID_PIECE, quantite) VALUES (?,?,?)",
                        (id_command, id_part, quantity))
    con.commit()
    con.close()
    print("____________________________________________\n")
    return None




"""
AUTRES FONCTIONS________________________________________________________________________________________________________
"""

#récupération de la date
def date():
    date_row = str(datetime.datetime.now()).split(" ")
    date = date_row[0]
    return date


