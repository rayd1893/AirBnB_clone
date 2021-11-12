#!/usr/bin/python3
'''Create Class Base'''


import uuid 
from datetime import datetime
import models

fd = "%Y-%m-%dT%H:%M:%S.%f"

class BaseModel:
    '''Class BaseModel'''
    name = ""
    def __init__(self, *args, **kwargs):
        '''Define constructor'''
    
        if len(kwargs) > 0:
            kwargs.pop("__class__", None)
            for key,value in kwargs.items():
                #if key == "update_at" or key == "created_at":
                    
                    #print(type(value))
                    #setattr(self, key, datetime.strptime(value, fd))
                #else:
                setattr(self, key, value)
            print(type(self.created_at))
            self.created_at = datetime.strptime(kwargs["created_at"], fd)
            print(type(self.created_at))
            if hasattr(self, "updated_at") and type(self.updated_at) is str:
                self.updated_at = datetime.strptime(kwargs["updated_at"], fd)
                
        else:
            #now = datetime.datetime.now()
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            #self.name = ""
            #self.my_number = 0
        models.storage.new(self)


    def __str__(self):
        name = type(self).__name__
        return "[{}] ({}) {}".format(name, self.id, self.__dict__)

    def save(self):
        #now = datetime.datetime.now()
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        name = type(self).__name__
        dictionary = self.__dict__.copy()
        dictionary['__class__'] = name
        if "created_at" in dictionary:
            dictionary['created_at'] = dictionary['created_at'].strftime(fd)
        if "updated_at" in dictionary:
            dictionary['updated_at'] = dictionary['updated_at'].strftime(fd)
        return dictionary

