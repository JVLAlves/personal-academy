from pprint import pprint

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

def update_skill(current_operator:archive.operator, collection:mg.collection.Collection):
    exists = False
    selected_operator = None
    operators = []
    for oper in collection.find():
        ops = dict(oper)
        ops["img"] = None
        operators.append(archive.operator(ops))

    for operator in operators:
        if operator.name == current_operator.name:
            exists = True
            selected_operator = operator
            break

    if exists:
        if selected_operator.skills == current_operator.skills:
            print("these skills already exists")
            return
        else:
            query = {"name":f"{current_operator.name}", "skill":selected_operator.skills}
            print(query)
            collection.update_one(query, {"$set":{"name":f"{current_operator.name}", "skills":current_operator.skills}})
            print("skills added")
            return
    else:
        print("Consider add the operator first")
        return




client = mg.MongoClient("mongodb+srv://joao:sdl170502@kaltsit.gyy0s.mongodb.net/kaltsit?retryWrites=true&w=majority", server_api=ServerApi('1'))
database = client["kaltsit"]
collection = database["operators"]
operators = archive.search(headless=True, max_searches=10)
for operator in operators:
    insert(operator, collection)

for operator in operators:
    print(operator.name)
    pprint(operator.skills)
    update_skill(operator, collection)




