import logging as log
import os

from app.Arkcrawler.cmd import consts
from datetime import date


def init():
    filename = consts.DIR_PATH + "/logs/" + str(date.today()) + ".log"
    isExists = os.path.exists(filename)
    if isExists:
        log.basicConfig(filename=filename, filemode='a', encoding='utf-8', level=log.INFO)
    else:
        log.basicConfig(filename=filename, filemode='w', encoding='utf-8', level=log.INFO)
