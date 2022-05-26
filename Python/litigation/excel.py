import pandas as pd


def getAllProcesses(file:str):
    try:
        open(file, "r")
    except:
        raise Exception("File does not exists")
    else:
        pass
    excel_DF = pd.read_excel(file)
    AllProcesses = []
    for row in excel_DF.iterrows():
        index, df = row
        AllProcesses.append(dict(df))
    return AllProcesses

if __name__ == "__main__":
    print(getAllProcesses("litigation_template.xlsx"))