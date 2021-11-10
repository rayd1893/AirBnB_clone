#!/usr/bin/python3
'''Define class FileStorage'''


import json
from models.base_model import BaseModel

class FileStorage(BaseModel):
    '''Class FileStorage'''
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        name = type(self).__name__
        FileStorage.__objects[name + "." + self.id] = obj

    def save(self):
        obj = json.dumps(FileStorage.__objects)
        with open(FileStorage.__file_path, "w", enconding="utf-8") as f:
            f.write(obj)

    def reload(self):
        try:
            with open(FileStorage.__file_path, "r", enconding="utf-8") as f:
                FileStorage.__objects = {}
                FileStorage.Objects = json.loads(f.read())
        except:
            pass

