#!/usr/bin/python3
'''Define class FileStorage'''

#New line added:
import uuid
import json
#from models.base_model import BaseModel

class FileStorage():
    '''Class FileStorage'''
    __file_path = "file.json"
    __objects = {}
        
    def all(self):
        return FileStorage.__objects

    def new(self, obj):

        name = obj['__class__']
        self.__objects[name + "." + obj['id']] = obj
    
    def save(self):
        obj = json.dumps(self.__objects)
        print("Aqui")
        print(obj)
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            f.write(obj)

    def reload(self):
        try:
            with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
                FileStorage.__objects = {}
                FileStorage.Objects = json.loads(f.read())
        except:
            pass

