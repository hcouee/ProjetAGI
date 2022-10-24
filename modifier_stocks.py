from flask import Flask, url_for, request, render_template, redirect
import sqlite3 as lite

conn = lite.connect('BDD.db')

#Il faut un compteur de commandes pour s'assurer de traiter uniquement la derniere commande (histoire de pas en compter une deux fois)


def modifier_stock(cur):
    if etat=="recue":
        rl = cur.execute("SELECT ID_PIECE, Liens.quantite FROM Liens WHERE ? = ID_COMMANDE",str(compteur))
        l1 = rl.fetchall()
        rs = cur.execute("SELECT ID, Quantite FROM Stock")
        l2 = rs.fetchall()

        print(l1,l2)

        for j in range(len(l1)):
            x=l1[j][1]
            cur.execute("UPDATE Stock SET Quantite=? WHERE Stock.ID=? ", (x,l1[j][0]))


cur=conn.cursor()
modifier_stock(cur)

