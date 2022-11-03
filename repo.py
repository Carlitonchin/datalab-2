from sqlite3 import Cursor
from .models.project import *
from .models.user import *


def get_projects_like(cur : Cursor, pattern : str):
    like = f'%{pattern}%'
    cur.execute("SELECT * FROM project WHERE project_name LIKE ?", (like,))

    result = []
    projects = cur.fetchall()

    for p in projects:
        result.append(create_project(p))
    
    return result

def get_users(cur:Cursor):
    cur.execute('''
    SELECT * FROM
    user LEFT JOIN user_role_association_table
    ON user.id = user_role_association_table.user_id
    LEFT JOIN role
    ON role.id = user_role_association_table.role_id
    ''')

    result = []
    users = cur.fetchall()
    for u in users:
        result.append(create_user(u))
    
    return result


