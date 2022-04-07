from sympy import *
import json
import units

"""
with open('config.json') as f:
    config = json.load(f)
"""


def convertTo(value: float, From: type(symbols("control")), to: type(symbols("control"))):
    # unitEquivalent = config['length'][From.lower()][to.lower()]
    unitEquivalent = units.length[From][to]
    return [(value * unitEquivalent), to]


Km,m = symbols("km m")
print(convertTo(4, m, Km))
