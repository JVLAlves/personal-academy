#this is the module which handles the Crawling part
#TODO: Handle multiple searches (Fresh News)
import logging
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

def Search(number:str, type:str, link:str="https://www.arknights.global", head:bool=True):
    option = Options()
    option.headless = head
    service = ChromeService(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=option)
    driver.get(link + "/news")
    time.sleep(10)
    if type == 'all':
        driver.find_element(by=By.XPATH, value="//li[normalize-space()='LATEST']").click()
        time.sleep(1.5)
        time.sleep(10)

    elif type == 'event':
        driver.find_element(by=By.XPATH, value="//li[normalize-space()='EVENT']").click()
        time.sleep(1.5)
        time.sleep(10)
    elif type == 'contest':
        driver.find_element(by=By.XPATH, value="//li[@class='news-tag-li active']")
        time.sleep(1.5)
        time.sleep(10)

    hrefs = []
    if number == "latest":
        element = driver.find_element(by=By.CSS_SELECTOR, value='.news-box')
        news_box = element.get_attribute("outerHTML")
        soup = BeautifulSoup(news_box, 'html.parser')
        tag = soup.find(name="a")
        href = tag['href']
        hrefs.append(href)
    elif number == "nines":
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


