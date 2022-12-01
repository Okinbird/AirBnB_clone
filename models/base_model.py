#!/usr/bin/python3
"""
    A class BaseModel that defines all common attributes
    and methods for other classes
"""
from uuid import uuid4
from datetime import datetime
import models

dform = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
    """
        The AirBnb projest BaseModel
    """

    def __init__(self, *args, **kwargs):
        """
        Set inital values for every instance

        Args:
            *args (any): Unused.
            **kwargs (dict): Key/value pairs of attributes.
        """
        if (kwargs):
            for key, value in kwargs.items():
                if key != "__class__":
                    if key == "created_at" or key == "updated_at":
                        val = datetime.strptime(value, dform)
                        setattr(self, key, val)
                    else:
                        setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """
            Represetation of the BaseModel instaces
            Returns:
                str: [<class name>] (<self.id>) <self.__dict__>
        """
        cls = type(self).__name__
        return "[{}] ({}) {}".format(cls, self.id, self.__dict__)

    def save(self):
        """
            Updates time and save changes into __objects (in FileStorage)
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        dictionary representation fo every instance
        time format: %Y-%m-%dT%H:%M:%S.%f
        key __class__ added to identify every instance
        Returns:
            dict: dictionary
        """
        dictionary = self.__dict__.copy()
        dictionary.update({'__class__': type(self).__name__})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        return dictionary
