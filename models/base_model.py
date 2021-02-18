#!/usr/bin/python3

"""AirBnB project - Base Models"""
import uuid
from datetime import datetime
import models
import copy


class BaseModel:
    """New instance BaseModel class
    """
    def __init__(self, *args, **kwargs):
        """Method constructor initialize an instance
        """
        if kwargs:
            form = "%Y-%m-%dT%H:%M:%S.%f"
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                    continue
                if key == "created_at":
                    self.created_at = datetime.strptime(value, form)
                    continue
                if key == "update_at":
                    self.update_at = datetime.strptime(value, form)
                    continue
                if key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """Print a readable string
        """
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Updates with the current datetime
        """
        self.update_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Instance public create a dict
        """
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = type(self).__name__
        new_dict["updated_at"] = new_dict["updated_at"].isoformat()
        new_dict["created_at"] = new_dict["created_at"].isoformat()
        return new_dict
