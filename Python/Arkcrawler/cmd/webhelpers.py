import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import consts
import logging


def getlatestnews(link):

    option = Options()
    option.headless = False
    service = ChromeService(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=option)
    driver.get(link + "/news")
    time.sleep(10)

    if consts.GET_LATESTS:
        driver.find_element(by="css selector", value=".news-tag-li").click()
        time.sleep(1.5)
        driver.refresh()
    elif consts.GET_EVENTS:
        driver.find_element(by="link text", value="EVENT").click()
        time.sleep(1.5)
        driver.refresh()
        time.sleep(10)

    hrefs = []

    if consts.GET_ALL:

        elements = driver.find_elements(by="css selector", value=".news-box")

        for e in elements:
            news_box = e.get_attribute("outerHTML")
            soup = BeautifulSoup(news_box, 'html.parser')
            tag = soup.find(name="a")
            href = tag['href']
            hrefs.append(href)

    else:
        element = driver.find_element(by="css selector", value='.news-box')
        news_box = element.get_attribute("outerHTML")
        soup = BeautifulSoup(news_box, 'html.parser')
        tag = soup.find(name="a")
        href = tag['href']
        hrefs.append(href)

    driver.quit()
    logging.debug(hrefs)
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

        textcontent.append(para)

    images = news_body.find_elements(by="tag name", value='img')

    for img in images:
        imgHTML = img.get_attribute("outerHTML")
        stew = BeautifulSoup(imgHTML, "html.parser")
        imgmkup = stew.find(name="img")
        src = imgmkup['src']
        imagesurllist.append(src)

    secondriver.quit()

    title = textcontent[0].replace(" ", "_")
    filename = title + ".txt"
    path = ""
    splittedTitle = textcontent[0].split(" ")

    print(splittedTitle)

    try:
        splittedTitle.index("Contest")
    except:
        try:
            splittedTitle.index("Event")
        except:
            path = consts.DIR_PATH + "/etc/" + filename
        else:
            path = consts.DIR_PATH + "/event/" + filename
    else:
        path = consts.DIR_PATH + "/contest/" + filename


    newsDict = {
        "title": title,
        "path": path,
        "paragraphs": textcontent,
        "srcs": imagesurllist
    }

    return newsDict
