import pymongo as mg
from pymongo.server_api import ServerApi
import globals.errors as err

try:
    client = mg.MongoClient("mongodb+srv://joao:Eu892907@flaghunter.wsia5.mongodb.net/test", server_api=ServerApi('1'))
    database = client["flaghunter"]
    flags_collection = database['flags']
except:
    raise ConnectionError

def insert(flagbearer:dict, collection:mg.collection.Collection=flags_collection):
    if collection.find_one({"hostname":flagbearer["hostname"], "user":flagbearer["user"], "uuid":flagbearer["uuid"]}) == None:
        collection.insert_one(flagbearer)
    else:
        raise err.AlreadyExistsError(flagbearer)

def update(flagbearer:dict, collection:mg.collection.Collection=flags_collection):
    if collection.find_one({"hostname":flagbearer["hostname"], "user":flagbearer["user"], "uuid":flagbearer["uuid"]}) != None:
            previous = dict(collection.find({"hostname":flagbearer["hostname"], "uuid":flagbearer["uuid"]}))
            current = {"$set": flagbearer}
            collection.update_one(previous, current)

    else:
        raise err.NotExistsError(flagbearer)

def Exists(profile:dict, collection:mg.collection.Collection=flags_collection):
    if collection.find_one(profile) != None:
        return True
    else:
        return False


