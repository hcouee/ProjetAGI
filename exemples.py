# -*- coding: utf-8 -*-
from flask import Flask, url_for, request, render_template, redirect
import sqlite3 as lite

# ------------------
# application Flask
# ------------------

app = Flask(__name__)


# ---------------------------------------
# des fonctions utiles à plusieurs pages
# ---------------------------------------

# renvoie un lien HTML pour retourner à la page index
def retour_index():
	return render_template('accueil.html')
	
# renvoie un formulaire vers la page cible demandant un prénom (avec une valeur par défaut)
def formulaire_prenom(cible, prenom = "entrez votre prénom"):
	formulaire = ""
	formulaire += "<form method='post' action='" + url_for(cible) + "'>"
	formulaire += "<input type='text' name='prenom' value='" + prenom + "'>"
	formulaire += "<input type='submit' value='Envoyer'>"
	formulaire += "</form><br/>"
	
	return formulaire
	
# connecte à la BDD, affecte le mode dictionnaire aux résultats de requêtes et renvoie un curseur
def connection_bdd():
	
	con = lite.connect('BDD.db')
	con.row_factory = lite.Row
	
	return con
	
# connecte à la BDD et renvoie toutes les lignes de la table Stock
def selection_pieces():
	
	conn = connection_bdd()
	cur = conn.cursor()
	
	cur.execute("SELECT ID, Piece, Quantite FROM Stock")
	
	lignes = cur.fetchall()
	
	conn.close()
	
	return lignes
	
# connecte à la BDD et renvoie les lignes de la table personne dont le prénom commence par la lettre donnée
def selection_personnes_lettre(lettre):
	
	conn = connection_bdd()
	cur = conn.cursor()
	
	cur.execute("SELECT nom, prenom, role FROM personnes WHERE prenom LIKE ?", (lettre + "%",))
	
	lignes = cur.fetchall()
	
	conn.close()
	
	return lignes
	
# connecte à la BDD et insère une nouvelle ligne avec les valeurs données
def insertion_stock(ID, Piece, Quantite):
	
	try:
		conn = connection_bdd()
		cur = conn.cursor()
		
		cur.execute("INSERT INTO Stock('ID', 'Piece', 'Quantite') VALUES (?,?,?)", (ID,Piece,Quantite))
		
		conn.commit()
		
		conn.close()
		
		return True
		
	except lite.Error:
		
		return False
	


# ---------------------------------------
# les différentes pages (fonctions VUES)
# ---------------------------------------


# une page index avec des liens vers les différentes pages d'exemple d'utilisation de Flask
@app.route('/')
def index():	
	return render_template('accueil.html');
  


# une page avec du texte statique
@app.route('/agilog')  
def agilog():
	return render_template('agilog.html')


@app.route('/commande')  
def commande():
	
	contenu = ""
	contenu += retour_index()
	contenu += "La page commande"
	
	return contenu

@app.route('/reception')  
def reception():
	
	contenu = ""
	contenu += retour_index()
	contenu += "La page reception"
	
	return contenu

# une page avec du texte dynamique déterminé par l'URL
@app.route('/agigreen')  
def agigreen():
	
	contenu = ""
	contenu += retour_index()
	contenu += "La page AgiGreen"
	
	return contenu
	
# une page avec un entier dynamique déterminé par l'URL
@app.route('/hello_url_entier/<int:valeur>')  
def hello_url_entier(valeur):
	
	contenu = ""
	contenu += retour_index()
	contenu += "Hello, n * 2 = " + str(valeur*2) + " !"
	
	return contenu
	
# une page avec du texte dynamique envoyé par HTTP/GET
@app.route('/hello_get', methods=['GET'])  
def hello_get_prenom():
	
	contenu = ""
	contenu += retour_index()
	contenu += "Hello, " + request.args.get('prenom', 'une valeur par defaut') + " !"
	
	return contenu

@app.route('/fichier_statique')
def fichier_statique():
	contenu = ""
	contenu += retour_index()
	contenu += "Hello, World !<br/>"
	contenu += "<img src='" + url_for('static', filename='globe.png') + "'/>"
	
	return contenu
	
# une page avec du texte dynamique envoyé par HTTP/POST
@app.route('/hello_post', methods=['POST'])  
def hello_post_prenom():
	
	contenu = ""
	contenu += retour_index()
	contenu += "Hello, " + request.form['prenom'] + " !"
	
	return contenu

# un page qui combine affichage du formulaire et traitement
@app.route('/formulaire_combine', methods=['GET','POST'])  
def formulaire_combine():
	
	contenu = ""
	contenu += retour_index()
	
	erreur = ""
	if request.method == 'POST':
		
		if (request.form['prenom'][0].lower() == "a"):
			contenu += "Hello, " + request.form['prenom'] + " !"
			return contenu
		
		else:
			erreur = 'le prénom doit commencer par un "A"'
	
	# on arrive ici si rien n'a été envoyé par POST, ou si la validation des données a échoué
	
	if (erreur != ""):
		contenu += "<strong>Erreur : " + erreur + "</strong>"
		
	contenu += formulaire_prenom("formulaire_combine", prenom = "prénom en A")
	
	return contenu

@app.route('/template_html', methods=['GET'])  
def template_html():
	return render_template('hello.html', prenom=request.args.get('prenom', ''), afficher_globe=request.args.get('globe', False))
	
	
@app.route('/stock', methods=['GET'])
def affichage_bdd_stock():
	
	lignes = selection_pieces()
	
	return render_template('affichage_stock.html', Stock = lignes)
	
	
@app.route('/afficher_personnes_a')
def affichage_bdd_personnes_a():
	
	lignes = selection_personnes_lettre("A")
	
	return render_template('affichage_personnes_lettre.html', lettre = "A", personnes = lignes)
	
	
@app.route('/ajouter_stock', methods=['GET', 'POST'])
def insertion_bdd_piece_stock():
	
	erreur = ""
	if request.method == 'POST':
		
		if (request.form['ID'] != "" and request.form['Piece'] != "" and request.form['Quantite'] != ""):
			
			res = insertion_stock(request.form['ID'],request.form['Piece'],request.form['Quantite'])
			
			if (res):
			
				return redirect(url_for('affichage_bdd_stock'))
				
			else:
				erreur = "Une erreur a été détectée lors de l'insertion dans la base de données. Veuillez réessayer ou contacter l'administrateur du site."
		else:
			erreur = "Une erreur a été détectée dans le formulaire, merci de remplir tous les champs correctement."
	
	# on arrive ici si rien n'a été envoyé par POST, ou si la validation des données a échoué
	
	return render_template('formulaire_personne.html', msg = erreur, nom = request.form.get('ID', ''), prenom = request.form.get('Piece', ''), role = request.form.get('Quantite', ''))

# ---------------------------------------
# pour lancer le serveur web local Flask
# ---------------------------------------

if __name__ == '__main__':
	app.run(debug=True)
