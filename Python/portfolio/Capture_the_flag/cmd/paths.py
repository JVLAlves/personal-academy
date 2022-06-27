import os.path
from pathlib import Path
from configparser import ConfigParser

import PySimpleGUI as sg

CONFIGFILE = '.tags.ini'
HOME = str(Path.home())
AUTOF = HOME + "/automatic_files/"

class basefolders_window:
    def __init__(self):
        layout = [
            [sg.Push(), sg.Text("NAME YOUR FIRSTS FOLDERS", font="Arial 16 bold", text_color="#000000"), sg.Push()],
            [sg.VPush()],
            [sg.Text("Define Tag and Folder: "), sg.Input(size=(5, 1), key="-TAG-", default_text="TAG", tooltip="Three Uppercase letters only"), sg.Input(size=(14,1), key="-FOLDER-", default_text="Folder", tooltip="Your folder name"), sg.Button("ADD", key="-ADD-")],
            [sg.VPush()],
            [sg.Text("TAGS AND FOLDERS")],
            [sg.Text("Nothing yet", key="-TAGSNFOLDERS-")],
            [sg.VPush()],
            [sg.Push(), sg.Button("DELETE", key="-DELLAST-", tooltip="Delete last folder path and tag", button_color="#9e2a2b"),sg.Button("SUBMIT", key="-SUBMIT-", button_color="#3a5a40"), sg.Push()]
        ]

        self.window = sg.Window("First Folders").layout(layout)
    def init(self):
        TAGS = []
        FOLDERS = []
        while True:
            event, value = self.window.read(timeout=100)
            if len(TAGS) != 0 and len(FOLDERS) != 0:
                TnFlist = ""
                for tag, folder in zip(TAGS, FOLDERS):
                    TnFlist += f"{tag}  {folder}\n"

                self.window["-TAGSNFOLDERS-"].update(TnFlist)

            if event == sg.WIN_CLOSED:
                exit()
            elif event == "-ADD-":
                if value is None:
                    raise Exception("Unknown Error")

                #TAG format verification
                if not value["-TAG-"].isalpha() or len(value["-TAG-"]) != 3:
                    sg.popup_error(f"TAGS MUST BE THREE UPPERCASE LETTERS ONLY\n LENGTH: {len(value['-TAG-'])}")
                    continue

                tag = value["-TAG-"].upper()
                folder = value["-FOLDER-"]

                TAGS.append(tag)
                FOLDERS.append(AUTOF+folder+"/")
                continue

            elif event == "-DELLAST-":
                if len(TAGS) == 0 and len(FOLDERS) == 0:
                    sg.popup_error("Can not delete nothing.")
                    continue

                TAGS.pop(-1)
                FOLDERS.pop(-1)
                continue

            elif event == "-SUBMIT-":
                self.window.close()
                return (TAGS, FOLDERS)




def Config():
    if not os.path.exists(AUTOF):
        os.mkdir(AUTOF)

    if not os.path.exists(CONFIGFILE):
        init()

    config = ConfigParser()
    config.read(CONFIGFILE)
    return config



#create and populate the config file for the first time
def init():
    #set the firsts tags and folders
    basefolder = basefolders_window()
    TAGS, FOLDERS = basefolder.init()

    #create .ini file to populated
    with open(CONFIGFILE, "x"):
        pass

    #make the file a config
    config = ConfigParser()
    config.read(CONFIGFILE)

    config.add_section("TAGS")

    for tag, folder in zip(TAGS, FOLDERS):
        print(tag, folder)
        config.set("TAGS", tag, folder)

    with open(CONFIGFILE, "w") as ConfigFile:
        config.write(ConfigFile)


def start():
    config = Config()

    tags_and_folders = {}
    TAGS = config["TAGS"]
    for elem in TAGS:
        tags_and_folders[elem.upper()] = TAGS[elem]

    if not os.path.exists(HOME + "/automatic_files/"):
        os.mkdir(HOME + "/automatic_files/")
    for path in tags_and_folders.values():
        if not os.path.exists(path):
            os.mkdir(path)
    return tags_and_folders

def ExistsOnConfigfile(KeyVal:str, information:str, return_element:bool=False, return_alterElement:bool=False):

    config = Config()
    valid = {"key", "value"}


    if KeyVal not in valid:
        raise ValueError("results: KeyVal must be one of %r." % valid)


    if KeyVal == "key":
        for key, value in config["TAGS"].items():
            if key == information:
                if return_element:
                    return True, key
                elif return_alterElement:
                    return True, value
                else:
                    return True, None

        return False, None

    elif  KeyVal == "value":
        for key, value in config["TAGS"].items():
            if value == information:
                if return_element:
                    return True, value
                elif return_alterElement:
                    return True, key
                else:
                    return True, None

        return False, None


