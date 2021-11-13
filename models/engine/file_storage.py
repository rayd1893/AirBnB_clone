#!/usr/bin/python3
'''Define class FileStorage'''
# New line added:
import uuid
import json
from models.base_model import BaseModel
Classes = {"BaseModel": BaseModel}


class FileStorage:
    '''Class FileStorage'''
    __file_path = "file.json"
    __objects = {}

    def all(self):
        '''Returns _objects dictionary\
                at the beggining
        '''
        return FileStorage.__objects

    def new(self, obj):
        '''add obj object to __objects dict'''
        # print("NEW METHOD IN FILESTORAGE")
        # print(type(obj))
        # print(obj)
        if obj is not None:
            key = obj.__class__.__name__ + "." + obj.id
            self.__objects[key] = obj
            # self.__objects[name + "." + obj['id']] = obj
            # print(self.__objects)
    def save(self):
        jsondict = {}
        # print("This is the dictionary __objects in method save")
        # print(type(self.__objects))
        # print(self.__objects)
        for key in self.__objects:
            jsondict[key] = self.__objects[key].to_dict()

        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            json.dump(jsondict, f)

    def reload(self):
        try:
            jsondict = {}
            with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
                jn = json.load(f)
                # print("jn IS CREATED IN THE RELOAD METHOD")
                # print(type(jn))
                # print(jn)
                for key in jn:
                    b = jn[key]["__class__"]
                    self.__objects[key] = Classes[b](**jn[key])
                # print("__objects RELOADED")
                # print(type(self.__objects))
                # print(self.__objects)
        except Exception as f:
            # print(f)
            pass
