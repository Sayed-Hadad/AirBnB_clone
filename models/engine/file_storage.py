# models/engine/file_storage.py

import json
import os.path
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """
    This class serializes instances to
    a JSON file and deserializes JSON
    file to instances
    """

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """
        Returns __objects dictionary
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        Sets in __objects the obj with key
        <obj class name>.id
        """
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to the JSON file
        """
        obj_dic = {}
        for key, value in FileStorage.__objects.items():
            obj_dic[key] = value.to_dict()
        json_objs = json.dumps(obj_dic, default=str)
        with open(FileStorage.__file_path, 'w') as f:
            f.write(json_objs)

    def reload(self):
        """
        Deserializes the JSON file to __objects
        """
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r') as f:
                obj_dict = json.load(f)
                for key, value in obj_dict.items():
                    class_name = value['__class__']
                    if class_name == 'BaseModel':
                        model_class = BaseModel
                    elif class_name == 'State':
                        model_class = State
                    elif class_name == 'City':
                        model_class = City
                    elif class_name == 'Amenity':
                        model_class = Amenity
                    elif class_name == 'Place':
                        model_class = Place
                    elif class_name == 'Review':
                        model_class = Review
                    else:
                        model_class = None
                    if model_class:
                        obj = model_class(**value)
                        self.__objects[key] = obj
