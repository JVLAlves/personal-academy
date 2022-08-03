from pprint import pprint

import PySimpleGUI as sg
import LITTY.glob.globals as glob


class selection:
    def __init__(self, title:str, collection:list):
        self.recollection = []
        self.title = title
        self.id = id
        self.collection = collection
        self.length = len(collection)

    def isThis(self, item:str):
        print(self.collection)
        print(self.recollection)
        if item in self.collection:
            if item not in self.recollection:
                self.recollection.append(item)
                print(f"{item} added to {self.title} recollection.")
        else:
            print(f"{item} does not belongs to the {self.title} collection.")

    def contextSegment(self):
        context_segment = {self.title:", ".join(self.recollection)}
        counter = 1
        lead = self.title.upper().replace("S", "")
        for index, item in enumerate(self.recollection):
            print(item)
            key = lead+f"{counter}"
            context_segment[key] = item
            counter+=1
        return context_segment




class popup_download:
    layout = [
        [sg.Push(), sg.Text("Choose a path to Download:", font=glob.FONT_H1.toPySimpleGui(), text_color=glob.FONT_H1.color), sg.Push()],
        [sg.Push(), sg.FolderBrowse(key="-DOWNPATH-", tooltip="This must be the folder in which you want your file to be downloaded."), sg.Text(), sg.Push()],
        [sg.VPush()],
        [sg.Push(), sg.Button("SUBMIT"), sg.Push()],
    ]

    def __init__(self):

        self.window = sg.Window("Download Path").layout(self.layout)

    def open(self):

        while True:
            event, value = self.window.read()
            if event == sg.WIN_CLOSED:
                sg.popup_error("The download path must be declared.", title="Download path not found.")
                continue
            elif event == "SUBMIT":
                if value is not None and value["-DOWNPATH-"] is not None:
                    self.window.close()
                    return value["-DOWNPATH-"]

class popup_selector:
    def __init__(self, list_elements:list):
        self.layout = [
            [sg.Push(), sg.Text("Select Information", font="Times 14 bold", text_color="#000000"), sg.Push()],
            [sg.VPush()]
        ]
        frames = []
        self.selections = []

        for element in list_elements:
            print(element)
            layout = []
            title = list(element.keys())[0]
            items = list(element.values())[0]


            print(title, items)
            select = selection(title, items)
            self.selections.append(select)
            for value in items:
                checkbox = [sg.Checkbox(value, key=value)]
                layout.append(checkbox)
            frames.append(sg.Frame(title, layout))

        self.layout.append(frames)
        self.layout.append([sg.VPush()])
        self.layout.append([sg.Push(), sg.Button("SELECT"), sg.Push()])

        self.window = sg.Window("SELECT").layout(self.layout)

    def open(self):

        while True:
            event, values = self.window.read()

            if event == sg.WIN_CLOSED:
                exit()
            elif event == "SELECT":
                pprint(values)
                for everyValue in values:
                    print(everyValue, values[everyValue])
                    if values[everyValue]:

                        for selection in self.selections:
                            selection.isThis(everyValue)

                overall_context = {}
                for category in self.selections:
                    overall_context.update(category.contextSegment())
                self.window.close()
                return overall_context








