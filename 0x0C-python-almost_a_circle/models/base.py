#!/usr/bin/python3
"Base class"
import json
import csv
from os import path


class Base:
    "Base class"
    __nb_objects = 0

    def __init__(self, id=None):
        "Initiation of the class with id"
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    @property
    def nb_objects(self):
        "Setter of counter"
        return self.__nb_objects

    @nb_objects.setter
    def nb_objects(self, value):
        "Getter of counter"
        self.__nb_objects = value

    @staticmethod
    def to_json_string(list_dictionaries):
        "Static method from dict to json string"
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        "Save objects to json file"
        js = ""
        ls = []
        if len(list_objs) == 0:
            with open(cls.__name__ + ".json", mode='w') as f:
                f.write("[]")
                return
        for i in list_objs:
            dic = i.to_dictionary()
            ls.append(dic)
        js += i.to_json_string(ls)
        with open(cls.__name__ + ".json", mode='w') as f:
            f.write(js)

    @staticmethod
    def from_json_string(json_string):
        "From json to dict"
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        "create another object"
        dummy = cls(1, 1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        "Load json string from json file"
        if not path.isfile(cls.__name__ + ".json"):
            return []
        ls = []
        with open(cls.__name__ + ".json", 'r') as f:
            todd = f.read()
            todd = cls.from_json_string(todd)
        for i in todd:
            dummy = cls.create(**i)
            ls.append(dummy)
        return ls

    @classmethod
    def save_to_file_csv(cls, list_objs):
        "Save to csv file"
        ls2 = []
        for i in list_objs:
            ls = []
            dic = i.to_dictionary()
            ls.append(dic['id'])
            if cls.__name__ == "Rectangle":
                ls.append(dic['width'])
                ls.append(dic['height'])
            if cls.__name__ == "Square":
                ls.append(dic['size'])
            ls.append(dic['x'])
            ls.append(dic['y'])
            ls2.append(ls)
        with open(cls.__name__ + ".csv", mode='w') as f:
            csw = csv.writer(f)
            for i in ls2:
                csw.writerow(i)

    @classmethod
    def load_from_file_csv(cls):
        "Load from csv file"
        if not path.isfile(cls.__name__ + ".csv"):
            return []
        ls = []
        with open(cls.__name__ + ".csv", 'r') as f:
            csr = csv.reader(f)
            csr = list(csr)
            lsdir = []
            for i in range(len(csr)):
                dic = {}
                dic.setdefault('id', int(csr[i][0]))
                if cls.__name__ == 'Rectangle':
                    dic.setdefault('width', int(csr[i][1]))
                    dic.setdefault('height', int(csr[i][2]))
                if cls.__name__ == 'Square':
                    dic.setdefault('size', int(csr[i][1]))
                dic.setdefault('x', int(csr[i][-2]))
                dic.setdefault('y', int(csr[i][-1]))
                lsdir.append(dic)
        for i in lsdir:
            dummy = cls.create(**i)
            ls.append(dummy)
        return ls
