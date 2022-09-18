import json
import os

class JsonManager:
    def __init__(self):
        self.__basePath = 'src/app_infrastructure/persistence/json/'
        self.__current_path = os.path.realpath(__file__)

    def readJson(self, name):
        with open(self.__basePath + name) as file:
            data = json.load(file)
        return data
