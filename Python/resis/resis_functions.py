import sympy
import resis_classes as rclasses


def Forces(Fx: list):
    sumofall = 0
    varCount = 0
    var = ""
    for n in Fx:
        if isinstance(n, type(sympy.symbols("CONTROL"))) or isinstance(n, type((sympy.symbols(
                "TIMES") * 10))) or isinstance(n, type((sympy.symbols("DIVISION") / 10))):
            varCount += 1
            var = n
        sumofall += n
    if varCount <= 0:
        return
    elif varCount > 1:
        return sumofall
    else:
        sympy.pprint(sumofall)
        equation = sympy.Eq(sumofall, 0)
        ans = round(sympy.solve(equation, var)[0], 2)
        print(f'{var} = {ans}')
        return ans


def Momentum(Loads: list):
    sumofall = 0
    varCount = 0
    var = ""
    for n in Loads:
        if isinstance(n, list):
            varCount += 1
            var = n[1]
            sumofall += n[0]
            continue
        sumofall += n
    if varCount <= 0:
        return
    elif varCount > 1:
        return sumofall
    else:
        sympy.pprint(sumofall)
        equation = sympy.Eq(sumofall, 0)
        ans = round(sympy.solve(equation, var)[0], 2)
        print(f'{var} = {ans}')
        return ans
