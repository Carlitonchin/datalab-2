class Project:
    def __init__(self, row):
        self.id = row[0]
        self.project_images = row[1]
        self.project_description = row[2]
        self.project_name = row[3]
        self.project_active = row[4]

    def to_json(self):
        me = {}
        me['id'] = self.id
        me['project_images'] = self.project_images
        me['project_description'] = self.project_description
        me['project_name'] = self.project_name
        me['project_active'] = self.project_active
        return me