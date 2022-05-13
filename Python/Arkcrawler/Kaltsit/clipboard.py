import datetime
from pprint import pprint

import pymongo as mg
from pymongo.server_api import ServerApi
import Kaltsit.archive as archive
import cmd2.originum as ori

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


if __name__ == "__main__":
    client = mg.MongoClient(
        "mongodb+srv://joao:sdl170502@kaltsit.gyy0s.mongodb.net/kaltsit?retryWrites=true&w=majority",
        server_api=ServerApi('1'))
    database = client["kaltsit"]
    collection = database["operators"]
    operators = archive.search(headless=True, max_searches=10)
    for operator in operators:
        collection.update_one({"name":f"{operator.name}"}, {"$set": {"url": operator.url}})

    for operator in operators:
        print(operator.name)
        pprint(operator.skills)
        update_skill(operator, collection)

def get_operator(operator_name:str):
    today_moment = datetime.datetime.today()
    today_str = today_moment.strftime("%Y-%m-%dT%H:%M")
    config = ori.Config()
    kaltsit = config["kaltsit"]

    client = mg.MongoClient(
        kaltsit["database_link"],
        server_api=ServerApi('1'))
    database = client["kaltsit"]
    collection = database["operators"]

    query = {"name":operator_name}
    result = collection.find(query)
    operator_data = None
    for oper in result:
        operator_data = dict(oper)

    kaltsit["last_time_run"] = today_str
    with open(ori.CONFIG_FILE, "w") as ConfigFile:
        config.write(ConfigFile)
    return operator_data


