import Kaltsit.arknomicon as ark

import pandas as pd

def biggestInArray(arrays:list):
    maxLenght = 0
    biggerArray = None
    for t in arrays:
        print(f"({len(t)}) {t}")
        if len(t) > maxLenght:
            maxLenght = len(t)
            biggerArray = t
    return maxLenght, biggerArray

types = {}
if __name__ == "__main__":
    operators = ark.get_all_operator()
    dataframe = {
        "Name": [],
        "Type": [],
        "Archetype": [],
        "Promotions": [],
        "Skill Count": [],
    }

    for operator in operators:
        dataframe["Name"].append(operator["name"])
        dataframe["Type"].append(operator["type"])
        dataframe["Archetype"].append(operator["archetype"])
        dataframe["Promotions"].append(len(operator["stats"]))
        dataframe["Skill Count"].append(len(operator["skills"]) if operator["skills"] != None else 0)
    
    df = pd.DataFrame(dataframe)
    print(df.loc[df["Type"]=="Medic",["Name"]])

    """for operator in operators:
        if operator["type"] not in types.keys():
            types[operator["type"]] = [operator["name"]]
        else:
            types[operator["type"]].append(operator["name"])

    Modal, _ = biggestInArray(list(types.values()))

    for t in types.values():
        if len(t) != Modal:
            while len(t) < Modal:
                t.append(None)
        else:
            pass"""




