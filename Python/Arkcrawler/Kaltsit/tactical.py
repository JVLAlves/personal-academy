import random

import arknomicon as ark
from pprint import *
import pymongo as mg
import pandas as pd

class operator_resume:
    def __init__(self, operator_dict:dict):
        self.name = operator_dict["name"]
        self.type = operator_dict["type"]
        self.archetype = operator_dict["archetype"]
        self.url_access = operator_dict["url"]


def get_from_type(type:str, collection:mg.collection.Collection=ark.kaltsitCollection):
    all_operator = []
    operators = collection.find({"type": {"$eq":f"{type.capitalize()}"}})
    for operator in operators:
        all_operator.append(dict(operator))
    if len(all_operator) == 0:
        all_operator = None
    return all_operator

def get_from_archetype(archetype:str, collection:mg.collection.Collection=ark.kaltsitCollection):
    all_operator = []
    operators = collection.find({"archetype": {"$regex":f"{archetype}"}})
    for operator in operators:
        all_operator.append(dict(operator))
    if len(all_operator) == 0:
        all_operator = None
    return all_operator


def random_formation():
    JUMP = False
    SQUAD = {
        "build": {
            "medic": 2,
            "defender": 1,
            "vanguard": 2,
            "sniper": 2,
            "caster": 2,
            "guard": 2,
            "any": 1
        },
        "team": []
    }

    for type, quant in SQUAD["build"].items():
        if quant == 0:
            continue
        elif quant < 0:
            raise IndexError
        if type == "any":
            SQUAD["build"]["any"] -= 1
            JUMP = True
            type = random.choice(list(SQUAD["build"].keys()))
            print(f"THE PLAYER CHOICE TYPE IS {type.upper()}")
        operators_of_type = get_from_type(type)
        operator_of_choice = random.choices(operators_of_type, k=quant)
        if not JUMP:
            SQUAD["build"][type] -= len(operator_of_choice)
        else:
            JUMP = False
        for operator in operator_of_choice:
            if operator["name"].find("Reserve Operator") != -1:
                while operator["name"].find("Reserve Operator") != -1:
                    operator = random.choice(operators_of_type)
            SQUAD["team"].append(operator["name"])

    for index, operator in enumerate(SQUAD["team"]):
        mongo_operator = ark.get_operator(operator)
        SQUAD['team'][index] = mongo_operator
    return SQUAD



def balanced_formation():
    JUMP = False
    SQUAD = {
        "build": {
            "AoE / Multi-target Medic": 1,
            "ST / Medic": 1,
            "Normal / Protector": 1,
            "Skill-DP / Pioneer": 2,
            "AoE / Artilleryman": 1,
            "Anti-Air / Marksman": 1,
            "AoE / Splash Caster": 1,
            "ST / Core Caster": 1,
            "Duelist / Dreadnought": 1,
            "Arts Fighter": 1,
            "any": 1
        },
        "team": []
    }
    for arche, quant in SQUAD["build"].items():
        if quant == 0:
            continue
        elif quant < 0:
            raise IndexError
        if arche == "any":
            SQUAD["build"]["any"] -= 1
            JUMP = True
            type = random.choice(["Defender", "Guard", "Supporter", "Specialist", "Sniper", "Vanguard", "Caster", "Medic"])
            print(f"THE PLAYER CHOICE TYPE IS {type.upper()}")
            operators_of_type = get_from_type(type)
            operator = random.choice(operators_of_type)
            if operator["name"].find("Reserve Operator") != -1:
                while operator["name"].find("Reserve Operator") != -1:
                    operator = random.choice(operators_of_type)
            elif operator["name"] in SQUAD["team"]:
                while operator["name"] in SQUAD["team"]:
                    operator = random.choice(operators_of_type)
            SQUAD["team"].append(operator["name"])
            continue

        operators_of_archetype = get_from_archetype(arche)
        operator_of_choice = random.choices(operators_of_archetype, k=quant)
        if not JUMP:
            SQUAD["build"][arche] -= len(operator_of_choice)
        else:
            JUMP = False
        for operator in operator_of_choice:
            if operator["name"].find("Reserve Operator") != -1:
                while operator["name"].find("Reserve Operator") != -1:
                    operator = random.choice(operators_of_archetype)
            elif operator["name"] in SQUAD["team"]:
                while operator["name"] in SQUAD["team"]:
                    operator = random.choice(operators_of_archetype)
            SQUAD["team"].append(operator["name"])

    for index, operator in enumerate(SQUAD["team"]):
        mongo_operator = ark.get_operator(operator)
        SQUAD['team'][index] = mongo_operator
    return SQUAD

def core_formation(operator_core:str):
    JUMP = False
    SQUAD = {
        "build": {
            "medic": 2,
            "defender": 1,
            "vanguard": 2,
            "sniper": 2,
            "caster": 2,
            "guard": 2,
            "any": 1
        },
        "team": []
    }

    #prepare already given data
    core_operator = ark.get_operator(operator_core)
    recommendation = core_operator["synergy"]

    for field in recommendation.keys():
        for index, operator in enumerate(recommendation[field]):
            print(f"Analysing operator: {operator if isinstance(operator, str) else f'object of {operator.name}'}")
            if isinstance(operator, operator_resume):
                continue

            try:
                character = ark.get_operator(operator)
                if character is None:
                    raise Exception()
            except:
                continue
            else:
                recommendation[field][index] = operator_resume(character)


    for field in recommendation.keys():
        toRemove = []
        for operator in recommendation[field]:
            if isinstance(operator, str):
                toRemove.append(operator)
            elif isinstance(operator, operator_resume):
                print(f"name: {operator.name} from {operator}")
            else:
                continue

        for removable in toRemove:
            recommendation[field].remove(removable)

    pprint(recommendation)


    recommendation_length = len(recommendation.keys())

    squad_length = 0

    for v in SQUAD["build"].values():
        squad_length += v

    if squad_length <= 0:
        raise Exception("Error measuring the Squad length.")

    global DFs

    for field in recommendation.keys():
        dataframe = {
            "name": [],
            "type": [],
            "archetype": [],
        }
        for index, operator in enumerate(recommendation[field]):
            dataframe["name"].append(operator.name)
            dataframe["type"].append(operator.type)
            dataframe["archetype"].append(operator.archetype)

        df = pd.DataFrame(dataframe)
        DFs.append(df)
    




if __name__ == "__main__":
    core_formation("W")


"""
Blemishine
{"specific_operators": ["Mudrock", "Kafka", "Ch'en"]}

Eunectes
{"specific_operators":["Nian"]}

Surtr 
{"specific_operators":["Saria", "Suzuran", "Ifrit", "Aak"]}

Thorns
{"SP_batteries":["Liskarm", "Warfarin", "Ptilopsis", "Ch'en"]}

W
{"debuffers":["Saria", "Suzuran", "Shamare", "Pramanix"], "atk_buffer":["Mulberry", "Skadi the Corrupting Heart", "Podenco", "Rosa (Poca)", "Aak", "Warfarin", "Sora"]}

Suzuran
{"slow_debuffers":["Orchid", "Istina", "Saria", "Glaucus"]}

"""