class Project:
    def __init__(self, row):
        self.id = row[0]
        self.project_images = row[1][0]
        self.project_description = row[1][1]
        self.project_name = row[1][2]
        self.project_active = row[1][3]