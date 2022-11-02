from flask import Flask
import sqlite3

app = Flask(__name__)

@app.route("/proyecto/<id_proyecto>")
def project(id_proyecto):
    con = sqlite3.connect('sitio.db')
   
    
    
    con.close()
    return "Hello World"
