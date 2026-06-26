import json

my_file = open('test_data.json') #Метод вычитывает содержимое файла
global_data = json.load(my_file)

class DataProvider:

    def __init__(self):
        self.data = global_data

    def get(self, prop:str):
        return self.data.get(prop)

    def getint(self, prop:str):
        val = self.data.get(prop)
        return int(val)

    def get_token(self):
        return self.data.get("token")