import time
import re
import requests
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

# import json

url = "https://www.arknights.global"


def GetLatestNews(link):
    option = Options()
    option.headless = True
    service = ChromeService(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=option)
    driver.get(link + "/news")
    time.sleep(3)
    element = driver.find_element(by="class name", value="news-box")
    news_box = element.get_attribute("outerHTML")
    soup = BeautifulSoup(news_box, 'html.parser')
    tag = soup.find(name="a")
    href = tag['href']
    driver.quit()

    news_link = link + href
    return news_link


def TranscriptNews(link):
    option = Options()
    option.headless = True
    service = ChromeService(executable_path=ChromeDriverManager().install())
    secondriver = webdriver.Chrome(service=service, options=option)
    secondriver.get(link)
    time.sleep(3)
    news_body = secondriver.find_element(by="class name", value="news-detail-content")
    paragraphs = news_body.find_elements(by="tag name", value="p")
    textinformation = []
    for p in paragraphs:
        para = p.text
        textinformation.append(para)

    images = news_body.find_elements(by="tag name", value='img')
    imagesurllist = []
    for img in images:
        imgHTML = img.get_attribute("outerHTML")
        stew = BeautifulSoup(imgHTML, "html.parser")
        imgmkup = stew.find(name="img")
        src = imgmkup['src']
        imagesurllist.append(src)

    secondriver.quit()

    return textinformation, imagesurllist


news_url = GetLatestNews(url)
infos, imgs = TranscriptNews(news_url)

for txt in infos:
    print(txt)

for img in imgs:
    print(img)
