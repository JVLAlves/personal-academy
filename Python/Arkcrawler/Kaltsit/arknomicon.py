import datetime
import re
from pprint import pprint

import pymongo as mg
from pymongo.server_api import ServerApi
client = mg.MongoClient(
    "mongodb+srv://joao:sdl170502@kaltsit.gyy0s.mongodb.net/kaltsit?retryWrites=true&w=majority",
    server_api=ServerApi('1'))
database = client["kaltsit"]
try:
    kaltsitCollection = database["operators"]
except:
    print("Is this a new computer?\nHave you added the new IP?\n")


def add_field(field: str, collection: mg.collection.Collection=kaltsitCollection, default_value=None):
    if collection.find_one({f"{field.lower()}": {"$exists": True}}) == None:
        collection.update_many({}, {"$set": {f"{field.lower()}": default_value}})
        print("field added")
    elif collection.find_one({f"{field.lower()}": {"$exists": True}}) != None and default_value !=None:
        collection.update_many({}, {"$set": {f"{field.lower()}": default_value}})
        print("subfields or default values added")


def insert_operator(new_operator: dict, collection: mg.collection.Collection=kaltsitCollection):
    if collection.find_one({"name": {"$eq": new_operator["name"]}}) != None:
        print("operator already exists in the Database")
    else:
        collection.insert_one(new_operator)
        print("operator added")
    return


def update_operator(current_operator: dict, collection: mg.collection.Collection=kaltsitCollection):
    exists = False
    differences = []
    model_keys = dict(collection.find_one({"name": "Honeyberry"})).keys()
    print(model_keys)
    model = list(model_keys)
    if collection.find_one({"name": {"$eq": current_operator["name"]}}) != None:
        pass
    else:
        raise Exception("Operator not found. Please make sure you're not trying to update the name.")

    selected_operator = dict(collection.find_one({"name": current_operator["name"]}))
    if current_operator.keys() != model:
        print(f"MODEL: {model}")
        for keys in current_operator.keys():
            print(fr"KEY: {keys if keys != '' else 'Nothing'}, MODEL: {model}")
            if keys not in model:
                print(f"(DIFF) {keys}")
                print(f"if you want to add a new field called {keys}, consider to do it separately")
                return
    else:
        pass

    if current_operator != selected_operator:
        for key, val in current_operator.items():
            if selected_operator[key] != val:
                if key == "name" or key == "_id":
                    raise Exception("You cannot update the name or id of an Operator by the Code")
                print(f"({key}) OLD: {selected_operator[key]}\n({key}) NEW: {val}")
                differences.append((key, val))

        for values in differences:
            key, val = values
            collection.update_one({"name": current_operator["name"]}, {"$set": {key: val}})
        print("updates applied")
    else:
        print("There in nothing to update")


Kaltsit = {
    '_id': mg.collection.ObjectId('6272b6b124eade9189bbab7e'),
    'name': "Kal'tsit",
    'img': None,
    'type': 'Medic',
    'archetype': 'single target healer',
    'stats': {
        'base':
            {'hp': 865, 'atk': 167, 'def': 94, 'dp_cost': 18},
        'elite_one':
            {'hp': 1219, 'atk': 274, 'def': 137, 'dp_cost': 20},
        'elite_two':
            {'hp': 1469, 'atk': 392, 'def': 172, 'dp_cost': 20}
    },
    'skills': {
        'command: structural fortification': {
            'sp_cost': 30,
            'duration': 30,
            'effect': 'This unit and Mon3tr gains DEF +60%. This unit also gains 20% Physical resist'
        }},
    'url': None}


def get_operator(operator_name: str, collection: mg.collection.Collection = kaltsitCollection):
    if collection.find_one({"name": {"$eq": operator_name}}) != None:
        operator = dict(collection.find_one({"name": {"$eq": operator_name}}))
        return operator
    else:
        print("this operator does not exists")
        return None


def get_all_operator(collection: mg.collection.Collection = kaltsitCollection, operator:str=""):
    all_operator = []
    operators = collection.find({"name":{"$regex":f"^{operator}"}})
    for operator in operators:
        all_operator.append(dict(operator))
    if len(all_operator) == 0:
        all_operator = None
    return all_operator


def delete_operator(operator: dict, collection: mg.collection.Collection = kaltsitCollection):
    if collection.find_one({"name": {"$eq": operator["name"]}}) != None:
        collection.delete_one(operator)
        print("operator deleted")
    else:
        raise Exception(f"Impossible to delete an inexistent Operator named {operator['name']}")

"""
ROSMOTIS
"synergy": {
        "defense_debuffers":["Shemare", "Pramanix"],
        "redeploy_specialists":["Projekt Red", "Gravel", "Phantom", "Kafka", "Waai fu"],
        "specific_operators":["W"]
        
        } 

MUDROCK 
"synergy":{
        "specific_operators":["Ch'en", "Blemishine", "Aak"],
        "crowd_control":["Texas", "Mayer", "Projekt Red", "Glaucus"]
        }
        

"""