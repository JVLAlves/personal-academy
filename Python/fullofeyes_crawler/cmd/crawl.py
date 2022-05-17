import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from translate import Translator
from biblepaths import bible, toBooks, Passage, Image
import re


def Search(book: str, link: str = "https://www.fullofeyes.com/resources/search-art-by-scripture/", head: bool = True):
    option = Options()
    option.headless = head
    service = ChromeService(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=option)
    driver.get(link)
    time.sleep(5)

    books_paragraph = driver.find_element(by=By.XPATH, value="//p[2]")
    try:
        if book == "Psalm":
            book = "Psalms"
        book_ref = books_paragraph.find_element(by=bible[book]["method"], value=bible[book]["path"])
    except:
        return None
    else:
        return book_ref.get_attribute("href")


def Analyse(href: str, head: bool = True):
    option = Options()
    option.headless = head
    service = ChromeService(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=option)
    driver.get(href)
    time.sleep(5)

    thumbs = driver.find_elements(by=By.CSS_SELECTOR, value="div.project.small")
    verses_of_images = []
    images_of_verses = []
    for thumb in thumbs:
        anchor = thumb.find_element(by=By.CSS_SELECTOR, value="div.inside > a")
        link = anchor.get_attribute("href")
        element_img = anchor.find_element(by=By.TAG_NAME, value="img")
        img_src = element_img.get_attribute("src")
        dimensions = [element_img.get_attribute("width"), element_img.get_attribute("height")]
        images_of_verses.append(Image(link, img_src, dimensions))

        element_span = anchor.find_element(by=By.CSS_SELECTOR, value="span.title")
        title = element_span.get_attribute("outerHTML")
        soup = BeautifulSoup(title, 'html.parser')

        tag = soup.find(name="span")
        span = tag.contents[0]
        if len(span) == 0:
            continue
        else:
            verse = span.contents[0]

        verses_of_images.append(verse)

    verses_and_images = []
    for index, verses in enumerate(verses_of_images):
        verses_and_images.append(([verses, images_of_verses[index]]))

    pattern = re.compile("(([^\W\d_]+)\s(\d{1,3}):(\d{1,3})-(\d{1,3})|([^\W\d_]+)\s(\d{1,3}):(\d{1,3}))")
    toExclude = []
    for vm in verses_and_images:
        if not re.match(pattern, vm[0]):
            print(f"{vm[0]} Doesnt fit the pattern.")
            toExclude.append(vm)

    for ex in toExclude:
        verses_and_images.remove(ex)

    object_verses = []
    for vm in verses_and_images:
        pattern = re.compile("([^\W\d_]+)\s(\d{1,3}):(\d{1,3}-\d{1,3}|\d{1,3})")
        agroupment = re.findall(pattern, vm[0])
        object_verses.append(Passage(agroupment[0][0], agroupment[0][1], agroupment[0][2], img=vm[1]))

    for ob in object_verses:
        print("Showing Objects: ", ob.show())
    return object_verses


#######################################################################
"""
TODO: Reformulate to be receive an object list already
"""


def compare(ref: object, available: list):
    single_verses = []
    single_pattern = re.compile("^([^\W\d_]+)\s(\d{1,3}):(\d{1,3})$")
    composed_verse = []
    composed_pattern = re.compile("^([^\W\d_]+)\s(\d{1,3}):(\d{1,3})-(\d{1,3})$")

    for index, verse in enumerate(available):
        print("Comparing", verse.show())

        if single_pattern.match(verse.show()):
            print(f"{verse.show()} is a Single Verse")
            single_verses.append(verse)
        elif composed_pattern.match(verse.show()):
            print(f"{verse.show()} is a Composed Verse")
            composed_verse.append(verse)

    object_verses = []
    for sv in single_verses:
        if re.match(single_pattern, sv.show()):
            object_verses.append(sv)

    for cv in composed_verse:
        if re.match(composed_pattern, cv.show()):
            object_verses.append(cv)

    closest = []
    history = []
    print(ref.book, ref.chapter, ref.verses)
    if ref.book is not None and ref.chapter is not None and ref.verses is not None:
        for obj in object_verses:
            if obj.book == ref.book and obj.chapter == ref.chapter and obj.verses == ref.verses:
                if obj.book.lower() == "psalm":
                    obj.book = "psalms"
                else:
                    obj.book = obj.book.lower()
                return True, obj
            elif obj.book == ref.book and obj.chapter == ref.chapter:
                if obj.book.lower() == "psalm":
                    obj.book = "psalms"
                else:
                    obj.book = obj.book.lower()
                if obj.show() in history:
                    obj.setName(f"V{history.count(obj.show())+1}")
                closest.append(obj)
                history.append(obj.show())
    elif ref.book is not None and ref.chapter is not None and ref.verses is None:
        for obj in object_verses:
            if obj.book == ref.book and obj.chapter == ref.chapter:
                if obj.book.lower() == "psalm":
                    obj.book = "psalms"
                else:
                    if obj.show() in history:
                        obj.setName(f"V{history.count(obj.show()) + 1}")
                    closest.append(obj)
                    history.append(obj.show())
    elif ref.book is not None and ref.chapter is None and ref.verses is None:
        for obj in object_verses:
            if obj.book == ref.book:
                if obj.book.lower() == "psalm":
                    obj.book = "psalms"
                else:
                    if obj.show() in history:
                        obj.setName(f"V{history.count(obj.show()) + 1}")
                    closest.append(obj)
                    history.append(obj.show())

    if len(closest) != 0:
        return False, closest
    else:
        return False, None


"""
def compare(ref:str, available:list):

href = Search("João")
print(href)
Analyse(href)


REGEX

singe verse -> ^[a-zA-Z]+\s?\d{1,3}\:\d{1,3}$
range verse -> ^[a-zA-Z]+\s?\d{1,3}\:\d{1,3}\-\d{1,3}$

"""
