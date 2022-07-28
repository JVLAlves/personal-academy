from pprint import pprint

import pandas as pd
import os
from configparser import ConfigParser


class File:
    def __init__(self, file: str):

        # verify if file path exists
        if not os.path.exists(file):
            raise FileNotFoundError

        # verify if the file is actually a file
        if not os.path.isfile(file):
            raise FileExistsError

        # select the filename, absolute path and directory
        self.file = os.path.basename(file)
        _, self.extension = os.path.splitext(self.file)
        self.filename = self.file.replace(self.extension, "")
        self.path = os.path.realpath(file)
        self.dir = os.path.dirname(self.path)

        if self.extension == ".xlsx" or self.extension == ".xls":
            self.DF = pd.read_excel(self.path)
        elif self.extension == ".csv":
            self.DF = pd.read_csv(self.path)
        elif self.file.endswith(".docx"):
            pass
        else:
            raise Exception("File not supported")


# this function opens the excel database and collect all data from it
def getAllProcesses(file: File = File):
    # list all the process information
    AllProcesses = []
    for row in file.DF.iterrows():
        index, df = row
        AllProcesses.append(dict(df))
    return AllProcesses


def getByColumnValue(Column_header: str, value, file: File = File):
    # Get all processes which correspond to a given condition
    DFspec = file.DF.loc[file.DF[Column_header] == value]

    # list all the process information
    specProcesses = []
    for row in DFspec.iterrows():
        index, df = row
        specProcesses.append(dict(df))
    return specProcesses


def getVerticalHeaders(file: File, ColumnHeader: str):
    DF = file.DF

    keys = list(DF.loc[:, ColumnHeader])

    print(keys)
    answerSheet = {}
    for k in keys:
        answerSheet[str(k)] = None
    pprint(answerSheet)
    return answerSheet


def CreateContextGenerator(file:File, verticalHeaders: bool = False):
    """Creates a context generator function.

    :param file: Is the file which contains the data table.
    :param verticalHeaders: Indicates if the table headers are in vertical position or horizontal position.
    :return: A function to generate a context and the Header position.
    """

    def getVerticalHeadersTbl():

        """This functions reads a table in which the Headers are in vertical position.
        It is considered this table have only two columns and all Headers are in the first column.

        :return: A list with contexts.
        """

        DF = file.DF
        print(DF)

        headers = list(DF)

        keys = list(DF.loc[:, headers[0]])
        values = list(DF.loc[:, headers[1]])
        print(keys, values)
        answerSheet = {}
        for k, v in zip(keys, values):
            if isinstance(v, str) and v.find(", ") != -1:
                if k.lower().endswith("s"):

                    answerSheet[str(k)] = v.strip()
                else:
                    endstr = None
                    if k.islower() or k.istitle():
                        endstr = "s"
                    elif k.isupper():
                        endstr = "S"
                    answerSheet[str(k)+endstr] = v.strip()
                v = v.strip().split(", ")
            answerSheet[str(k)] = v
        return [answerSheet]

    def getHorizontalHeadersTbl():

        """This functions reads a table in which the Headers are in horizontal position.
        It is considered this table have Headers in the first row of the file and the rows below represents individual data.

        :return: A list with contexts.
        """

        answerSheets = []

        DF = file.DF


        keys = list(DF)

        clients_count = len(DF.index)
        loop_counter = 0

        while loop_counter < clients_count:
            answerSheet = {}
            client = (DF.loc[loop_counter])
            for k, v in zip(keys, client):
                if isinstance(v, str) and v.find(", ") != -1:
                    if k.lower().endswith("s"):

                        answerSheet[str(k)] = v.strip()
                    else:
                        endstr = None
                        if k.islower() or k.istitle():
                            endstr = "s"
                        elif k.isupper():
                            endstr = "S"
                        answerSheet[str(k) + endstr] = v.strip()
                    v = v.strip().split(", ")
                    answerSheet[str(k)] = v

            answerSheets.append(answerSheet)
            loop_counter += 1

        return answerSheets

    if verticalHeaders:
        return getVerticalHeadersTbl
    else:
        return getHorizontalHeadersTbl
object

if __name__ == '__main__':
    GenerateContext = CreateContextGenerator(File(
        "/Users/joaovitor/projects/repo/personal-academy/Python/litigation/LITTY/LITTY - REF - cópia/PLANILHA REFERENCIA - COM CELULA COMPOSTA.xlsx"),
                                                True)
    context = GenerateContext()
    pprint(context, sort_dicts=False)
