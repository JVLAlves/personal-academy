
import sympy.physics.units as units
from sympy.physics.units import convert_to, Unit
from sympy.physics.units.systems import SI
from sympy.physics.units.quantities import Quantity
from resis.units import kN, MPa
#Teor de umidade (%)
def wh(Wh2o:float, Ws:float):
    return (Wh2o/Ws)*100

def w(W:float, Ws:float):
    return ((W-Ws)/Ws)*100


#Indice de Vazios (Adimensional)
def e(Vv:float, Vs:float):
    e = Vv/Vs

    if e >= 0.5 or e <= 1.5:
        return e
    else:
        raise Exception("ValueExpectedError: Valor está fora da margem de limites esperados.")

def en(n:float):

    return n/(1-n)


#Porosidade (%)
def n(Vv:float, V:float):
    n = (Vv/V)*100

    if n >= 30 or n <= 70:
        return e
    else:
        raise Exception("ValueExpectedError: Valor está fora da margem de limites esperados.")


#Grau de Saturação (%)
def S(Vh2o:float, Vv:float):
    S = (Vh2o/Vv)*100

    if S < 0:
        raise ValueError

    if S == 0:
        print("Solo Seco")
    elif S == 100:
        print("Solo Saturado")

    return S


# Peso especifico Generico (kN/m3)
def GammaNatural(W:float, V:float):
    return W/V

def GammaSolids(Ws:float, Vs:float):
    return GammaNatural(Ws, Vs)

def GammaDried(Ws:float, V:float):
    return GammaNatural(Ws, V)

def GammaSat(Ws:float, Wh2o:float, V:float):
    return (Ws+Wh2o)/V

def GammaSub(GammaNat:float, GammaH2O:float=1.0):
    return GammaNat - GammaH2O

def Consistency(w:float, LL:float, LP:float):

    return (LL - w)/(LL-LP)