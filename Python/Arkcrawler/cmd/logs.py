import logging
import logging as log
import consts
from datetime import date


def init():

    filename = consts.DIR_PATH + "/logs/" + str(date.today()) + ".log"
    log.basicConfig(filename=filename, filemode='a', encoding='utf-8', level=logging.DEBUG)