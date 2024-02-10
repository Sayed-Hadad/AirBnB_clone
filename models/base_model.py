import datetime
import uuid


class BaseModel:
    """
    This class defines all common attributes/methods for other classes:

    Public instance attributes:
    * id: string - assign with a uuid when an instance is created
    * created_at: datetime - assign with the current datetime when an instance is created
    * updated_at: datetime - assign with the current datetime when an instance is created
      and it will be updated every time you change your object
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
        from models import storage  # Import here to avoid circular import
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key == 'created_at' or key == 'updated_at':
                        setattr(self, key, datetime.datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f'))
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
        Return a string representation of the BaseModel instance.
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        Update the public instance attribute updated_at with the current datetime.
        """
        from models import storage  # Import here to avoid circular import
        self.updated_at = datetime.datetime.now()
        storage.save()


    def to_dict(self):
        """
        Return a dictionary containing all keys/values of __dict__ of the instance.

        A key __class__ must be added to this dictionary with the class name of the object.
        created_at and updated_at must be converted to string object in ISO format.
        """
        from models import storage  # Import here to avoid circular import
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
