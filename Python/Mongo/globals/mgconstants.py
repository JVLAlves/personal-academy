import pymongo as mg
from pymongo.server_api import ServerApi

client = mg.MongoClient(
    "mongodb+srv://joao:sdl170502@kaltsit.gyy0s.mongodb.net/kaltsit?retryWrites=true&w=majority",
    server_api=ServerApi('1'))
database = client["kaltsit"]
try:
    kaltsitCollection = database["operators"]
    HarmonyCollection = database["harmony"]
except:
    print("Is this a new computer?\nHave you added the new IP?\n")
