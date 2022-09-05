import random
import time
import sympy as symp
from typing import Tuple

symp.init_printing(use_unicode=True)


class Neraph_struct:
    def __init__(self, var: symp.core.symbol.Symbol, eq, diff):
        self.var = var
        self.eq = eq
        self.diff = diff

    def Solve(self, x: float):
        y = float(self.eq.subs(self.var, x))
        y_ = float(self.diff.subs(self.var, x))
        return y, y_


class EquationPack(Neraph_struct):
    def __init__(self, var: symp.core.symbol.Symbol, eq):
        self.id = id
        self.__diff = symp.diff(eq)
        self.__integer = symp.integrate(eq)
        super().__init__(var, eq, self.__diff)

    @property
    def getDiff(self):
        return self.__diff

    @property
    def getInteger(self):
        return self.__integer


# def equationPack(var:float):
#     x =  symp.symbols("x")
#
#     x0 = float(((x**2) - 2).subs(x,var))
#
#     x1 = float(symp.diff(((x**2) - 2), x).subs(x, var))
#
#     return x0, x1


def create_eq(func):
    def core_eq(x):
        y, y_ = func(x)
        return y, y_

    return core_eq


def generate_timer(seconds: int):
    def timer():
        x = 0
        while x <= seconds:
            print(x)
            time.sleep(1)
            x += 1

    return timer


# this is a function which represents the Newton Raphson iteration metthod.
def Neraph(func, seed: float, epsilon: float, tolerance: float = 0.001, max_iterations: int = 100):
    x0 = seed

    for i in range(max_iterations):
        print(f"Iteration {i}, x0 = {x0}")
        y, y_ = func(x0)

        if abs(y_) < epsilon:
            break

        x1 = x0 - y / y_

        if abs(x1 - x0) <= tolerance:
            print(f"SUCCESS! x = {x1}")
            return

        x0 = x1

    print("FAIL!")


########################################################################################################################

def GenerateCoinLauncher():
    def CoinLauncher():
        coin = ["head", "tail"]
        return random.choice(coin)

    return CoinLauncher


def Elastic_line(eq, z, struct: int, values:tuple):




    # Parameters verification
    if struct not in [-1, 1, 2]:
        raise ValueError

    if len(values) != 3:
        raise ValueError




    C1, C2 = symp.symbols("C:2")
    theta = symp.integrate(eq, z)/2 + C1
    y = symp.integrate(theta, z) + C2

    # Condições de Contorno

    if struct == -1:
        # Viga Engastada Invertida
        # Z = l --> Theta = 0 e Y = 0

        L = symp.Dummy("l")  # Constante l (comprimento total da viga)
        E = symp.Dummy("E")  # Modulo de Elasticidade
        i = symp.Dummy("I")  # Inercia da Seção

        # Equação das Tangentes -- C1
        thetaC = symp.Eq(theta, 0).subs(z, L)
        C1v = symp.solve(thetaC)
        C1v = C1v[0][list(C1v[0].keys())[0]]

        theta = theta.subs({C1: C1v})

        print("Tangents' Equation:\n")
        theta = theta / (E * i)
        symp.pprint(theta)
        print()

        # Equação da Linha Elastica -- C2
        y = y.subs({C1: C1v})
        yC = symp.Eq(y, 0).subs(z, L)
        C2v = symp.solve(yC)
        C2v = C2v[0][list(C2v[0].keys())[0]]

        y = y.subs({C2: C2v})

        print("Elastic Line's Equation:\n")
        y = y / (E * i)
        symp.pprint(y)
        print()

        length, Elastic_Module, Inertia = values
        theta = theta.subs({L: length, E: Elastic_Module, i: Inertia})
        y = y.subs({L: length, E: Elastic_Module, i: Inertia})

        if struct == 2:
            # Viga Engastada Invertida
            # Z = 0 e Z = l --> Y = 0

            L = symp.Dummy("l")  # Constante l (comprimento total da viga)
            E = symp.Dummy("E")  # Modulo de Elasticidade
            i = symp.Dummy("I")  # Inercia da Seção

            # Equação das Tangentes -- C2
            yC2 = symp.Eq(y, 0).subs(z, 0)
            C2v = symp.solve(yC2)
            C2v = C1v[0][list(C2v[0].keys())[0]]

            y = y.subs({C2: C2v})

            # Equação da Linha Elastica -- C1
            yC1 = symp.Eq(y, 0).subs(z, L)
            C1v = symp.solve(yC1)
            C1v = C2v[0][list(C1v[0].keys())[0]]

            y = y.subs({C1: C1v})

            print("Tangents' Equation:\n")
            theta.subs({C1: C1v})
            theta = theta / (E * i)
            symp.pprint(theta)
            print()

            print("Elastic Line's Equation:\n")
            y = y / (E * i)
            symp.pprint(y)
            print()

        length, Elastic_Module, Inertia = values
        theta = theta.subs({L: length, E: Elastic_Module, i: Inertia})
        y = y.subs({L: length, E: Elastic_Module, i: Inertia})

    return theta, y


if __name__ == "__main__":
    z = symp.var("z")
    p = symp.symbols("p")
    L = symp.Dummy("l")  # Constante l (comprimento total da viga)
    E = symp.Dummy("E")  # Modulo de Elasticidade
    i = symp.Dummy("I")  # Inercia da Seção
    t, y = Elastic_line(-p, z, -1, (L, E, i))

    y = y.subs({p:5, z:400})
    print(float(y))

