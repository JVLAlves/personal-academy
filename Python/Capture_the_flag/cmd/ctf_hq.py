from paths import tags_and_folders
import PySimpleGUI as sg
from paths import *
from ctf import *

def isTag(possible_tag: str):
    if possible_tag.isupper() and len(possible_tag) == 3:
        return True
    else:
        return False


def tagExists(tag: str):
    if tag in tags_and_folders.keys():
        return True
    else:
        return False


class new_tag_window:
    config = Config()

    def __init__(self, tag: str):
        black = "#000000"
        layout = [
            [sg.Text("NEW TAG FORM", font="Arial 16 bold", text_color=black)],
            [sg.Text("TAG:       ", text_color=black),
            sg.InputText(default_text=tag.upper(), size=(5, 1), key="-TAG-", font="Arial 10")],
            [sg.Text("FOLDER:", text_color=black), sg.Input(default_text=tag.lower(), size=(8, 1), key="-FOLDER-")],
            [sg.Submit(button_color="#2a850e")]

        ]
        self.window = sg.Window("NEW TAG FORM", font="Arial 10").layout(layout).finalize()
        self.esc = self.window.bind("<Key-Escape>", "esc")
        self.enter = self.window.bind("<Key-Return>", "enter")

        while True:
            event, keys = self.window.read()
            print(event)
            if event == sg.WIN_CLOSED or event == self.esc or event == "Cancel":
                break

            elif event == "Submit" or event == self.enter:
                self.config.set("tags", f"{keys['-TAG-'].upper()}", AUTOF + keys['-FOLDER-'] + "/")
                with open(FILE, "w") as configFile:
                    self.config.write(configFile)
                break

        self.window.close()
        time.sleep(5)
        ctf()

class verify_tag_window:
    def __init__(self, tag: str):
        layout = [
            [sg.Text(f"Add a new tag named", font="Arial 16 bold"),
            sg.Text(tag, font='Arial 16 bold italic', text_color="#45040c"), sg.Text("?", font="Arial 16 bold")],
            [sg.OK(button_color="#2a850e"), sg.Cancel(button_color="#ba0c0c")]
        ]

        self.window = sg.Window("NEW TAG FOUND", font="Arial 10").layout(layout).finalize()
        self.esc = self.window.bind("<Key-Escape>", "esc")
        self.enter = self.window.bind("<Key-Return>", "enter")

        event, _ = self.window.read()
        if event == sg.WIN_CLOSED or event == self.esc or event == "Cancel":
            self.window.close()

        elif event == "OK" or event == self.enter:
            self.window.close()
            new_tag_window(tag)

class files_of_tag:
    config = Config()
    def __init__(self, tag:str):
        column = [[sg.Push(), sg.Text(f"FILES OF TAG {tag.upper()}", font="Arial 16 bold", text_color="#000000"), sg.Push(), sg.VPush()]]
        files = os.listdir(config["tags"][tag.lower()])
        for file in files:
            semicol = [sg.Text(file, font="Arial 12", text_color="#000000")]
            column.append(semicol)

        self.window = sg.Window(f"-{tag.upper()}-").layout(column)
        while True:
            event, _ = self.window.read()
            if event == sg.WIN_CLOSED:
                break
        self.window.close()




class tag_list_window:
    config = Config()
    def __init__(self):
        self.tag_list = list(self.config["tags"])
        column = [
            [sg.Push(), sg.Text("All TAGS", font="Arial 16 bold", text_color="#000000"), sg.Push()]
        ]
        for elem in self.tag_list:
            semicol = [sg.Push(), sg.Button(f"{elem.upper()}", font="Arial 14", size=(5,1)), sg.Push()]
            column.append(semicol)

        self.window = sg.Window("ALL TAGS", font="Arial 8").layout(column)

        while True:
            event, _ = self.window.read()
            if event == sg.WIN_CLOSED:
                break
            else:
                print(event)
                files_of_tag(event)
        self.window.close()



class CTF_menu:
    config = Config()
    def __init__(self):
        layout=[
            [sg.Push(), sg.Text("CTF", font="Arial 30 bold", text_color="#000000"), sg.Push()],
            [sg.Push(), sg.Text("Capture The Flag", font="Arial 20 italic", text_color="#000000"), sg.Push()],
            [sg.VPush()],
            [sg.VPush()],
            [sg.VPush(), sg.Push(), sg.Button("Start Filter", key="-START-", font="Arial 14", size=(15,1)), sg.Push()],
            [sg.VPush(), sg.Push(), sg.Button("Create New Tag", key="-NEW-", font="Arial 14", size=(15,1)), sg.Push()],
            [sg.VPush(), sg.Push(), sg.Button("All Tags", key="-ALL-", font="Arial 14", size=(15,1),), sg.Push()],
            [sg.VPush()],
            [sg.VPush()],
            [sg.Push(), sg.Text("Auto-Filter:", font="Arial 14", text_color="#000000"), sg.Push()],
            [sg.Push(), sg.Radio("on", "STATUS", key="online", default=True, font="Arial 14"), sg.Push()],
            [sg.Push(), sg.Radio("off", "STATUS", key="offline", font="Arial 14"), sg.Push()],
            [sg.VPush()],
            [sg.Push(), sg.Cancel("LEAVE", key="-EXIT-", font="Arial 12"), sg.Push()]
        ]
        self.window = sg.Window("CTF menu").layout(layout).finalize()

    def init(self):
        while True:
            event, value = self.window.read()
            if event == sg.WIN_CLOSED or event == "-EXIT-":
                if value is not None:
                    if value["online"]:
                        self.config.set("autofilter", "status", "online")
                        with open(FILE, "w") as configFile:
                            self.config.write(configFile)
                    elif value["offline"]:
                        self.config.set("autofilter", "status", "offline")
                        with open(FILE, "w") as configFile:
                            self.config.write(configFile)
                break
            elif event == "-START-":
                ctf()
                sg.popup("Filter done")
            elif event == "-NEW-":
                new_tag_window("")
            elif event == "-ALL-":
                tag_list_window()
        self.window.close()


if __name__ == "__main__":
    window = CTF_menu()
    window.init()
