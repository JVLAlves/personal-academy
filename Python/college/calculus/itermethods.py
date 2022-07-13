import random
import time
import sympy as symp

symp.init_printing(use_unicode=True)

class Neraph_struct:
    def __init__(self, var:symp.core.symbol.Symbol, eq, diff):
        self.var = var
        self.eq = eq
        self.diff = diff

    def Solve(self, x:float):
        y = float(self.eq.subs(self.var, x))
        y_ = float(self.diff.subs(self.var, x))
        return y, y_


class EquationPack(Neraph_struct):
    def __init__(self, var:symp.core.symbol.Symbol, eq):
        self.id = id
        diff = symp.diff(eq)
        super().__init__(var, eq, diff)



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


def generate_timer(seconds:int):

    def timer():
        x = 0
        while x <= seconds:
            print(x)
            time.sleep(1)
            x+=1

    return timer

# this is a function which represents the Newton Raphson iteration metthod.
def Neraph(func, seed:float, epsilon:float, tolerance:float=0.001, max_iterations:int=100):

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

if __name__ == "__main__":
    coin = GenerateCoinLauncher()
    x = 0
    throws = 100
    CoinClipboard = {"head": 0, "tail": 0}
    while x <=throws :

        side = coin()
        CoinClipboard[side]+= 1
        x+=1

    print(CoinClipboard)

    # x = symp.symbols("x")
    # print(type(x))
    # EqP1 = EquationPack(x, (2*x - 1))
    # eq = create_eq(EqP1.Solve)
    # Neraph(eq, 1, 0.5)


