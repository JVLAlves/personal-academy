import time
#import requests
#import pandas as pd
#from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
#import json

url = "https://www.arknights.global/news"

option = Options()
option.headless = True
driver = webdriver.Firefox()

driver.get(url)
time.sleep(10)

res = driver.find_element(by='class_name', value='news-box-wrap')
print(res)


driver.quit()



