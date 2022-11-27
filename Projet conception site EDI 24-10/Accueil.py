from flask import Flask, url_for, request, render_template, redirect
import sqlite3 as lite

# ------------------
# application Flask
# ------------------

app = Flask(__name__)

# ---------------------------------------
# les différentes pages (fonctions VUES)
# ---------------------------------------

#Page accueil
@app.route('/')
def index():
	
	contenu = ""
	contenu = "Accueil<br/>"
	contenu += "<a href='/AgiLog'>AgiLog<br/></a>"
	contenu += "<a href='/AgiLean'>AgiLean</a>"
	return contenu;


#Page AgiLog
@app.route('/AgiLog')  
def AgiLog():
	
	contenu = ""
	contenu += "<a href='/'>Retour à l'accueil</a><br/><br/>"
	contenu += "<a href='/AgiLog/Stock'>Stock</a><br/><br/>"
	contenu += "<a href='/AgiLog/Reception'>Réception</a><br/><br/>"
	contenu += "<a href='/AgiLog/Commande'>Commande</a><br/><br/>"
	contenu += "Contenu en cours de construction (AGILOG)"
	return contenu

#Sous page Stock
@app.route('/AgiLog/Stock')  
def Stock():
	
	contenu = ""
	contenu += "<a href='/AgiLog'>Retour à la page AgiLog</a><br/><br/>"
	contenu += "Contenu en cours de construction (STOCK)"
	return render_template('stock.html')
	'''return contenu'''
	
#Sous page Réception
@app.route('/AgiLog/Reception')  
def Reception():
	
	contenu = ""
	contenu += "<a href='/AgiLog'>Retour à la page AgiLog</a><br/><br/>"
	contenu += "Contenu en cours de construction (RECEPTION)"
	return contenu
	
#Sous page Commande
@app.route('/AgiLog/Commande')  
def Commande():
	
	con = lite.connect('BDD.db')
	con.row_factory = lite.Row
	cur = con.cursor()
	cur.execute("SELECT * FROM Pieces")
	lignes = cur.fetchall()
	con.close()
	return render_template('commande2.html', Pieces=lignes)
	
def create_command():
	return()


	
	
#Page AgiLean
@app.route('/AgiLean')  
def AgiLean():
	
	contenu = ""
	contenu += "<a href='/'>Retour à l'accueil</a><br/><br/>"
	contenu += "<a href='/AgiLean/Expedition'>Expédition</a><br/><br/>"
	contenu += "<a href='/AgiLean/Retour'>Retour</a><br/><br/>"
	contenu += "Contenu en cours de construction (AGILEAN)"
	return contenu

#Sous page Expédition
@app.route('/AgiLean/Expedition')  
def Expedition():
	
	contenu = ""
	contenu += "<a href='/AgiLean'>Retour à la page AgiLean</a><br/><br/>"
	contenu += "Contenu en cours de construction (EXPEDITION)"
	return contenu
	
#Sous page Retour
@app.route('/AgiLean/Retour')  
def Retour():
	
	contenu = ""
	contenu += "<a href='/AgiLean'>Retour à la page AgiLean</a><br/><br/>"
	contenu += "Contenu en cours de construction (RETOUR)"
	return contenu


if __name__ == '__main__':
	app.run(debug=True, port=5678)
