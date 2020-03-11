import json
from json import JSONEncoder

class FitsFile:
    def __init__(self, id, title, description, path):
        self.id = id
        self.title = title
        self.description = description
        self.path = path

    def __repr__(self):
        return '<FitsFile %r>' % self.title



# subclass JSONEncoder
class FitsFileEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__


