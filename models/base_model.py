#!/usr/bin/python3
'''Create Class Base'''


import uuid
from datetime import date
import json


class BaseModel:
    '''Class BaseModel'''
    def __init__(self):
        '''Define constructor'''
        self.id = str(uuid.uuid4())
        self.created_at = (date.today()).strftime("%Y-%m-%dT%H:%M:%S.%f")
        self.updated_at = (date.today()).strftime("%Y-%m-%dT%H:%M:%S.%f")
        self.name = ""
        self.my_number = 0

    def __str__(self):
        name = type(self).__name__
        return "[{}] ({}) {}".format(name, self.id, self.__dict__)

    def save(self):
        self.updated_at = (date.today()).strftime("%Y-%m-%dT%H:%M:%S.%f")

    def to_dict(self):
        name = type(self).__name__
        dictionary = self.__dict__
        dictionary['__class__'] = name
        return dictionary
