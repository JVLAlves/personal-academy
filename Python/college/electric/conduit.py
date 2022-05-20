import pandas as pd

conduit = pd.ExcelFile("conduit.xlsx")
FIOS = pd.read_excel(conduit, "fios")
CABOS = pd.read_excel(conduit, "cabos")
STEEL = pd.read_excel(conduit, "steel")
PVC = pd.read_excel(conduit, "PVC")
CONDUIT = pd.read_excel(conduit, "PVC_conduit")
print(type(STEEL))
LINE = CONDUIT.loc[CONDUIT["NOM"] == 32]
index = LINE.index[0]
print(LINE.loc[index, "THREEUP"])

def CREATEWIRES(section:int, quantity:int=1, table:pd.core.frame.DataFrame=FIOS):
    AREA_LINE = table.loc[table["SECMIN"]==section]
    index = AREA_LINE.index[0]
    AREA = AREA_LINE.loc[index, "AREATOT"]
    return AREA * quantity

def CREATECABLES(section:int, quantity:int=1, table:pd.core.frame.DataFrame=CABOS):
    AREA_LINE = table.loc[table["SECMIN"]==section]
    index = AREA_LINE.index[0]
    AREA = AREA_LINE.loc[index, "AREATOT"]
    return AREA * quantity

def EXTERNALDIAMETER(AREA:float, table:pd.core.frame.DataFrame=PVC):
    OCCUP = table["OCCUP"]
    NEAREST = None
    for a in OCCUP:
        if a >= AREA:
            NEAREST = a
            break
        else:
            continue

    DIAM = table.loc[OCCUP == NEAREST]
    index = DIAM.index[0]
    Dnom = DIAM.loc[index, "DIAM"]
    return Dnom

print(EXTERNALDIAMETER(216))



EXTERNALDIAMETER(216)
