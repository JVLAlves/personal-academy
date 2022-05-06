from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
from bs4 import BeautifulSoup
"""
ICON
NAME
TYPE
ARCHETYPE
STATS- BASE, E1 (?), E2 (?)


"""

class operator_cell:
    def __init__(self, op_name, op_url):
        self.name = op_name
        self.url = op_url

class operator:
    def __init__(self, character:dict):
        self.dict = character
        self.name = character["name"]
        self.img = character["img"]
        self.type = character["type"]
        self.archetype = character["archetype"]
        self.status = character["stats"]
        self.skills = character["skills"]

    def 
def status(driver:webdriver):
    status = ["hp", "atk", "def"]

    stats = {}
    for sts in status:
        element = driver.find_element(by=By.XPATH, value=f"//div[@id='stat-{sts}']").text
        if element != '':
            value = int(element)
            stats[f"{sts}"] = value
        else:
            continue

    cost = int(driver.find_element(by=By.XPATH, value="//span[@id='operator-cost']").text)
    stats["dp_cost"] = cost
    return stats

def skill(driver:webdriver):

    # skill clicker XPATH - //li[normalize-space()='Skill 2']
    # SKILL NAME CSS_SELECTOR - div[id='skill-tab-1'] a:nth-child(2)
    # SP COST CSS_SELECTOR - div[id='skill-tab-1'] div[class='sp-cost'] div[class='effect-description skill-upgrade-tab-1 current-tab']
    # DURATION = div[id='skill-tab-1'] div[class='skill-effect-parent'] div[class='effect-description skill-upgrade-tab-1 current-tab']
    # EFFECT - div[id='skill-tab-1'] div[class='skill-description'] div[class='effect-description skill-upgrade-tab-1 current-tab'] (BS4)

    #SKILL 1
    global sp_cost
    skills = {}
    skill = driver.find_element(by=By.CSS_SELECTOR, value="div[id='skill-tab-1'] a:nth-child(2)").text
    skill_name = skill.replace("Skill 1: ", "")
    element = driver.find_element(by=By.CSS_SELECTOR, value="div[id='skill-tab-1'] div[class='sp-cost'] div[class='effect-description skill-upgrade-tab-1 current-tab']").text
    if element != '':
        sp_cost = int(element)
    element = driver.find_element(by=By.CSS_SELECTOR, value="div[id='skill-tab-1'] div[class='skill-effect-parent'] div[class='effect-description skill-upgrade-tab-1 current-tab']").text
    time = element.replace(" Seconds", "")
    if time == "-":
        duration = None
    else:
        duration = int(time)

    skill_effect = driver.find_element(by=By.CSS_SELECTOR, value="div[id='skill-tab-1'] div[class='skill-description'] div[class='effect-description skill-upgrade-tab-1 current-tab']")
    imgHTML = skill_effect.get_attribute("innerHTML")
    stew = BeautifulSoup(imgHTML, "html.parser")
    effect = stew.get_text()
    skills[skill_name] = {"sp_cost":sp_cost, "duration":duration, "effect":effect}


    # SKILL 2
    try:
        skill_two = driver.find_element(by=By.XPATH, value="//li[normalize-space()='Skill 2']")
        driver.execute_script("arguments[0].click();", skill_two)
    except:
        return skills
    else:
        skill = driver.find_element(by=By.CSS_SELECTOR, value="div[id='skill-tab-2'] a:nth-child(2)").text
        skill_name = skill.replace("Skill 2: ", "")
        element = driver.find_element(by=By.CSS_SELECTOR, value="div[id='skill-tab-2'] div[class='sp-cost'] div[class='effect-description skill-upgrade-tab-1 current-tab']").text
        if element != '':
            sp_cost = int(element)
        element = driver.find_element(by=By.CSS_SELECTOR,
                                      value="div[id='skill-tab-2'] div[class='skill-effect-parent'] div[class='effect-description skill-upgrade-tab-1 current-tab']").text
        time = element.replace(" Seconds", "")
        if time == "-":
            duration = None
        else:
            duration = int(time)

        skill_effect = driver.find_element(by=By.CSS_SELECTOR, value="div[id='skill-tab-2'] div[class='skill-description'] div[class='effect-description skill-upgrade-tab-1 current-tab']")
        imgHTML = skill_effect.get_attribute("innerHTML")
        stew = BeautifulSoup(imgHTML, "html.parser")
        effect = stew.get_text()
        skills[skill_name] = {"sp_cost": sp_cost, "duration": duration, "effect": effect}


    # SKILL 3
    try:
        skill_two = driver.find_element(by=By.XPATH, value="//li[normalize-space()='Skill 3']")
        driver.execute_script("arguments[0].click();", skill_two)
    except:
        return skills
    else:
        skill = driver.find_element(by=By.CSS_SELECTOR, value="div[id='skill-tab-3'] a:nth-child(2)").text
        skill_name = skill.replace("Skill 3: ", "")
        element = driver.find_element(by=By.CSS_SELECTOR,
                                      value="div[id='skill-tab-3'] div[class='sp-cost'] div[class='effect-description skill-upgrade-tab-1 current-tab']").text
        if element != '':
            sp_cost = int(element)
        element = driver.find_element(by=By.CSS_SELECTOR,
                                      value="div[id='skill-tab-3'] div[class='skill-effect-parent'] div[class='effect-description skill-upgrade-tab-1 current-tab']").text
        time = element.replace(" Seconds", "")
        if time == "-":
            duration = None
        else:
            duration = int(time)

        skill_effect = driver.find_element(by=By.CSS_SELECTOR,
                                           value="div[id='skill-tab-3'] div[class='skill-description'] div[class='effect-description skill-upgrade-tab-1 current-tab']")
        imgHTML = skill_effect.get_attribute("innerHTML")
        stew = BeautifulSoup(imgHTML, "html.parser")
        effect = stew.get_text()
        skills[skill_name] = {"sp_cost": sp_cost, "duration": duration, "effect": effect}

    return skills


def kaltsit(url:str, headless:bool=True):

    character = {}

    option = Options()
    option.headless = headless
    service = ChromeService(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=option)

    # Get the page through the driver
    driver.get(url)
    time.sleep(2)
    name = driver.find_element(by=By.CSS_SELECTOR, value="div[id='page-title'] h1").text
    character["name"] = name
    img = driver.find_element(by=By.XPATH, value="//div[@id='image-tab-1']//a//img").get_attribute("src")
    character["img"] = img
    type = driver.find_element(by=By.CSS_SELECTOR, value="div[class='profession-cell-inner'] div[class='profession-title']").text
    character["type"] = type
    archetype = driver.find_element(by=By.CSS_SELECTOR, value="div[class='profession-cell-inner subprofession-cell'] div[class='profession-title']").text
    character["archetype"] = archetype

    #BASE_STATUS

    base_stats = status(driver)

    #ELITE 1

    try:
        element = driver.find_element(by=By.CSS_SELECTOR, value=f".rank-button[data-tab='e1']")
        if element is None or element == '':
            raise Exception
    except:
        e1_stats = None
    else:
        driver.execute_script("arguments[0].click();", element)

        e1_stats = status(driver)


    #ELITE 2

    try:
        element = driver.find_element(by=By.CSS_SELECTOR, value=f".rank-button[data-tab='e2']")
        if element is None or element == '':
            raise Exception
    except:
        e2_stats = None
    else:
        driver.execute_script("arguments[0].click();", element)

        e2_stats = status(driver)


    character["stats"] = { "base": base_stats, "elite_one": e1_stats, "elite_two": e2_stats}
    character["skills"] = skill(driver)

    return character






def search(url:str="https://gamepress.gg/arknights/tools/interactive-operator-list#tags=null##", show:str="stats", headless=False, max_searches:int = 10):
    show_options = ["stats", "traits", "skills", "talents", "evaluation", "atags", "obtain","modules"]
    show = show.lower()
    if show not in show_options:
        raise ValueError
    url = url + show
    option = Options()
    option.headless = headless
    service = ChromeService(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=option)

    # Get the page through the driver
    driver.get(url)
    time.sleep(2)

    # Get the operators data table
    tbbody = driver.find_element(by=By.CSS_SELECTOR, value="#operators-list")
    print(f"Found {tbbody}")
    cells = tbbody.find_elements(by=By.CSS_SELECTOR, value=".operators-row")
    print(f"Found {cells}")

    #new list of operators data table
    operator_available = []

    for cell in cells:
        display = cell.get_attribute("style")
        if display == "display: none;":
            continue
        op_name = cell.get_attribute("data-name")
        try:
            op_url = cell.find_element(by=By.XPATH, value=f"//a[normalize-space()='{op_name}']").get_attribute("href")
        except:
            continue
        op = operator_cell(op_name, op_url)
        operator_available.append(op)


    operators = []

    count = 0

    for op in operator_available:
        if count > max_searches:
            break
        oper = kaltsit(op.url)
        operators.append(operator(oper))
        count+=1
    return operators



    #click on status button to start searching

if __name__ == "__main__":
    search()