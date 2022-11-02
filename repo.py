from sqlite3 import Cursor
from .models.project import *

def get_projects_like(cur : Cursor, pattern : str):
    like = f'%{pattern}%'
    cur.execute("SELECT * FROM project WHERE project_name LIKE ?", (like,))

    result = []
    projects = cur.fetchall()

    for p in projects:
        result.append(Project(p).to_json())
    
    return result
