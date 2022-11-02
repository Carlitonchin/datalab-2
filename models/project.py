def create_project(row):
    project = {
        "id": row[0],
    "project_images" : row[1],
    "project_description" : row[2],
    "project_name" : row[3],
    "project_active" : row[4]
    }

    return project
        