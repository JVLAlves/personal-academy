import random
from pprint import pprint

import pymongo as mg
from pymongo.server_api import ServerApi
from globals.mgconstants import kaltsitCollection, HarmonyCollection

"""
{'_id': ObjectId('6275359e55af10f626578bd8'),
 'archetype': 'Enmity / Juggernaut',
 'growth': {'farming_plan': None,
            'materials': {'crafting_materials': None,
                          'farming_materials': None}},
 'img': 'https://gamepress.gg/arknights/sites/arknights/files/2020-11/char_311_mudrok_1.png',
 'information': {'gender': 'Female',
                 'nation': 'Rhodes Island',
                 'race': 'Sarkaz'},
 'name': 'Mudrock',
 'outfits': {'Obsidian': {'cost': 18,
                          'img': 'https://gamepress.gg/arknights/sites/arknights/files/2022-05/%E7%AB%8B%E7%BB%98_%E6%B3%A5%E5%B2%A9_skin2.png',
                          'series': 'Ambience Synesthesia'},
             'Silent Night DN06': {'cost': 18,
                                   'img': 'https://gamepress.gg/arknights/sites/arknights/files/2021-08/char_311_mudrok_summer%236.png',
                                   'series': 'Coral Coast'}},
 'release': 'Global',
 'skills': {'Bloodline of Desecrated Earth': {'duration': 30,
                                              'effect': 'Upon skill '
                                                        'activation, Mudrock '
                                                        'stops attacking and '
                                                        'does not take damage '
                                                        'for 10 seconds, and '
                                                        'reduces the Movement '
                                                        'Speed of surrounding '
                                                        'enemies by -60%; '
                                                        'After this state '
                                                        'ends, Mudrock Stun '
                                                        'surrounding ground '
                                                        'enemies for 3 seconds '
                                                        'and gains reduced '
                                                        'Attack Interval, ATK '
                                                        '+70%, DEF +30%, and '
                                                        'the ability to attack '
                                                        'multiple targets '
                                                        'equal to block number '
                                                        '(hits any targets '
                                                        'within attack range)* '
                                                        'This Skill modifies '
                                                        'the Attack Interval '
                                                        'by -0.3',
                                              'sp_cost': 35},
            'Crag Splitter': {'duration': None,
                              'effect': 'The next attack restores 4% of this '
                                        "unit's Max HP and deals 170% ATK as "
                                        'Physical damage to all surrounding '
                                        'ground enemies, with a 30% chance to '
                                        'Stun them for 0.4 seconds',
                              'sp_cost': 6},
            'DEF Up γ': {'duration': 40, 'effect': 'DEF +30%', 'sp_cost': 45}},
 'stats': {'base': {'atk': 370, 'def': 229, 'dp_cost': 32, 'hp': 1677},
           'elite_one': {'atk': 515, 'def': 347, 'dp_cost': 34, 'hp': 2207},
           'elite_two': {'atk': 687, 'def': 463, 'dp_cost': 36, 'hp': 2867}},
 'synergy': {'crow_control': ['Mayer', 'Projekt Red', 'Glaucus'],
             'specific_operators': ["Ch'en", 'Blemishine', 'Aak']},
 'tags': [],
 'talents': {'Unshakable Solidarity': 'Takes 30% less damage from Sarkaz '
                                        'enemies',
                                        'Ward of the Fertile Soil': 'Every 9 seconds, gains 1 Shield (Can '
                                        'have up to 2 stacks, with 1 stack '
                                        'granted immediately when deployed). '
                                        'When a Shield is broken, restores '
                                        '15% of Max HP'},
 'traits': 'Cannot be healed by allies',
 'type': 'Defender',
 'url': 'https://gamepress.gg/arknights/operator/mudrock'}
"""


def get_operator(operator_name: str, collection: mg.collection.Collection = kaltsitCollection):
    operator_profile = collection.find_one({"name": operator_name.title()})

    if operator_profile is not None:
        operator = dict(operator_profile)

        pprint(operator)

        return operator
    else:
        return None


def calculate_operators_by_type(type:str, collection: mg.collection.Collection = kaltsitCollection):
    """Calculate how many operators are there with a same type.

    :param type: One of the eight Arknights operator's type
    :param collection: The Arknights MongoDB collection
    :return: The number of operators of the specified type.
    """

    agroupment = {

        "$group": {
            "_id": "$type",
            "Total Operators": {"$sum":1}
        }
    }

    pipeline = [agroupment]

    results = collection.aggregate(pipeline)

    #this first loop is used to return the total number
    for result in results:
        each = dict(result)
        db_type = each["_id"]
        if db_type == type.capitalize():
            return int(each["Total Operators"])

def calculate_operators_outfits(collection:mg.collection.Collection = kaltsitCollection):
    project = {
        #PROJECT creates an new group with specified conditions
        # The differences between GROUP and PROJECT is that GROUP agroups with a certain condition (i.e., same name)
        "$project": {
            "_id": "$name",
            "Total Outfits":
                {
                "$cond": {
                    "if": {"$isArray":{"$objectToArray":"$outfits"}},
                    "then":{"$size":{"$objectToArray":"$outfits"}},
                    "else":0}
                }
        }
    }

    sort = {
        "$sort": {"Total Outfits": mg.DESCENDING}
    }

    match = {
        "$match": {
            "Total Outfits": {"$gt": 0}
        }
    }
    pipeline = [project, sort, match]

    results = collection.aggregate(pipeline)

    for each in results:
        pprint(each)


def operator_isType(operator_name:str, type:str, collection: mg.collection.Collection = kaltsitCollection):
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

def QuickVerify(operators_array:list[str], type:str, collection: mg.collection.Collection = kaltsitCollection):

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



def MatchUpOperators(operator_name:str, acceptRandomness:bool=False, squadForCompartion:list[str]=None, collection: mg.collection.Collection = kaltsitCollection):

    graphLookUp = {
        "$graphLookup":{
            "from": "harmony",
            "startWith":"$name",
            "connectFromField":"synergy",
            "connectToField": "name",
            "maxDepth":10,
            "depthField":"synergyHierarchy",
            "as":"synergyList"
        }
    }

    project = {
        "$project": {
            "name": "$name",
            "synergy": {"$cond":{
                "if":{"$eq":[{"$size":"$synergyList"}, 0]},
                "then": None,
                "else": "$synergyList"
            }}
        }
    }

    match = {
        "$match": {
            "name": operator_name,
            "synergy":{"$ne":None},
        }
    }
    pipeline = [graphLookUp, project, match]

    results = collection.aggregate(pipeline)

    for each in results:
        pprint(each, sort_dicts=False)
        print("\n\n")
        operator = dict(each)
        operator["synergyCollection"] = []
        for harmonious in operator["synergy"]:
            synergetic = dict(harmonious)
            if acceptRandomness and squadForCompartion is not None:
                if synergetic["name"] == operator["name"]:
                    syn = operator["name"]
                    while syn in squadForCompartion:
                        syn = random.choice(synergetic["synergy"])
                    print(syn)
                    operator["synergyCollection"].append(
                    {"name": syn, "nearnessDegree": 1})
            else:
                if synergetic["synergyHierarchy"] > 0:
                    operator["synergyCollection"].append(
                        {"name": synergetic["name"], "nearnessDegree": synergetic["synergyHierarchy"]})


        if len(operator["synergyCollection"]) > 0:
            return operator["synergyCollection"]


def insert_operator(new_operator: dict, collection: mg.collection.Collection=kaltsitCollection):
    if collection.find_one({"name": {"$eq": new_operator["name"]}}) != None:
        print("operator already exists in the Database")
    else:
        collection.insert_one(new_operator)
        print("operator added")
    return


def PopulateHarmony(collection: mg.collection.Collection = kaltsitCollection):
    project = {
        "$project": {
            "_id":0,
            "name":"$name",
            "synergy": "$synergy"
        }
    }

    match = {
        "$match":{
            "synergy": {"$ne":None}
        }
    }

    pipeline = [project, match]

    result = collection.aggregate(pipeline)

    for each in result:
        pprint(each)
        operator = dict(each)
        insert_operator(operator, collection=HarmonyCollection)


def core_relation(core:str):
    squad = [core]
    AbleToRetry = True
    legacy = [core]

    while True:
        synergetics = MatchUpOperators(core)

        nearness = []

        if synergetics is None and AbleToRetry:
            print(f"No Synergy, trying the Core Operator {squad[0]} again")
            synergetics = MatchUpOperators(squad[0], acceptRandomness=True, squadForCompartion=squad)
            print(synergetics)
            AbleToRetry = False
        elif synergetics is not None and AbleToRetry:
            pprint(synergetics)
        else:
            print("No Synergy")
            return squad

        if AbleToRetry:
            for op in synergetics:
                nearness.append(op["nearnessDegree"])

            if len(nearness) > 1:
                nearest = min(nearness)
                nearest_index = nearness.index(nearest)
                nearest_operator = synergetics[nearest_index]["name"]

                furthest = max(nearness)
                furthest_index = nearness.index(furthest)
                furthest_operator = synergetics[furthest_index]["name"]

                print(
                f"Closest Synergy (nearness: {nearest}) --> {nearest_operator}\nFurthest Synergy (nearness: {furthest}) --> {furthest_operator}")

                if nearest_operator in squad:
                    nearest_operator = furthest_operator
            else:
                nearest_operator = synergetics[0]["name"]
                print(nearness[0])

            if nearest_operator in legacy:
                return squad

            core = nearest_operator
        else:
            core = synergetics[0]["name"]
        squad.append(core)
        legacy.append(core)

def SynergyList(collection: mg.collection.Collection = kaltsitCollection):
    project = {
        "$project":{
            "_id":"$name",
            "synergy": "$synergy"
        }
    }

    match = {
        "$match":
            {
                "synergy" : {"$ne":None}
            }
    }

    pipeline = [project, match]

    results = collection.aggregate(pipeline)
    for each in results:
        pprint(each)


if __name__ == '__main__':
    print(core_relation("Lizkarm"))

"""
Blemishine
{"specific_operators": ["Mulberry", "Skadi the Corrupting Heart", "Podenco", "Rosa (Poca)", "Aak", "Warfarin", "Sora"]}

"""