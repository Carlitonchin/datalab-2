import encodings
from encodings.utf_8 import encode
from flask import Flask
import sqlite3
from .repo import get_projects_like, get_users
import json

app = Flask(__name__)

@app.route("/proyecto/<id_proyecto>")
def project(id_proyecto):
    con = sqlite3.connect('sitio.db')
    cur = con.cursor()
    
    proyectos = get_projects_like(cur, id_proyecto)
    usuarios = get_users(cur)
    
    con.close()

    result = {
        "projects": proyectos, 
        "users":usuarios
        }
    
    return result
