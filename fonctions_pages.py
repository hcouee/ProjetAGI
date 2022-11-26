from flask import *
from fonction_logiques import *
import sqlite3 as lite

"""
Création de l'app
"""
app = Flask(__name__)


"""
Création de la page d'acceuil du site
"""
@app.route('/')
def index():
    return render_template("index.html")

"""
Redirection sur les pages dédiées aux entreprises
"""
@app.route('/log')
def log():
    return render_template("log.html")

@app.route('/leen')
def leen():
    return render_template("leen.html")

"""
Page de commande
"""

@app.route('/commands', methods=['GET', 'POST'])
def create_commande():
    if not request.method == 'POST':
        return render_template('formulaire_personne.html', msg="", nom="", prenom="", role=0)
    else:
        nom = request.form.get('nom', '')
        prenom = request.form.get('prenom', '')
        role = request.form.get('role', 0, type=int)

        if (nom != "" and prenom != "" and role > 0 and role < 4):
            con = lite.connect('exemples.db')
            con.row_factory = lite.Row
            cur = con.cursor()
            cur.execute("INSERT INTO personnes('nom', 'prenom', 'role') VALUES (?,?,?)", (nom, prenom, role))
            con.commit()
            con.close()
            return redirect(url_for('afficher_personnes'))
        else:
            return render_template('formulaire_personne.html', msg="Mauvaise saisie !", nom="", prenom="", role=0)