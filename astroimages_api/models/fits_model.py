import json

class FitsFile:
    def __init__(self, id, title, description, path):
        self.id = id
        self.title = title
        self.description = description
        self.path = path

    def __repr__(self):
        return json.dumps(self.__dict__)
