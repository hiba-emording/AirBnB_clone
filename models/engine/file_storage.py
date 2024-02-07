#!/usr/bin/python3
"""
"""
import json
import os
import models


class FileStorage:
    """ """
    def __init__(self):
        """ """
        self.__file_path = "file.json"
        self.__objects = {}

    def all(self):
        """ """
        return self.__objects

    def new(self, obj):
        """ """
        objclsname = obj.__class__.__name__
        self.__objects["{}.{}".format(objclsname, obj.id)] = obj

    def save(self):
        """ """
        objdict = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(self.__file_path, 'w') as f:
            json.dump(objdict, f)

    def reload(self):
        """ """
        try:
            with open(self.__file_path, 'r') as f:
                info = json.load(f)
                for key, value in info.items():
                    classname, obj_id = key.split(".")
                    classobj = globals()[classname]
                    instance = classobj(**value)
                    self.__objects[key] = instance
        except FileNotFoundError:
            return
