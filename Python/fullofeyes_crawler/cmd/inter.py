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
            [sg.Push(), sg.Text("Versículo: "), sg.Input(key="verse", default_text="john 3:16"), sg.Push()],
            [sg.Push(), sg.Button("Search", key="search"), sg.Push()],
            [sg.VPush()],
        ]
        self.window = sg.Window("main window").layout(layout)

    #executes the main window process of opening and functioning
    def Run(self):
        while True:
            event, value = self.window.Read()
            print(event)
            if event == sg.WIN_CLOSED:
                break

            #When the only functional button "search" is clicked it triggers the searching process
            elif event == "search":
                verse = value["verse"]
                print(verse)

                #REGEX PATTERNS
                #MATCHES: Book, Chater and Verse (i.e. Matthew 24:11)
                wholeRef = re.compile("([^\W\d_]+)\s(\d{1,3}):(\d{1,3}-\d{1,3}|\d{1,3})")

                #MATCHES: Book and Chapter only (i.e. Matthew 24)
                bookChapterRef = re.compile("([^\W\d_]+)\s(\d{1,3})")

                #MATCHES: Book only (i.e. Matthew)
                bookOnlyRef = re.compile("([^\W\d_]+)")



                # if it matches the Whole Reference...
                if re.match(wholeRef, verse):

                    #then separete the components (Book, Chapter, Verse)
                    agroupment = re.findall(wholeRef, verse)

                    print(agroupment[0]) #print it

                    #assign it
                    book, chapter, verse = agroupment[0]

                    #Tries to create a Passage object which contains the Components
                    #if it fails the window loop restarts
                    #else keeps searching the passage, first by the book
                    try:
                        passage = Passage(book, chapter, verse)
                    except:
                        continue
                    else:
                        href = Search(passage.book)
                        verses = Analyse(href)
                        imgExists, answer = compare(passage, verses)
                        return imgExists, answer

                #if it matches the Book and Chapter Only reference
                elif re.match(bookChapterRef, verse):

                    #then separate it
                    book_chap = re.findall(bookChapterRef, verse)

                    print(book_chap[0]) # print it

                    #assign ti
                    book, chapter = book_chap

                    # Tries to create a Passage object which contains the Book and Chapter only
                    # if it fails the window loop restarts
                    # else keeps searching the passage, first by the book
                    try:
                        passage = Passage(book, chapter, None)
                    except:
                        continue
                    else:
                        href = Search(passage.book)
                        verses = Analyse(href)
                        imgExists, answer = compare(passage, verses)
                        return imgExists, answer



                # if it matches the Book Only reference...
                elif re.match(bookOnlyRef, verse):

                    # NO NEED OF REGEX SEPARATION

                    # Tries to create a Passage object which contains the Book only
                    # if it fails the window loop restarts
                    # else keeps searching the passage, first by the book
                    try:
                        passage = Passage(verse, None, None)
                    except:
                        continue
                    else:
                        href = Search(passage.book)
                        verses = Analyse(href)
                        imgExists, answer = compare(passage, verses)
                        return imgExists, answer

        self.window.close()


# in case of the exactly image exists, there is a Afirmative (or positive) window to show it.
class Afirmative:
    def __init__(self, passage: object):

        # Searches for the image
        jpg_data = (
            cloudscraper.create_scraper(
                browser={"browser": "firefox", "platform": "windows", "mobile": False}
            ).get(passage.img.src).content)

        pil_image = Image.open(io.BytesIO(jpg_data))
        png_bio = io.BytesIO()
        pil_image.save(png_bio, format="PNG")
        png_data = png_bio.getvalue()


        #Searches of the English biblical passage of the reference
        headers = {
            'api-key': "4223398bc109e6c68df22e4f96ebc69e",
            'content-type': 'application/json'
        }
        print(f"What is written in {passage.show(to_request=True)}?")
        verse_json = requests.request("GET", f"http://getbible.net/json?scrip={passage.show(to_request=True)}&raw=true", headers=headers).json()
        chapter = verse_json["book"][0]["chapter"]
        verse_keys = list(chapter.keys())
        verse = ''
        for vk in verse_keys:
            verse += " " + chapter[vk]['verse']

        # window layout
        layout = [
            [sg.VPush()],
            [sg.Push(), sg.Text("The image Exists!", font="Arial 16 bold"), sg.Push()],
            [sg.VPush(), sg.Push(), sg.Text(verse, font="Arial 14 italic"), sg.Push(), sg.VPush()],
            [sg.Push(), sg.Text(f"Versículo: {passage.show()}", font="Arial 12 italic"), sg.Push()],
            [sg.VPush(), sg.Push(), sg.Image(data=png_data), sg.Push(), sg.VPush()],
            [sg.Push(), sg.Button("See on Page", key="see"), sg.Button("Download", key="download"), sg.Push()],
            [sg.VPush()],
        ]
        self.window = sg.Window(passage.show()).layout(layout)

        #the window running process, in this case, is automatic
        while True:
            event, value = self.window.Read()
            if event == sg.WIN_CLOSED:
                break


            # if the "See" button is clicked, the lead the user to the Full of Eyes page of origin
            elif event == "see":
                webbrowser.open(passage.img.href)


            # if the "Download" button is clicked, it downloads the image to the compute
            elif event == "download":
                download_path = os.environ['HOME'] + "/Downloads"
                filename = download_path + "/" + passage.show() + ".png"
                if not os.path.isdir(download_path):
                    os.makedirs(download_path)
                with Image.open(io.BytesIO(png_data)) as im:
                    im.save(filename, "PNG")
                sg.popup("Image Downloaded.", title="Success!")

        self.window.close()



# in case the reference is not greatly especific of the exact reference does not exists but similiar does
# there is a Possible window to show all the possible images which could match that reference, including all of them.
class Possible:
    def __init__(self, closests: list):

        #assign the closest references to a list atribute
        self.closests = closests

        #default layout which is going to be incremented later
        layout = [
            [sg.VPush()],
        ]

        # for each passage in closest array, create a button with the reference in the default layout
        for passages in closests:
            layout_part = [sg.Push(), sg.Button(f"{passages.getName()}", key=f"{passages.getName()}"), sg.Push()]
            layout.append(layout_part)

        layout.append([sg.VPush()])

        # window running process
        self.window = sg.Window("Closest passages found").layout(layout)
        while True:
            event, value = self.window.Read(timeout=100)
            if event == sg.WIN_CLOSED:
                break

            # considering there are a lot of button the logic is:
            # if any event is triggered get the name of it and shows an Afirmative window of it
            elif event is not None:
                passage = ''
                for c in self.closests:
                    if event == c.getName():
                        passage = c
                if passage != '':
                    Afirmative(passage)


        self.window.close()


if __name__ == "__main__":
    win = main()
    ans, objs = win.Run()
    if ans:
        Afirmative(objs)
    else:
        if objs is not None:
            Possible(objs)
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

#ERROR:Book of John (João) Cannot be found. Maybe it is a problem in the translation.
#TODO: Improve the GUI of 'CHOICES' (buttons) and the presentation GUI.
#TODO: Improve Image download method and resolution.
#TODO: Check the error of translation.
#TODO: Faster the webscrapping, if possible.
#TODO: Create english and portuguese versions.


