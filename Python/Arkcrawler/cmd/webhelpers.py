import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import consts


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
    return hrefs

