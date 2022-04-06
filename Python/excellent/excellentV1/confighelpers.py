from configparser import ConfigParser
FILE = 'config.ini'

def init():
    config = ConfigParser()
    config.read(FILE)
    return config