import logging
import time

from app.Arkcrawler.cmd import filehelpers
from app.Arkcrawler.cmd import webhelpers
from app.Arkcrawler.cmd import logs
from app.Arkcrawler.cmd import consts

files = []
dictAllNews = {}
url = "https://www.arknights.global"

def getLatestNews():
    #Consts Reassignment
    consts.GET_LATESTS = True

    filehelpers.init()
    time.sleep(5)
    logs.init()
    time.sleep(5)
    news_numbers = webhelpers.getlatestnews(url)

    for num in news_numbers:
        news_url = url + num
        news = webhelpers.getContent(news_url)
        files.append(news["path"])
        dictAllNews.update({news["path"]: news})

    alreadyExists, fileQueue = filehelpers.verifyExistentFiles(files)

    if not alreadyExists:
        for file in fileQueue:
            filehelpers.writedown(file, dictAllNews[file]["paragraphs"], dictAllNews[file]["srcs"])
    else:
        logging.info(f"There is nothing to see here.")

    def getLatestNews():
        # Consts Reassignment
        consts.GET_LATESTS = True

        filehelpers.init()
        time.sleep(5)
        logs.init()
        time.sleep(5)
        news_numbers = webhelpers.getlatestnews(url)

        for num in news_numbers:
            news_url = url + num
            news = webhelpers.getContent(news_url)
            files.append(news["path"])
            dictAllNews.update({news["path"]: news})

        alreadyExists, fileQueue = filehelpers.verifyExistentFiles(files)

        if not alreadyExists:
            for file in fileQueue:
                filehelpers.writedown(file, dictAllNews[file]["paragraphs"], dictAllNews[file]["srcs"])
        else:
            logging.info(f"There is nothing to see here.")

def getEventNews():
    #Consts Reassignment
    consts.GET_EVENTS = True

    filehelpers.init()
    time.sleep(5)
    logs.init()
    time.sleep(5)
    news_numbers = webhelpers.getlatestnews(url)

    for num in news_numbers:
        news_url = url + num
        news = webhelpers.getContent(news_url)
        files.append(news["path"])
        dictAllNews.update({news["path"]: news})

    alreadyExists, fileQueue = filehelpers.verifyExistentFiles(files)

    if not alreadyExists:
        for file in fileQueue:
            filehelpers.writedown(file, dictAllNews[file]["paragraphs"], dictAllNews[file]["srcs"])
    else:
        logging.info(f"There is nothing to see here.")

def getContestNews():
    #Consts Reassignment
    consts.GET_CONTESTS = True

    filehelpers.init()
    time.sleep(5)
    logs.init()
    time.sleep(5)
    news_numbers = webhelpers.getlatestnews(url)

    for num in news_numbers:
        news_url = url + num
        news = webhelpers.getContent(news_url)
        files.append(news["path"])
        dictAllNews.update({news["path"]: news})

    alreadyExists, fileQueue = filehelpers.verifyExistentFiles(files)

    if not alreadyExists:
        for file in fileQueue:
            filehelpers.writedown(file, dictAllNews[file]["paragraphs"], dictAllNews[file]["srcs"])
    else:
        logging.info(f"There is nothing to see here.")