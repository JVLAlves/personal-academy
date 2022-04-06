import pandas as pd
class Tfuds:
    def __init__(self, filename):
        self.__invFi = None
        self.__invFri = None
        self.__Fri = None
        self.__totalfi = None
        self.__fri = None
        self.__Fi = None
        self.__fi = None
        fComposition = filename.split(".")
        if len(fComposition) != 2:
            print("Not a valid file.")
            return
        fExtension = fComposition[1]
        if fExtension == "csv":
            self.__Dataframe = pd.read_csv(filename)
        elif fExtension == "xlsx":
            self.__Dataframe = pd.read_excel(filename)

    def __isMissingValue(self, array):
        for index, v in enumerate(array):
            print(v, index)
            if pd.isna(v):
                return True, index
        return False, -1

    def __isMissingTotal(self, isMissingValue, array):
        if not isMissingValue:
            array_lastPosition = len(array) - 1
            if sum(array) == array[array_lastPosition]:
                return False
            else:
                return True
        else:
            return

    def fi(self):

        #Frequencia Simples Absoluta
        __fi = self.__Dataframe['fi']
        fi_lastPosition = len(__fi) - 1
        isMissing, index = self.__isMissingValue(__fi[:fi_lastPosition])
        print(isMissing, index)
        if isMissing:
            __fiToSum = list(__fi[:index])
            __fiToSum.extend(list(__fi[index+1:fi_lastPosition]))

            fi_sum = sum(__fiToSum)
            fi_total = self.__Dataframe.loc[fi_lastPosition, "fi"]
            missingValue = fi_total - fi_sum
            print("{} = {} - {}".format(missingValue, fi_total, fi_sum))

            self.__Dataframe.loc[index, "fi"] = missingValue
        else:
            __fi = self.__Dataframe['fi']
            isMissingV, _ = self.__isMissingValue(__fi)
            isMissingT = self.__isMissingTotal(isMissing, __fi)
            if isMissingT:
                __total = sum(__fi)
                self.__Dataframe.loc[len(__fi)+1, "fi"] = __total
                self.__fi = self.__Dataframe['fi']
                self.__totalfi = __total



    def fri(self):
        #Frequencia Simples Relativa
        __fi = self.__Dataframe['fi']
        __fri = []
        for fi in __fi:
            __fri.append(round((fi/self.__totalfi)*100, 2))

        if __fri[-1] != 100.0:
            print("Frequencia Simples Relativa não fecha. Favor conferir tabela.")
            print(__fri)
            return
        else:
            self.__Dataframe.loc[:, 'fri'] = __fri
            self.__fri = self.__Dataframe['fri']

    def Fi(self):
        #Frequencia Acumulada Absoluta
        Fi = []
        __sFi = 0
        for fi in self.__fi:
            __sFi += fi
            Fi.append(__sFi)
            print(len(Fi), len(self.__fi))

        if Fi[-1] != self.__totalfi:
            print("Frequencia Acumulada Absoluta não fecha. Favor conferir tabela.")
            print(Fi)
            return
        else:
            if len(Fi) != len(self.__fi):
                Fi.append(None)
            self.__Dataframe.loc[:, "Fi"] = Fi
            self.__Fi = self.__Dataframe.loc[:len(self.__fi)-1, "Fi"]

    def Fri(self):
        #Frequencia Acumulada Relativa
        __Fri = []
        for Fi in self.__Fi:
            __Fri.append(round((Fi/self.__totalfi)*100, 1))

        if __Fri[-1] != 100.0:
            print("Frequencia Acumulada Relativa não fecha. Favor conferir tabela.")
            print(__Fri)
            return
        else:
            if len(__Fri) != len(self.__fi):
                __Fri.append(None)
            self.__Dataframe.loc[:, "Fri"] = __Fri
            self.__Fri = self.__Dataframe.loc[:len(self.__fi)-1, "Fri"]


    def invFi(self):
        #Frequencia Acumalada Inversa Absoluta
        __inFi = []
        __sinFi = 0
        for i in range((len(self.__fi)) - 1, -1, -1):
            __sinFi += self.__Fi[i]
            __inFi.append(__sinFi)

        if __inFi[-1] != self.__totalfi:
            print("Frequencia Acumalada Inversa Absoluta não fecha. Favor conferir tabela.")
            print(__inFi)
            return
        else:
            __inFi.sort(reverse=True)
            if len(__inFi) != len(self.__fi):
                __inFi.append(None)
            self.__Dataframe.loc[:, "invFi"] = __inFi
            self.__invFi = self.__Dataframe.loc[:len(self.__fi)-1, "invFi"]

    def invFri(self):
        #Frequencia Acumulada Inversa Relativa
        __inFri = []
        for iFi in self.__invFi:
            __inFri.append(round((iFi/self.__totalfi)*100, 1))
            if __inFri[0] != 100.0:
                print("Frequencia Acumulada Inversa Relativa não fecha. Favor conferir tabela.")
                print(__inFri)
                return
            else:
                if len(__inFri) != len(self.__fi):
                    __inFri.append(None)
                self.__Dataframe.loc[:, "invFri"] = __inFri
                self.__invFri = self.__Dataframe.loc[:len(self.__fi)-1, "invFri"]

    @property
    def Dataframe(self):
        self.fi()
        self.fri()
        self.Fi()
        self.Fri()
        self.invFi()
        self.invFri()
        return self.__Dataframe




df = Tfuds("Q1TPROEST.csv")
print(df.Dataframe)
