#!/usr/bin/python3
"""
This module is for Base class -model- which will act
as the back bone of our project, as  defines all common
attributes/methods for other classes:
"""
import datetime
import uuid
from models import storage


class BaseModel:
    """
    This class defines all common attributes/methods for other classes:

    Public instance attributes:
    * id: string - assign with an uuid when an instance is created:
    * created_at: datetime - assign with the current datetime when an
        instance is created
    * updated_at: datetime - assign with the current datetime when an instance
        is created and it will be updated every time you change your object
    """

    def __init__(self, *args, **kwargs):
        """
        The constructor of our instances:
        * creates a unique id using uuid.uuid4()
        * initialize created_at with the current time
        * initialize updated_at with the current time

        Args:
        *args: Unused positional arguments.
        **kwargs: Keyword arguments used for recreating an instance from
        dictionary representation.

        If kwargs is not empty:
        - Recreates instance attributes from the provided dictionary
            representation.
        - Converts 'created_at' and 'updated_at' strings to datetime objects.
        - If 'id' and 'created_at' are missing, generates them.
        If kwargs is empty:
        - Creates a new instance with fresh 'id', 'created_at',
        and 'updated_at'.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key == 'created_at' or key == 'updated_at':
                        setattr(self, key, datetime.datetime.strptime
                                (value, '%Y-%m-%dT%H:%M:%S.%f'))
                    else:
                        setattr(self, key, value)
            if 'id' not in kwargs:
                self.id = str(uuid.uuid4())
            if 'created_at' not in kwargs:
                self.created_at = datetime.datetime.now()
            if 'updated_at' not in kwargs:
                self.updated_at = datetime.datetime.now()
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            storage.new(self)

    def __str__(self):
        """
        prints: [<class name>] (<self.id>) <self.__dict__>
        """
        name = self.__class__.__name__
        return f'[{name}] ({self.id}) {self.__dict__}'

    def save(self):
        """
        updates the public instance attribute updated_at
        with the current datetime
        """
        self.updated_at = datetime.datetime.now()
        storage.save()

    def to_dict(self):
        """
        returns a dictionary containing all keys/values of
        __dict__ of the instance:

        * by using self.__dict__, only instance attributes set
            will be returned
        * a key __class__ must be added to this dictionary with the
            class name of the object
        * created_at and updated_at must be converted to string object
            in ISO format
        """
        temp_dic = self.__dict__.copy()
        temp_dic['created_at'] = temp_dic['created_at'].isoformat()
        temp_dic['updated_at'] = temp_dic['updated_at'].isoformat()
        temp_dic['__class__'] = self.__class__.__name__
        return temp_dic
