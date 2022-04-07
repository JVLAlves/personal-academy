import math


class Velocidade:
    Vmetrics = {
        "m/s": {"km/h":3.6},
        "km/h":{"m/s":0.2778},
    }
    def __init__(self, value, unit):
        self.value = value
        self.unit = unit
    def ConvertUnitTo(self, AlterUnit):
        NewUnit = ""
        Conv = 0
        for m in self.Vmetrics:
            if m == self.unit:
                for u in self.Vmetrics[m]:
                    if u == AlterUnit:
                        Conv = self.Vmetrics[m][u]
                        NewUnit = u
                        break
                break
        self.value = round(self.value * Conv, 3)
        self.unit = NewUnit

class Diametro:
    Dmetrics = {
        "km":{"hm":10, "dam":100, "m":1000, "dm":10000, "cm":100000, "mm":1000000},
        "hm":{"km":0.1, "dam":10, "m":100, "dm":1000, "cm":10000, "mm":100000},
        "dam": {"km": 0.01, "hm": 0.1, "m": 10, "dm": 100, "cm": 1000, "mm": 10000},
        "m": {"km": 0.001, "hm": 0.01, "dam": 0.1, "dm": 10, "cm": 100, "mm": 1000},
        "dm": {"km": 0.0001, "hm": 0.001,"dam":0.01, "m": 0.1, "cm": 10, "mm": 100},
        "cm": {"km": 0.00001, "hm": 0.0001, "dam": 0.001, "m": 0.01, "dm":0.1, "mm": 10},
        "mm": {"km": 0.000001, "hm": 0.00001, "dam": 0.0001, "m": 0.001, "dm": 0.01, "cm": 0.1},
    }
    def __init__(self, value, unit):
        self.value = value
        self.unit = unit

    def ConvertUnitTo(self, AlterUnit):
        NewUnit = ""
        Conv = 0
        for m in self.Dmetrics:
            if m == self.unit:
                for u in self.Dmetrics[m]:
                    if u == AlterUnit:
                        Conv = self.Dmetrics[m][u]
                        NewUnit = u
                        break
                break
        self.value = round(self.value * Conv, 3)
        self.unit = NewUnit

    def Raio(self):
        return round(self.value/2, 3), self.unit

    def Area(self):
        RaioV, _ = self.Raio()
        A = math.pi * (RaioV**2)
        return round(A, 3), self.unit

    def Volume(self, height):
        if height.unit != self.unit:
            height.ConvertUnitTo(self.unit)
        Area, _ = self.Area()
        return round(Area*height.value, 3), self.unit

class Altura:
    Dmetrics = {
        "km": {"hm": 10, "dam": 100, "m": 1000, "dm": 10000, "cm": 100000, "mm": 1000000},
        "hm": {"km": 0.1, "dam": 10, "m": 100, "dm": 1000, "cm": 10000, "mm": 100000},
        "dam": {"km": 0.01, "hm": 0.1, "m": 10, "dm": 100, "cm": 1000, "mm": 10000},
        "m": {"km": 0.001, "hm": 0.01, "dam": 0.1, "dm": 10, "cm": 100, "mm": 1000},
        "dm": {"km": 0.0001, "hm": 0.001, "dam": 0.01, "m": 0.1, "cm": 10, "mm": 100},
        "cm": {"km": 0.00001, "hm": 0.0001, "dam": 0.001, "m": 0.01, "dm": 0.1, "mm": 10},
        "mm": {"km": 0.000001, "hm": 0.00001, "dam": 0.0001, "m": 0.001, "dm": 0.01, "cm": 0.1},
    }

    def __init__(self, value, unit):
        self.value = value
        self.unit = unit

    def ConvertUnitTo(self, AlterUnit):
        NewUnit = ""
        Conv = 0
        for m in self.Dmetrics:
            if m == self.unit:
                for u in self.Dmetrics[m]:
                    if u == AlterUnit:
                        Conv = self.Dmetrics[m][u]
                        NewUnit = u
                        break
                break
        self.value = round(self.value * Conv, 3)
        self.unit = NewUnit

class PesoEspecifico:
    Gravity = 9.81
    GravityUnit = "m/s^2"

    def __init__(self, value, unit):
        self.value = value
        self.unit = unit

    def H2O(self):
        return 9810, "N/m^3"

    @classmethod
    def CalculateFromMass(self, MassaEspecifica):
        if MassaEspecifica.unit != "kg/m^3":
            MassaEspecifica.ConvertUnitTo("kg/m^3")
        self.value = MassaEspecifica.value * self.Gravity
        self.unit = "N/m^3"

class MassaEspecifica:
    Mmetrics = {
        "kg/m^3": {"g/m^3":1000, "kg/l":0.001, "g/l":1, "t/m^3":0.001, "g/cm^3":0.001},
        "g/m^3": {"kg/m^3":0.001, "kg/l":0.000001, "g/l":0.001, "t/m^3":0.000001, "g/cm^3":0.000001},
    }
    def __init__(self, value, unit):
        self.value = value
        self.unit = unit

    def ConvertUnitTo(self, AlterUnit):
        NewUnit = ""
        Conv = 0
        for m in self.Mmetrics:
            if m == self.unit:
                for u in self.Mmetrics[m]:
                    if u == AlterUnit:
                        Conv = self.Mmetrics[m][u]
                        NewUnit = u
                        break
                break
        self.value = round(self.value * Conv, 3)
        self.unit = NewUnit

    @classmethod
    def Calculate(self, mass, volume): 
        self.value = mass/volume
        self.unit = "kg/m^3"