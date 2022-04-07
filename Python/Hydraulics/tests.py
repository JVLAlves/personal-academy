from sympy import *
from configparser import ConfigParser
file = 'units.ini'
config = ConfigParser()
config.read(file)
print(config.sections())
print(config['length']['km'])
