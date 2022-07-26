from pprint import pprint

import pymongo as mg
from pymongo.server_api import ServerApi
from globals.errors import NonExistentError

client = mg.MongoClient(
    "mongodb+srv://joao:sdl170502@kaltsit.gyy0s.mongodb.net/kaltsit?retryWrites=true&w=majority",
    server_api=ServerApi('1'))
database = client["kaltsit"]
try:
    kaltsitCollection = database["operators"]
except:
    print("Is this a new computer?\nHave you added the new IP?\n")


def query_operator(query: dict, collection: mg.collection.Collection = kaltsitCollection):
    operator_bundle = []
    operators = collection.find(query)
    for operator in operators:
        operator_bundle.append(dict(operator))

    if len(operator_bundle) == 0:
        operator_bundle = None
    return operator_bundle


def get_operator(operator_name: str, collection: mg.collection.Collection = kaltsitCollection):
    if collection.find_one({"name": {"$eq": operator_name}}) != None:
        operator = dict(collection.find_one({"name": {"$eq": operator_name}}))
        return operator
    else:
        raise NonExistentError


def get_from_type(type: str, collection: mg.collection.Collection = kaltsitCollection):
    all_operator = []
    operators = collection.find({"type": {"$eq": f"{type.capitalize()}"}})
    for operator in operators:
        all_operator.append(dict(operator))
    if len(all_operator) == 0:
        all_operator = None
    return all_operator


def get_from_archetype(archetype: str, collection: mg.collection.Collection = kaltsitCollection):
    all_operator = []
    operators = collection.find({"archetype": {"$regex": f"{archetype}"}})
    for operator in operators:
        all_operator.append(dict(operator))
    if len(all_operator) == 0:
        all_operator = None
    return all_operator

####################### AGGREGATION METHODS ###############################################################
def operator_isType(operator_name:str, type:str, collection: mg.collection.Collection = kaltsitCollection):

    """Searches in the Database and verifies if the given operator is from the given type

    :param operator_name: The name of the Operator.
    :param type: One of the eight Arknights Operators types.
    :param collection: The MongoDB Arknights Database.
    """

    project = {
        "$project":
            {
                "_id": "$name",
                "isType":
                    {
                    "$cond":
                        {
                        "if": {"$eq": ["$type", type.capitalize()]},
                        "then": True,
                        "else": False
                        }
                    }
            }
    }

    match = {
        "$match": {
            "_id": {"$eq": operator_name.title()}
        }
    }

    pipeline = [project, match]

    results = collection.aggregate(pipeline)
    for each in results:
        operator_search = dict(each)
        if operator_search["_id"] == operator_name.title():
            return operator_search["isType"]


def operators_QuickVerify(operators_array:list[str], type:str, collection: mg.collection.Collection = kaltsitCollection):
    """Quickly verify which - if any - of the given array of operators match the specified type

    :param operators_array: An array of operators' names. WARNING: they MUST be written correctly.
    :param type: One of the eight Arknights Operators types.
    :param collection: collection: The MongoDB Arknights Database.
    :return: The matching names.
    """



    project = {
        "$project":
            {
                "_id": "$name",
                "type": "$type"
            }
    }


    match = {
        "$match":
            {
                "_id": {"$in":operators_array},
                "type": {"$eq": type.capitalize()}
            }
    }

    pipeline = [project, match]

    results = collection.aggregate(pipeline)

    valid_operators = []
    for each in results:
        valid_operators.append(each["_id"])

    if len(valid_operators) != 0:
        return valid_operators
    else: return None


if __name__ == '__main__':
    print()
