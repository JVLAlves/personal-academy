import random

import arknomicon as ark
from pprint import *
import pymongo as mg



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
    operators = collection.find({"archetype": {"$regex":f"{archetype.title()}"}})
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
    return SQUAD



def balanced_formation():
    SQUAD = {
        "build": {
            "AoE / Multi-target Medic": 1,
            "ST / Medic": 1,
            "defender": 1,
            "Skill-DP / Pioneer": 2,
            "Aoe / Artilleryman": 1,
            "Anti-Air / Marksman": 1,
            "AoE / Splash Caster": 1,
            "ST / Core Caster": 1,
            "Duelist / Dreadnpught": 1,
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
            SQUAD["team"].append(operator["name"])
            continue

        print()
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
            SQUAD["team"].append(operator["name"])
    return SQUAD



SQUAD = balanced_formation()
pprint(SQUAD)




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