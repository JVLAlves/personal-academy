class CustomError(Exception):
    pass

def isInList(array, value):
    global isinList
    try:
        x  = array.index(value)
    except:
        isinList = False
    else:
        isinList = True

    return isinList
