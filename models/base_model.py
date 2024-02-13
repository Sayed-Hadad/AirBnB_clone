import datetime
import uuid
from models import storage


class BaseModel:
    """
    Base class for other classes with common attributes/methods.

    Public instance attributes:
    * id: string - assigned a uuid when an instance is created
    * created_at: datetime - assigned the current datetime
    when an instance is created
    * updated_at: datetime - assigned the current datetime
    when an instance is created
      and updated every time an object is changed
    """

    def __init__(self, *args, **kwargs):
        """
        Constructor method:
        * creates a unique id using uuid.uuid4()
        * initializes created_at with the current time
        * initializes updated_at with the current time

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
                    if key in ('created_at', 'updated_at'):
                        setattr(self, key, parse_datetime(value))
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


def parse_datetime(datetime_str):
    return datetime.datetime.strptime(datetime_str, '%Y-%m-%dT%H:%M:%S.%f')
