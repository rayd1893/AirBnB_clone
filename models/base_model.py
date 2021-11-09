#!/usr/bin/python3
'''Create Class Base'''


import uuid
import datetime
import json


class BaseModel:
    '''Class BaseModel'''
    def __init__(self):
        '''Define constructor'''
        now = datetime.datetime.now()
        self.id = str(uuid.uuid4())
        self.created_at = now
        self.updated_at = now
        self.name = ""
        self.my_number = 0

    def __str__(self):
        name = type(self).__name__
        return "[{}] ({}) {}".format(name, self.id, self.__dict__)

    def save(self):
        now = datetime.datetime.now()
        self.updated_at = now

    def to_dict(self):
        name = type(self).__name__
        dictionary = (self.__dict__).copy()
        dictionary['__class__'] = name
        dictionary['created_at'] = str(self.created_at.isoformat('T'))
        dictionary['updated_at'] = str(self.updated_at.isoformat('T'))
        return dictionary
