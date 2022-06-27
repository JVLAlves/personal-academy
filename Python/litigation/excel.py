import pandas as pd
import os
from configparser import ConfigParser

class File:
    def __init__(self, file:str):

        # verify if file path exists
        if not os.path.exists(file):
            raise FileNotFoundError

        # verify if the file is actually a file
        if not os.path.isfile(file):
            raise FileExistsError

        # select the filename, absolute path and directory
        self.file = os.path.basename(file)
        self.path = os.path.realpath(file)
        self.dir = os.path.dirname(self.path)

        if self.file.endswith(".xlsx") or self.file.endswith(".xls"):
            self.DF = pd.read_excel(self.path)
        elif self.file.endswith(".csv"):
            self.DF = pd.read_csv(self.path)
        elif self.file.endswith(".docx"):
            pass
        else:
            raise Exception("File not supported")



#TODO: Refactor function to have no default values, but first initiation window
def init():
    file = "deluiz_config.ini"
    if not os.path.exists(file):
        with open(file, "x"):
            pass
    else:
        pass
    conf = ConfigParser()
    conf.read(file)

    try:
        TEMPLATE = conf["database"]["docx"]
        TABLE = conf["database"]["table"]
        if (TEMPLATE is None or TEMPLATE == "") or (TABLE is None or TABLE == ""):
            raise Exception()
        else:
            pass
    except:
        conf.set("database", "docx", "litigation_template.docx")
        conf.set("database", "table", "litigation_template.xlsx")
        with open(file, "w") as conffile:
            conf.write(conffile)

        TEMPLATE = conf["database"]["docx"]
        TABLE = conf["database"]["table"]
    else:
        pass

    return TEMPLATE, TABLE

_, TABLE, = init()
#this function opens the excel database and collect all data from it
def getAllProcesses(file:File=File(TABLE)):

    #list all the process information
    AllProcesses = []
    for row in file.DF.iterrows():
        index, df = row
        AllProcesses.append(dict(df))
    return AllProcesses

def getByColumnValue( Column_header:str, value, file:File=File(TABLE),):
    #Get all processes which correspond to a given condition
    DFspec = file.DF.loc[file.DF[Column_header]==value]

    # list all the process information
    specProcesses = []
    for row in DFspec.iterrows():
        index, df = row
        specProcesses.append(dict(df))
    return specProcesses
