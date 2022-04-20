import io
import os
import PySimpleGUI as sg
import re
import requests
import cloudscraper

from crawl import *
from biblepaths import *
import webbrowser
from PIL import Image


class main:
    def __init__(self):
        layout = [
            [sg.VPush()],
            [sg.Push(), sg.Text("Full of Eyes Image Searcher", font="Arial 16 bold"), sg.Push()],
            [sg.Push(), sg.Text("Versículo: "), sg.Input(key="verse", default_text="êxodo 17:17"), sg.Push()],
            [sg.Push(), sg.Button("Search", key="search"), sg.Push()],
            [sg.VPush()],
        ]
        self.window = sg.Window("main window").layout(layout)

    def Run(self):
        while True:
            event, value = self.window.Read()
            if event == sg.WIN_CLOSED:
                break
            elif event == "search":
                verse = value["verse"]
                print(verse)
                agroupment = re.findall("([^\W\d_]+)\s(\d{1,3}):(\d{1,3}-\d{1,3}|\d{1,3})", verse)
                print(agroupment[0])
                passage = Passage(agroupment[0][0], agroupment[0][1], agroupment[0][2])
                href = Search(passage.book)
                verses = Analyse(href)
                imgExists, answer = compare(passage, verses)
                return imgExists, answer
        self.window.close()


class Afirmative:
    def __init__(self, passage: object):

        jpg_data = (
            cloudscraper.create_scraper(
                browser={"browser": "firefox", "platform": "windows", "mobile": False}
            ).get(passage.img.src).content)

        pil_image = Image.open(io.BytesIO(jpg_data))
        png_bio = io.BytesIO()
        pil_image.save(png_bio, format="PNG")
        png_data = png_bio.getvalue()


        headers = {
            'api-key': "4223398bc109e6c68df22e4f96ebc69e",
            'content-type': 'application/json'
        }
        vers = requests.request("GET", f"http://getbible.net/json?scrip={passage.show()}", headers=headers)
        print(vers.content)
        layout = [
            [sg.VPush()],
            [sg.Push(), sg.Text("The image Exists!", font="Arial 16 bold"), sg.Push()],
            [sg.Push(), sg.Text(f"Versículo: {passage.show()}", font="Arial 12 italic"), sg.Push()],
            [sg.VPush(), sg.Push(), sg.Text(vers.verse, font="Arial 14 italic"), sg.Push(), sg.VPush()],
            [sg.VPush(), sg.Push(), sg.Image(data=png_data), sg.Push(), sg.VPush()],
            [sg.Push(), sg.Button("See on Page", key="see"), sg.Button("Download", key="download"), sg.Push()],
            [sg.VPush()],
        ]
        self.window = sg.Window(passage.show()).layout(layout)
        while True:
            event, value = self.window.Read()
            if event == sg.WIN_CLOSED:
                break
            elif event == "see":
                webbrowser.open(passage.img.href)
            elif event == "download":
                download_path = os.environ['HOME']+"/Downloads"
                filename = download_path + "/" + passage.show()+ ".png"
                if not os.path.isdir(download_path):
                    os.makedirs(download_path)
                with Image.open(io.BytesIO(png_data)) as im:
                    im.save(filename, "PNG")
                sg.popup("Image Downloaded.", title="Success!")
        self.window.close()


win = main()
ans, objs = win.Run()

if ans:
    Afirmative(objs)
else:
    if objs is not None:
        fullText = ''
        for ob in objs:
            fullText += f"Ref: {ob.show()}, Link: {ob.href}\n"
        sg.popup(fullText, title="Closest References Found", font="Arial 12 italic")
    else:
        sg.popup("No image found for the searched verse.", title="Not Found")

"""


TODO LIST
- Input Cases: Only the Book, Only book and Chapter
- List images, create a button with a popup preview of the image. 
- Include verse text through API if possible
- Exceptions and Popups
- Key Binding (enter)  to the search
- Special receiving Cases: Ref with commas or with plus sign (Maybe will be excluded)


"""