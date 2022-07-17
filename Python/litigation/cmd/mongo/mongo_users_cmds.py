import pymongo as mg
from pymongo.server_api import ServerApi

client = mg.MongoClient("mongodb+srv://joao:sdl170502@litty.tivgq.mongodb.net/test", server_api=ServerApi('1'))

database = client["litty"]
user_collection = database['users']



############## COMANDOS PARA USUARIOS ##################################################################################

#acrescenta um automação ao banco
def insert_user(user:dict, collection:mg.collection.Collection=user_collection):
    try:
        collection.find_one({"username": {"$eq": user["username"]}})
    except:
        collection.insert_one(user)
        return
    else:
        if collection.find_one({"username": {"$eq": user["username"]}}) != None:
            raise Exception("User already exists")
        else:
            collection.insert_one(user)
            return


#pega um automação existente no banco utilizando o nome
def get_user(user_name:str, collection:mg.collection.Collection=user_collection):
    if collection.find_one({"username":{"$eq":user_name}}) != None:
        user = dict(collection.find_one({"username":{"$eq":user_name}}))
        return user
    else:
        raise Exception("This user does not exists. Please, make sure the name was spelled correctly.")

#pega uma automação no banco utilizando o metodo de query
def query_user(query:dict, collection:mg.collection.Collection=user_collection):
    if collection.find_one(query) != None:
        user = dict(collection.find_one(query))
        return user
    else:
        raise Exception("This query result in null. Please, make sure it was written correctly.")

#verifica se o nome da automação existe
def user_exists(user_name:str, collection:mg.collection.Collection=user_collection):
    if collection.find_one({"username":{"$eq":user_name}}) != None:
        return True
    else:
        return False

#verifica se há algum usuario ou se o banco está vazio
def user_any(username:str="", collection:mg.collection.Collection=user_collection):
    all_users = []
    try:
        users = collection.find({"username": {"$regex": f"^{username}"}})
    except:
        return False
    else:
        for user in users:
            all_users.append(dict(user))
        if len(all_users) > 0:
            return True
        else:
            return False


#apaga uma automação do banco
def delete_user(query:dict, collection:mg.collection.Collection=user_collection):
    if collection.find_one(query) != None:
        collection.delete_one(query)
        return
    else:
        raise Exception("Impossible to delete an inexistent query. Make sure it was written correctly.")