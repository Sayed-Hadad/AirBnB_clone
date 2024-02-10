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
    __model_classes = {
        'BaseModel': BaseModel,
        'State': State,
        'City': City,
        'Amenity': Amenity,
        'Place': Place,
        'Review': Review
    }

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
        try:
            with open(FileStorage.__file_path, 'w') as f:
                f.write(json_objs)
        except Exception as e:
            print(f"Error saving data: {e}")

    def reload(self):
        """
        Deserializes the JSON file to __objects
        """
        try:
            if os.path.exists(FileStorage.__file_path):
                with open(FileStorage.__file_path, 'r') as f:
                    obj_dict = json.load(f)
                    for key, value in obj_dict.items():
                        class_name = value.get('__class__')
                        model_class = self.__model_classes.get(class_name)
                        if model_class:
                            obj = model_class(**value)
                            self.__objects[key] = obj
        except Exception as e:
            print(f"Error reloading data: {e}")
