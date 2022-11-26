from flask import *
import sqlite3 as lite
from fonctions_pages import *



# ---------------------------------------
# pour lancer le serveur web local Flask
# ---------------------------------------

if __name__ == '__main__':
	app.run(debug=True, port=5678)
