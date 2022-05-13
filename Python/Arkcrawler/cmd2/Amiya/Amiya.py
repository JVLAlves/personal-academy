#this module handles the search of the
#TODO:Connection with Database (future feature)
import datetime
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import PySimpleGUI as sg
import cloudscraper
from PIL import Image
import io
import webbrowser
import cmd2.originum as ori
import Kaltsit.arknomicon as ark

location = {
    "HP": {By.XPATH: "//div[@id='stat-hp']", By.CSS_SELECTOR:"#stat-hp",},
    "ATK": {By.XPATH: "//div[@id='stat-atk']", By.CSS_SELECTOR:"#stat-atk",},
    "DEF": {By.XPATH: "//div[@id='stat-def']", By.CSS_SELECTOR:"#stat-def",},
    "RES": {By.XPATH: "//span[@id='arts-resist']", By.CSS_SELECTOR:"#arts-resist",},
    "DP COST": {By.XPATH: "//span[@id='operator-cost']", By.CSS_SELECTOR:"#operator-cost",},
    "BLOCK": {By.XPATH: "//span[@id='operator-block']", By.CSS_SELECTOR:"#operator-block",}
}

class Operator:
    def __init__(self, character_dictionary:dict):
        self.codename = character_dictionary["name"]
        self.S = character_dictionary["elite"]
        self.level = character_dictionary["level"]
        self.HP = character_dictionary["HP"]
        self.ATK = character_dictionary["ATK"]
        self.DEF = character_dictionary["DEF"]
        self.RES = character_dictionary["RES"]
        self.DP_COST = character_dictionary["DP COST"]
        self.BLOCK = character_dictionary["BLOCK"]
        self.url = character_dictionary["url"]
        self.img = character_dictionary["img"]

class Kaltsit_Operator:
    def __init__(self, character_dictionary: dict):
        self.name = character_dictionary["name"]
        self.img = character_dictionary["img"]
        self.type = character_dictionary["type"]
        self.archetype = character_dictionary["archetype"]
        self.status = character_dictionary["stats"]
        self.skills = character_dictionary["skills"]

def liskcraw(operator:str, elite:int=0, max_level:bool=True, default_level:int=1, link="https://www.gamepress.gg/arknights/operator/", head=True):
    character_status = {"name": operator.capitalize()}
    # Dynamically install and set up a Google Chrome web driver for Selenium
    operator.lower()
    if operator.find(" the ") != -1:
        operator = operator.replace(" the ", " ")
    if operator.find(" ") != -1:
        operator = operator.replace(" ", "-")
    if operator.find("'") != -1:
        operator = operator.replace("'", '')

    url = link + operator.lower()
    option = Options()
    option.headless = head
    service = ChromeService(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=option)

    # Get the page through the driver
    driver.get(url)
    time.sleep(2)

    # click on status button to start searching
    # access different elite stages depending on search
    character_status["elite"] = elite
    if elite != 0:
        if elite > 2 or elite < 0:
            raise Exception("This Elite level doesn't exists")
        element = driver.find_element(by=By.CSS_SELECTOR, value=f".rank-button[data-tab='e{elite}']")
        driver.execute_script("arguments[0].click();", element)
    # rowling the level ahead till max
    if max_level:
        c = 0
        while True:
            if c > 1000:
                exit()
            old_level = driver.find_element(by=By.XPATH, value="//span[@id='level-value']").text
            if old_level == '':
                old_level = 0
            else:
                old_level = int(old_level)
            element = driver.find_element(by=By.CSS_SELECTOR, value=".fa.fa-arrow-right")
            driver.execute_script("arguments[0].click();", element)
            new_level = int(driver.find_element(by=By.XPATH, value="//span[@id='level-value']").text)
            if old_level == new_level:
                character_status["level"] = new_level
                break
            c+= 1
    else:
        while True:
            new_level = int(driver.find_element(by=By.CSS_SELECTOR, value="#level-value").text)
            if new_level == default_level:
                character_status["level"] = new_level
                break
            element = driver.find_element(by=By.CSS_SELECTOR, value=".fa.fa-arrow-right")
            driver.execute_script("arguments[0].click();", element)


    # getting attack status

    method = By.XPATH
    for key, value in location.items():
        element = driver.find_element(by=method, value=value[method])
        text= element.text
        character_status[key] = float(text)

    # getting image src
    element = driver.find_element(by=By.XPATH, value="//div[@id='image-tab-1']//a//img")
    img = element.get_attribute("src")
    character_status["img"] = img


    # Last thing to do is append the url to the character dictionary
    character_status["url"] = url
    return character_status

class Operator_window:
    def __init__(self, operator:Operator):
        self.operator = operator
        jpg_data = (
            cloudscraper.create_scraper(
                browser={"browser": "firefox", "platform": "windows", "mobile": False}
            ).get(operator.img).content)

        basewidth = 600
        pil_image = Image.open(io.BytesIO(jpg_data))
        wpercent = (basewidth/float(pil_image.size[0]))
        hsize = int(float(pil_image.size[1])*float(wpercent))
        pil_image = pil_image.resize((basewidth, hsize), Image.ANTIALIAS)
        png_bio = io.BytesIO()
        pil_image.save(png_bio, format="PNG")
        png_data = png_bio.getvalue()

        layout=[
            [sg.VPush(), sg.Push(), sg.Text(operator.codename.upper(), font="Arial 16 bold"), sg.Push()],
            [sg.VPush(), sg.Push(), sg.Image(data=png_data, ), sg.Push(), sg.VPush()],
            [sg.VPush(), sg.Text("OPERATOR STATUS", font="Arial 16 bold")],
            [sg.Text(f"Lvl. {operator.level}", font="Arial 14")],
            [sg.Text(f"Elite {operator.elite_level}", font="Arial 14")],
            [sg.Text(f"HP: {operator.HP}", font="Arial 14")],
            [sg.Text(f"ATK: {operator.ATK}", font="Arial 14")],
            [sg.Text(f"DEF: {operator.DEF}", font="Arial 14")],
            [sg.Text(f"RES: {operator.RES}", font="Arial 14")],
            [sg.Text(f"DP Cost: {operator.DP_COST}", font="Arial 14")],
            [sg.Text(f"Block: {operator.BLOCK} {'enemy' if operator.BLOCK == 1 else 'enemies'}", font="Arial 14")],
            [sg.VPush(), sg.Button("see on page", key ="-see-"), sg.VPush()]
        ]
        self.window = sg.Window(f"Operator: {operator.codename}", icon="Amiya/Operator.png").layout(layout).finalize()
        self.window.bind("<Key-Escape>", "esc")

    def init(self):
        while True:
            event, _ = self.window.Read()
            if event == sg.WIN_CLOSED or event == "esc":
                break
            elif event == "-see-":
                webbrowser.open(self.operator.url)
        self.window.close()

def search_operator(operator_name:str):
    today_moment = datetime.datetime.today()
    today_str = today_moment.strftime("%Y-%m-%dT%H:%M")
    config = ori.Config()
    amiya = config["amiya"]

    if eval(amiya["database"]):
        operator_data = ark.get_operator(operator_name)
        print(operator_data)
        if operator_data is None:
            operator_data = liskcraw(operator_name)
            ark.insert_operator(operator_data)
    else:
        operator_data = liskcraw(operator_name)

    amiya["last_operator_seen"] = operator_data["name"]
    amiya["last_time_run"] = today_str
    with open(ori.CONFIG_FILE, "w") as ConfigFile:
        config.write(ConfigFile)
    return operator_data
