import math

import helpers

class Diameter:
    dMetrics = {
        "km": {"hm": 10, "dam":100, "m":1000, "dm":10000, "cm":100000, "mm":1000000},
        "hm": {"km": 0.1, "dam": 10, "m": 100, "dm": 1000, "cm": 10000, "mm": 100000},
        "dam": {"km": 0.01, "hm": 0.1, "m": 10, "dm": 100, "cm": 1000, "mm": 10000},
        "m": {"km": 0.001, "hm": 0.01, "dam": 0.1, "dm": 10, "cm": 100, "mm": 1000},
        "dm": {"km": 0.0001, "hm": 0.001, "dam": 0.01, "m": 0.1, "cm": 10, "mm": 100},
        "cm": {"km": 0.00001, "hm": 0.0001, "dam": 0.001, "m": 0.01, "dm": 0.1, "mm": 10},
        "mm": {"km": 0.000001, "hm": 0.00001, "dam": 0.0001, "m": 0.001, "dm": 0.01, "cm": 0.1},
    }
    SI_unit = "m"
    diameter_units = ["km", "hm", "dam", "m", "dm", "cm", "mm"]

    def __init__(self, value, unit):
        self.value = value
        self.unit = unit

    def Raio(self):
        return self.value/2, self.unit

    def convertUnitTo(self,NewUnit):
        #transforma str em lowercase
        if isinstance(NewUnit, str):
            spCorrection = NewUnit.split()
            c = 0
            for v in spCorrection:
                spCorrection[c] = v.lower()
                c+=1
            nCorrection = "".join(spCorrection)
            NewUnit = nCorrection

        #verifica se a unidade é compativel com as unidades de velocidade.
        if not helpers.isInList(self.diameter_units, NewUnit):
            raise helpers.CustomError("{} is not a Speed Unit or isnt available in this class version.".format(NewUnit))

        #realiza conversâo
        for m in self.dMetrics:
            if m == self.unit:
                for u in self.dMetrics[m]:
                    if u == NewUnit:
                        self.value *= round(self.dMetrics[m][u], 3)
                        self.unit = u
                        return

    @property
    def unit(self):
        return self._unit

    @unit.setter
    def unit(self, correction):
        if isinstance(correction, str):
            spCorrection = correction.split()
            c = 0
            for v in spCorrection:
                spCorrection[c] = v.lower()
                c+=1
            nCorrection = "".join(spCorrection)
            self._unit = str(nCorrection) #redundancia de conversão

    def SI(self):
        # realiza conversâo
        if self.unit == self.SI_unit:
            print("Already on SI")
        for m in self.dMetrics:
            if m == self.unit:
                for u in self.dMetrics[m]:
                    if u == self.SI_unit:
                        self.value *= round(self.dMetrics[m][u], 3)
                        self.unit = u
                        return

class Area:

    SI_unit = "m^2"
    def __init__(self, value, unit):
        self.value = value
        self.unit = unit

    @classmethod
    def Square(cls, b, h):
        a = round(b * h, 3)
        return cls(a, "m^2")

    @classmethod
    def Circle(cls, Diameter):
        Diameter.SI()
        R, _ = Diameter.Raio()
        a  = round(math.pi * (R**2), 3)
        return cls(a, "m^2")

    @classmethod
    def AnyTriangle(cls, b, h):
        a  = round((b * h)/2, 3)
        return cls(a, "m^2")

    @classmethod
    def EquiTriagle(cls, i):
        a = round(((i**2)*(math.sqrt(3)))/4, 3)
        return cls(a, "m^2")


class Velocity:
    sMetrics = {
        "m/s" : {"km/h":3.6},
        "km/h": {"m/s":0.2778}
    }
    speed_units = ["m/s", "km/h"]
    SI_unit = "m/s"

    def __init__(self, value, unit):
        self.value = value
        self.unit = unit

    def convertUnitTo(self,NewUnit):
        #transforma str em lowercase
        if isinstance(NewUnit, str):
            spCorrection = NewUnit.split("/")
            c = 0
            for v in spCorrection:
                spCorrection[c] = v.lower()
                c+=1
            nCorrection = "/".join(spCorrection)
            NewUnit = nCorrection

        #verifica se a unidade é compativel com as unidades de velocidade.
        if not helpers.isInList(self.speed_units, NewUnit):
            raise helpers.CustomError("{} is not a Speed Unit or isnt available in this class version.".format(NewUnit))

        #realiza conversâo
        for m in self.sMetrics:
            if m == self.unit:
                for u in self.sMetrics[m]:
                    if u == NewUnit:
                        self.value *= round(self.sMetrics[m][u], 3)
                        self.unit = u
                        return

    @property
    def unit(self):
        return self._unit

    @unit.setter
    def unit(self, correction):
        if isinstance(correction, str):
            spCorrection = correction.split("/")
            c = 0
            for v in spCorrection:
                spCorrection[c] = v.lower()
                c+=1
            nCorrection = "/".join(spCorrection)
            self._unit = str(nCorrection) #redundancia de conversão

    def SI(self):
        # realiza conversâo
        if self.unit == self.SI_unit:
            print("Already on SI")
        for m in self.sMetrics:
            if m == self.unit:
                for u in self.sMetrics[m]:
                    if u == self.SI_unit:
                        self.value *= round(self.sMetrics[m][u], 3)
                        self.unit = u
                        return

    @classmethod
    def calculate(cls, distance, time):
        V = round(distance/time, 3)
        return cls(V, "m/s")


class Flow:
    def __init__(self, value, unit, **kwargs):
        self.value = value
        self.unit = unit
        kwargsCount = len(kwargs)

        if kwargsCount == 1:
            keys = kwargs.keys()
            for x in keys:
                if x == "area":
                    self.area = kwargs[x]
                    self.velocity = self.value / self.area
                elif x == "velocity":
                    self.velocity = kwargs[x]
                    self.area = self.value / self.velocity
        elif kwargsCount == 2:
            self.area = kwargs["area"]
            self.velocity = kwargs["velocity"]
        elif kwargsCount > 2:
            raise helpers.CustomError("Too many kwargs")

    @classmethod
    def calculate(cls, area, velocity):
        Q = round(area.value * velocity.value, 3)
        return cls(Q, "m^3/s", area=area, velocity=velocity)

class Qcomponent:
    def __init__(self, value, unit):
        self.value = value
        self.unit = unit

def Continuity(Flow, Qcomponent):
    global incogValue, incogUnit
    if Qcomponent.unit == "m/s":
        incogUnit = "m^2"
    elif Qcomponent.unit == "m^2":
        incogUnit = "m/s"

    incogValue = round((Flow.value) / Qcomponent.value, 3)

    if incogUnit == "m/s":
        return Velocity(incogValue, incogUnit)
    elif incogUnit == "m^2":
        return Area(incogValue, incogUnit)