#!/usr/bin/python3
'''AirBnB Clone Project starts!!'''
import uuid
from datetime import datetime
import models
fd = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
    '''Main Class BaseModel'''
    name = ""

    def __init__(self, *args, **kwargs):
        '''Initializes an object and add it\
                to the __objects dictionary
        Args:
            args: Number of arguments. Not used
            kwargs: elements of a dict to create\
                    an object
        '''
        if len(kwargs) > 0:
            kwargs.pop("__class__", None)
            for key, value in kwargs.items():
                setattr(self, key, value)
            self.created_at = datetime.strptime(kwargs["created_at"], fd)
            if hasattr(self, "updated_at") and type(self.updated_at) is str:
                self.updated_at = datetime.strptime(kwargs["updated_at"], fd)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            # self.name = ""
            # self.my_number = 0
        models.storage.new(self)

    def __str__(self):
        '''Define printable representation of an\
                onject
        '''
        name = type(self).__name__
        return "[{}] ({}) {}".format(name, self.id, self.__dict__)

    def save(self):
        '''Save object to file storage'''
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        '''Create a dictionary representation of\
                an object. Used before save to a\
                file
        '''
        name = type(self).__name__
        dictionary = self.__dict__.copy()
        dictionary['__class__'] = name
        if "created_at" in dictionary:
            dictionary['created_at'] = dictionary['created_at'].strftime(fd)
        if "updated_at" in dictionary:
            dictionary['updated_at'] = dictionary['updated_at'].strftime(fd)
        return dictionary
