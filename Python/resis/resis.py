from sympy import *
from resis_classes import *
from resis_functions import *

Va, Ha, Vb = symbols("Va Ha Vb")
A = double(0, Va, Ha)
B = simple(10, Vb)
Cy1 = continuous(0, 7, -25)
Py1 = point(3, -50)
Py2 = point(7, -10)
Px1 = point(7, -7)
Cy2 = continuous(7, 3, -50)
Fy = [A.vertical, Cy1.loadValue, Py1.loadValue, Py2.loadValue, Cy2.loadValue, B.vertical]
Fx = [A.horizontal, Px1.loadValue]
Mz = [A.Momentum("vertical", 0), Cy1.Momentum(0), Py1.Momentum(0), Py2.Momentum(0), Cy2.Momentum(0), B.Momentum(0)]

sFy = Forces(Fy)
Ha_value = Forces(Fx)
Vb_value = Momentum(Mz)

Va_value = round(solve(sFy.subs(Vb, Vb_value), Va)[0], 2)

Q, N, M, l = symbols("Q N M l")
qeq = -1 * (+ Va_value + Cy1.continuousLoad * l)
qeq2 = -1 * (+ Va_value + Py1.loadValue + Cy1.continuousLoad * (3 * l))
meq = integrate(qeq)
meq_control = (Va_value * l) + (Cy1.continuousLoad * l * (l / 2))
meq2 = integrate(qeq2)
meq2_control = (Va_value * (-3 * l)) + (Cy1.continuousLoad * (-3 * l) * ((3 * l) / 2)) + (Py1.loadValue * l * -1)
equations = [qeq, meq, meq_control, qeq2, meq2, meq2_control]
for e in enumerate(equations):
    pprint(e)
