import pymongo as mg
from pymongo.server_api import ServerApi
import archive

def insert(operator:archive.operator, collection:mg.collection.Collection):
    names = []
    for ops in collection.find():
        op_dict = dict(ops)
        names.append(op_dict["name"])

    if operator.name in names:
        print("operator already exists in the Database")
        return
    else:
        collection.insert_one(operator.dict)
        print("operator added")
        return
client = mg.MongoClient("mongodb+srv://joao:sdl170502@kaltsit.gyy0s.mongodb.net/kaltsit?retryWrites=true&w=majority", server_api=ServerApi('1'))
database = client["kaltsit"]
collection = database["operators"]
operators = archive.search(headless=True, max_searches=100)
for operator in operators:
    insert(operator, collection)

def update(query:dict, new_value:dict, collection:mg.collection.Collection):
    collection.update_one(query, new_value)


