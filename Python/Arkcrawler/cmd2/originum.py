#this is the module which handles the Crawling part
#TODO: Handle multiple searches (Fresh News)
import logging
import os
import time
from configparser import ConfigParser

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

CONFIG_FILE = 'config.ini'


def Config():
    if not os.path.exists(CONFIG_FILE):
        open(CONFIG_FILE, "x")

    config = ConfigParser()
    config.read(CONFIG_FILE)
    return config

def Config_init():
    #get config variable, then the sections to compare with default sections (secs)
    config = Config()
    sections = config.sections()
    secs = ["liskarm", "amiya", "kaltsit"]

    #in case the sections already exists, there is no point to remake it so passes it.
    if sections == secs:
        pass
    else:
        #in case there are some of the sections missing, analyses and creates the missing one.
        if len(sections) != len(secs) and len(sections) > 0:
            for s in sections:
                if s not in secs:
                    config.add_section(s)
        elif len(sections) == 0:
            for s in secs:
                config.add_section(s)

    #LISKARM - the Crawler
    liskarm = list(config["liskarm"].keys())
    liskarm_elements = {"automation": "False", "interface_call":"False", "news_type":"None", "news_category":"None", "latest": "None", "last_time_run": "None", "last_google_event_created":"None"}

    #AMIYA - the Operator searcher
    amiya = config["amiya"]
    amiya_elements = {"database":"False", "last_time_run":"None", "last_operator_seen":"None"}

    #KAL'TSIT - the API to Operators Database
    kaltsit = config["kaltsit"]
    kaltsit_elements = {"database_link":"mongodb+srv://joao:sdl170502@kaltsit.gyy0s.mongodb.net/test", "last_time_run":"None"}

    #The same logic for the sections are applied to the elements from sections (liskarm, amiya and kaltsit)
    print(f"LISKARM ({len(liskarm)}): {liskarm}")
    if len(liskarm) != len(liskarm_elements):
        print(liskarm)
        for eKeys in liskarm_elements.keys():
            if eKeys not in list(liskarm):
                config.set("liskarm", eKeys, liskarm_elements[eKeys])
    else:
        pass

    if len(amiya) != len(amiya_elements):
        print(list(amiya))
        for eKeys in amiya_elements.keys():
            if eKeys not in list(amiya):
                config.set("amiya", eKeys, amiya_elements[eKeys])
    else:
        pass

    if len(kaltsit) != len(kaltsit_elements):
        print(list(kaltsit))
        for eKeys in kaltsit_elements.keys():
            if eKeys not in list(kaltsit):
                config.set("kaltsit", eKeys, kaltsit_elements[eKeys])
    else:
        pass

    #write the information the Config file
    with open(CONFIG_FILE, "w") as ConfigFile:
        config.write(ConfigFile)

def Search(type:str, category:str, link:str= "https://www.arknights.global", headless:bool=True):
    option = Options()
    option.headless = headless
    service = ChromeService(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=option)
    driver.get(link + "/news")
    time.sleep(10)
    if category == 'all':
        driver.find_element(by=By.XPATH, value="//li[normalize-space()='LATEST']").click()
        time.sleep(1.5)
        time.sleep(10)

    elif category == 'event':
        driver.find_element(by=By.XPATH, value="//li[normalize-space()='EVENT']").click()
        time.sleep(1.5)
        time.sleep(10)
    elif category == 'contest':
        driver.find_element(by=By.XPATH, value="//li[@class='news-tag-li active']")
        time.sleep(1.5)
        time.sleep(10)

    hrefs = []
    if type == "latest":
        element = driver.find_element(by=By.CSS_SELECTOR, value='.news-box')
        news_box = element.get_attribute("outerHTML")
        soup = BeautifulSoup(news_box, 'html.parser')
        tag = soup.find(name="a")
        href = tag['href']
        hrefs.append(href)
    elif type == "nines":
        elements = driver.find_elements(by=By.CSS_SELECTOR, value=".news-box")

        for e in elements:
            news_box = e.get_attribute("outerHTML")
            soup = BeautifulSoup(news_box, 'html.parser')
            tag = soup.find(name="a")
            href = tag['href']
            hrefs.append(href)

    driver.quit()
    return hrefs

def Focus(href:str, link:str="https://www.arknights.global", head:bool=True):
    logging.info(f"Focusing in... {href}")
    option = Options()
    option.headless = head
    seconservice = ChromeService(executable_path=ChromeDriverManager().install())
    secondriver = webdriver.Chrome(service=seconservice, options=option)
    secondriver.get(link + href)
    time.sleep(3)
    news_body = secondriver.find_element(by=By.XPATH, value="//div[@class='news-detail-content']")
    paragraphs = news_body.find_elements(by=By.TAG_NAME, value="p")

    textcontent = []
    imagesurllist = []

    for p in paragraphs:
        para = p.text

        ind = repr(para).find(r"\n")
        if repr(para).find(r"\n") != -1:
            paras = para.splitlines()
            for parag in paras:
                textcontent.append(parag)
            continue
        textcontent.append(para)

    images = news_body.find_elements(by="tag name", value='img')

    for img in images:
        imgHTML = img.get_attribute("outerHTML")
        stew = BeautifulSoup(imgHTML, "html.parser")
        imgmkup = stew.find(name="img")
        src = imgmkup['src']
        imagesurllist.append(src)


    return textcontent, link + href


