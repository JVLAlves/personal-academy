import sympy as sym
from pprint import pprint
import calculus.itermethods as iter

def inertiaRecX(b: float, h: float):
    return (b * (h ** 3)) / 12


if __name__ == '__main__':
    z = sym.symbols("Z")
    Equation = (-20*(z**2)) + (156*z) + 30
    iEquation = (-40*z) + 126.25
    Eq = iter.EquationPack(z, iEquation)
    print(Eq.getDiff)

