from flask import Flask, url_for

# ------------------
# application Flask
# ------------------

app = Flask(__name__)

# ---------------------------------------
# les différentes pages (fonctions VUES)
# ---------------------------------------

# une page index avec un lien vers une page exemple
@app.route('/')
def index():
	
	contenu = ""
	contenu = "Accueil<br/>"
	contenu += "<a href='/AgiLog'>AgiLog</a>"
	return contenu;

#Page AgiLog
@app.route('/AgiLog')  
def AgiLog():
	
	contenu = ""
	contenu += "<a href='/'>retour à l'index</a><br/><br/>"
	contenu += "Contenu en cours de construction"
	return contenu
	
if __name__ == '__main__':
	app.run(debug=True, port=5678)
