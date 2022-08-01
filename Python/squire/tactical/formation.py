import random

from pprint import *
import pandas as pd
import mongo.operator_cmds as mg_ops


class operator_resume:
    def __init__(self, operator_dict:dict):
        self.name = operator_dict["name"]
        self.type = operator_dict["type"]
        self.archetype = operator_dict["archetype"]
        self.url_access = operator_dict["url"]




def core_formation(operator_name:str, leader:bool=True):

    """Suggests a squad formation based on a single operator.

        The so called 'core operator' is the one whom all other ones will be chosen to match up with.

        :param str operator_name: The core operator name. Must be the full name (case sensitive).
        :param bool leader: Define if the core operator is a part of the squad or if the squad is going to form around it.
    """

    SQUAD = {
            "medic": 2,
            "defender": 1,
            "vanguard": 2,
            "sniper": 2,
            "caster": 2,
            "guard": 2,
            "any": 1
        }

    searching_types = []

    #this is the operator profile
    operator_profile = mg_ops.get_operator(operator_name)
    resume = operator_resume(operator_profile)

    #define the space taken by the core operator
    if not leader and resume.type not in ["support", "specialist"]:
        SQUAD["build"][resume.type] -= 1
    else:
        SQUAD["any"] -= 1

    #create a single list to linearly search the operator by its type in the core operator synergy list
    for type, qty, in SQUAD.items():
        while qty > 0:
            searching_types.append(type)
            qty -= 1

    print(searching_types)

    operator_per_synergy = {"min": 1, "max": 2}

    for synergy_array in operator_profile["synergy"].values():










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