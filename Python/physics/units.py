mass_units = {
    "t": {"kg":1000, "g":1000000, "mg":1000000000},
    "kg": {"t":0.001, "g":1000, "mg":1000000},
    "g": {"t":0.000001, "kg":0.001, "mg":1000},
    "mg": {"t":0.000000001, "kg":0.000001, "mg":0.001},
}

length_units = {
        "km": {"hm": 10, "dam":100, "m":1000, "dm":10000, "cm":100000, "mm":1000000},
        "hm": {"km": 0.1, "dam": 10, "m": 100, "dm": 1000, "cm": 10000, "mm": 100000},
        "dam": {"km": 0.01, "hm": 0.1, "m": 10, "dm": 100, "cm": 1000, "mm": 10000},
        "m": {"km": 0.001, "hm": 0.01, "dam": 0.1, "dm": 10, "cm": 100, "mm": 1000},
        "dm": {"km": 0.0001, "hm": 0.001, "dam": 0.01, "m": 0.1, "cm": 10, "mm": 100},
        "cm": {"km": 0.00001, "hm": 0.0001, "dam": 0.001, "m": 0.01, "dm": 0.1, "mm": 10},
        "mm": {"km": 0.000001, "hm": 0.00001, "dam": 0.0001, "m": 0.001, "dm": 0.01, "cm": 0.1},
    }

time_units = {
    "h": {"min":60, "s": 3600},
    "min": {"h": 0.01666, "s":60},
    "s":{"h":0.0002777, "min":0.01666}
}

import helpers
def multiply(a, b):
    global r
    A = a.lower()
    atimes = 1
    B = b.lower()
    btimes = 1

    if helpers.strContains(A, "^"):
        aCompostion = A.split("^")
        A = aCompostion[0]
        atimes = int(aCompostion[1])

    if helpers.strContains(B, "^"):
        bCompostion = B.split("^")
        B = bCompostion[0]
        btimes = int(bCompostion[1])

    if A == B:

        atimes += btimes
        r = A + "^" + str(atimes)
    else:

        r = A + B

    return r

def divide(a, b):
    def multiply(a, b):
        global r
        A = a.lower()
        atimes = 1
        B = b.lower()
        btimes = 1

        if helpers.strContains(A, "^"):
            aCompostion = A.split("^")
            A = aCompostion[0]
            atimes = int(aCompostion[1])

        if helpers.strContains(B, "^"):
            bCompostion = B.split("^")
            B = bCompostion[0]
            btimes = int(bCompostion[1])

        if A == B and (atimes == 1 and btimes == 1):
            return ""
        elif A == B and (atimes != 1 or btimes != 1):
            return "make it better"


print(multiply("m", "m"))

