import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from app.Arkcrawler.cmd import consts
import logging


def getlatestnews(link):

    option = Options()
    option.headless = True
    service = ChromeService(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=option)
    driver.get(link + "/news")
    time.sleep(5)

    if consts.GET_LATESTS:
        driver.find_element(by="xpath", value="//ul[@class='news-tag-ul']/li[1]").click()
        time.sleep(1.5)
    elif consts.GET_EVENTS:
        driver.find_element(by="xpath", value="//ul[@class='news-tag-ul']/li[2]").click()
        time.sleep(1.5)

    hrefs = []

    if consts.GET_ALL:

        elements = driver.find_elements(by="xpath", value=consts.NEWS_BOX_XPATH)
        for e in elements:
            news_box = e.get_attribute("outerHTML")
            soup = BeautifulSoup(news_box, 'html.parser')
            tag = soup.find(name="a")
            href = tag['href']
            hrefs.append(href)

    else:
        element = driver.find_element(by="xpath", value=consts.NEWS_BOX_XPATH)
        news_box = element.get_attribute("outerHTML")
        soup = BeautifulSoup(news_box, 'html.parser')
        tag = soup.find(name="a")
        href = tag['href']
        hrefs.append(href)

    driver.quit()
    logging.info(f"NEWS HREFS: {hrefs}")
    return hrefs


def getContent(link):
    option = Options()
    option.headless = True
    seconservice = ChromeService(executable_path=ChromeDriverManager().install())
    secondriver = webdriver.Chrome(service=seconservice, options=option)
    secondriver.get(link)
    time.sleep(3)
    news_body = secondriver.find_element(by="css selector", value=".news-detail-content")
    paragraphs = news_body.find_elements(by="tag name", value="p")

    textcontent = []
    imagesurllist = []

    for p in paragraphs:
        para = p.text
        if consts.DEBUGMODE:
            logging.debug(f'{paragraphs.index(p)} {para}')

        textcontent.append(para)

    images = news_body.find_elements(by="tag name", value='img')

    for img in images:
        imgHTML = img.get_attribute("outerHTML")
        stew = BeautifulSoup(imgHTML, "html.parser")
        imgmkup = stew.find(name="img")
        src = imgmkup['src']
        if consts.DEBUGMODE:
            logging.debug(f'IMAGE SRC DETECTED {src}')
        imagesurllist.append(src)

    secondriver.quit()
    n = 0
    for txt in textcontent:
        if consts.DEBUGMODE:
            logging.debug(f'TEXT LINE {textcontent.index(txt)}: {txt}')
        if txt == '' or txt == " ":

            continue
        else:
            n = textcontent.index(txt)
            break

    title = textcontent[n].replace(" ", "_")
    filename = title + ".txt"
    splittedTitle = textcontent[n].split(" ")
    if consts.DEBUGMODE:
        logging.debug(f'NEWS TITLE: {textcontent[n]}\n NEWS TITLE STRUCTURE: {splittedTitle}')
    try:
        splittedTitle.index("Contest")
    except:
        try:
            splittedTitle.index("EVENT")
        except:
            try:
                splittedTitle.index("STORY")
            except:
                try:
                    splittedTitle.index("STORY:")
                except:
                    path = consts.DIR_PATH + "/etc/" + filename
                else:
                    title = title.replace(":", "")
                    filename = title + ".txt"
                    path = consts.DIR_PATH + "/events/" + filename
            else:
                path = consts.DIR_PATH + "/events/" + filename
        else:
            path = consts.DIR_PATH + "/events/" + filename
    else:
        path = consts.DIR_PATH + "/contest/" + filename


    newsDict = {
        "title": title,
        "path": path,
        "paragraphs": textcontent,
        "srcs": imagesurllist,
        "name": textcontent[n]
    }
    logging.info(f"NEW OBJECT\n NAME: {newsDict['name']}\n FILE TITLE: {newsDict['title']}\n FILE PATH: {newsDict['path']}",)

    return newsDict
