#!/usr/bin/python3
"""
Consists of private class __nb_objects, and class the constructor __init__
Returns to JSON string representating of all of the list dictionaries
it also saves JSON strings of instance dictionaries into file
Returns to Python obj of JSON string representation
Also retturn instance with attributes which are already set
Additionally, return list of all instances
Saves to CSV and loads from the CSV file
"""


import json
import csv


class Base():
    """
    defines class Base
    Class Attributes:
        __nb_objects
    Methods:
        __init__(self, id=None)
    Static Methods:
        to_json_string(list_dictionaries)  from_json_string(json_string)
    Class Methods:
        save_to_file(cls, list_objs)      save_to_file_csv(cls, list_objs)
        load_from_file(cls)               load_from_file_csv(cls)
        create(cls, **dictionary)
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize id, increase class attribute if no id and then set as id"""
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns JSON string representation of list dict"""
        if list_dictionaries is None:
            list_dictionaries = []
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """Returns to Python obj of JSON string representation"""
        if json_string is None or len(json_string) == 0:
            json_string = "[]"
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """Save json strings of all instances into file"""
        objs = []
        if list_objs is not None:
            for x in list_objs:
                objs.append(cls.to_dictionary(x))
        fname = cls.__name__ + ".json"
        with open(fname, "w") as f:
            f.write(cls.to_json_string(objs))

    @classmethod
    def create(cls, **dictionary):
        """Returns instance with attributes that are already set"""
        if cls.__name__ == "Square":
            dummy = cls(1)
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Returns list of instances"""
        fnamee = cls.__name__ + ".json"
        b = []
        try:
            with open(fnamee, "r") as f:
                instances = cls.from_json_string(f.read())
            for a, dic in enumerate(instances):
                b.append(cls.create(**instances[a]))
        except:
            pass
        return b

    @classmethod
    def save_to_file_csv(cls, list_objs):
        fname = cls.__name__ + ".csv"
        with open(fname, 'w', newline='') as f:
            writer = csv.writer(f)
            for i in list_objs:
                if cls.__name__ == "Rectangle":
                    writer.writerow([i.id, i.width, i.height, i.x, i.y])
                if cls.__name__ == "Square":
                    writer.writerow([i.id, i.size, i.x, i.y])

    @classmethod
    def load_from_file_csv(cls):
        objs = []
        fname = cls.__name__ + ".csv"
        with open(fname, 'r', newline='') as f:
            reader = csv.reader(f)
            for my_row in reader:
                if cls.__name__ == "Rectangle":
                    dic = {"id": int(my_row[0]),
                           "width": int(my_row[1]),
                           "height": int(my_row[2]),
                           "x": int(my_row[3]),
                           "y": int(my_row[4])}
                if cls.__name__ == "Square":
                    dic = {"id": int(my_row[0]),
                           "size": int(my_row[1]),
                           "x": int(my_row[2]),
                           "y": int(my_row[3])}
                o = cls.create(**dic)
                objs.append(o)
        return objs

