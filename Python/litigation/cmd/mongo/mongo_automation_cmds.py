import pymongo as mg
from pymongo.server_api import ServerApi

client = mg.MongoClient("mongodb+srv://joao:sdl170502@litty.tivgq.mongodb.net/test", server_api=ServerApi('1'))

database = client["litty"]
automation_collection = database['automation']
user_collection = database['users']


################## COMANDOS PARA AUTOMAÇÕES #############################################################################
#acrescenta um automação ao banco
def insert_automation(automation:dict, collection:mg.collection.Collection=automation_collection):
    if collection.find_one({"name":{"$eq":automation["name"]}}) != None:
        raise Exception("Document already exists")
    else:
        collection.insert_one(automation)
        return

#pega um automação existente no banco utilizando o nome
def get_automation(automation_name:str, collection:mg.collection.Collection=automation_collection):
    if collection.find_one({"name":{"$eq":automation_name}}) != None:
        automation = dict(collection.find_one({"name":{"$eq":automation_name}}))
        return automation
    else:
        raise Exception("This automation does not exists. Please, make sure the name was spelled correctly.")

#pega uma automação no banco utilizando o metodo de query
def query_automation(query:dict, collection:mg.collection.Collection=automation_collection):
    if collection.find_one(query) != None:
        automation = dict(collection.find_one(query))
        return automation
    else:
        raise Exception("This query result in null. Please, make sure it was written correctly.")

#verifica se o nome da automação existe
def automation_exists(automation_name:str, collection:mg.collection.Collection=automation_collection):
    if collection.find_one({"name":{"$eq":automation_name}}) != None:
        return True
    else:
        return False

#apaga uma automação do banco
def delete_automation(query:dict, collection:mg.collection.Collection=automation_collection):
    if collection.find_one(query) != None:
        collection.delete_one(query)
        return
    else:
        raise Exception("Impossible to delete an inexistent query. Make sure it was written correctly.")

########################################################################################################################


