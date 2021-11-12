#!/usr/bin/python3
'''Define class FileStorage'''

#New line added:
import uuid
import json
from models.base_model import BaseModel

Classes = {"BaseModel": BaseModel}
#from models.base_model import BaseModel

class FileStorage:
    '''Class FileStorage'''
    __file_path = "file.json"
    __objects = {}
        
    def all(self):
        return FileStorage.__objects

    def new(self, obj):

        #name = obj['__class__']
        if obj is not None:
            key = obj.__class__.__name__ + "." + obj.id
            self.__objects[key] = obj
            #self.__objects[name + "." + obj['id']] = obj
    
    def save(self):
        jsondict = {}
        print("__objects")
        print(self.__objects)
        for key in self.__objects:
            jsondict[key] = self.__objects[key].to_dict()
            
    
        #obj = json.dumps(self.__objects)
        #print("Aqui")
        #print(obj)
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
           json.dump(jsondict, f)

    def reload(self):
        try:
            jsondict = {}
            with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
                #FileStorage.__objects = {}
                jn = json.load(f)
                print("AQUI AQUI")
                #print(jsondict)
                for key in jn:
                    b = jn[key]["__class__"]
                    self.__objects[key] = Classes[jn[key]["__class__"]](**jn[key])
                print("final")
                print(self.__objects)
        except Exception as f:
            print(f)

