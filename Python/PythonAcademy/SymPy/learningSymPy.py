from sympy import *

x, y, z = symbols("x y z")  ##Construindo variaveis
init_printing(use_unicode=True)  # print em unicode?
dxdy = diff(5 * x ** 3 + cos(x), x)  # Derivada
print(dxdy)
print(integrate(dxdy))  # Integral

Va = symbols("Va")
eq = Eq(Va + 10, 0)  # gera uma equação igualdade, colocando-se a formula de um lado e o resultado do outro.

ans = solveset(eq, Va)  # Calcula a resulução da equação tendo como referencia a variavel/simbolo indicada.

nResult = (Va + 10).subs(Va, 20)  # Substitui uma variavel indicada por um valor também indicado.

##################################
kg, m, s = symbols("kg m s")  #
eq2 = (m / s) * (m ** 2)  # --> Resolução do calculo de Unidade da vazao.
print(eq2)  #
##################################

units = list(symbols("km h"))
eq3 = (units[0] / units[1]) * units[0]
print(eq3)


def strContains(str, c):
    ans = str.find(c)
    if ans == -1:
        return False
    else:
        return True


class Quantity:
    def __init__(self, value, unit):
        self.value = value
        self.unit = unit




class Velocity(Quantity):
    pass


class Area(Quantity):
    pass


class Flow(Quantity):
    @classmethod
    def Define(cls, Vel, Are):
        nResult = Vel.value * Are.value
        uResult = Vel.unit * Are.unit
        return cls(nResult, uResult)

m,s = symbols("m s")

V1 = Velocity(30, m/s)
A1 = Area(14, m**2)
F1 = Flow.Define(V1, A1)
print(F1.value, F1.unit)

v = m * 10
print(type(m))

