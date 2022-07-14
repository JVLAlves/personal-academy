import os
import pathlib

import paths
import PySimpleGUI as sg
from paths import *
from ctf import *

def isTag(possible_tag: str):
    if possible_tag.isupper() and len(possible_tag) == 3:
        return True
    else:
        return False


def tagExists(tag: str):
    tags_and_folders = paths.start()
    if tag in tags_and_folders.keys():
        return True
    else:
        return False


class new_tag_window:
    config = Config()
    answer = None
    TNF_dict = None

    def __init__(self, initial_tag: str):
        black = "#000000"
        layout = [
            [sg.Text("NEW TAG FORM", font="Arial 16 bold", text_color=black)],
            [sg.Text("TAG:       ", text_color=black, font="Arial 12"),
            sg.InputText(default_text=initial_tag.upper(), size=(5, 1), key="-TAG-", font="Times 14 bold")],
            [sg.Text("FOLDER:", text_color=black, font="Arial 12"), sg.InputText(default_text=initial_tag.lower(), size=(5, 1), key="-FOLDER-", font="Arial 14")],
            [sg.VPush()],
            [sg.Push(), sg.Text("PREVIEW", font="Arial 14"), sg.Push()],
            [sg.VPush()],
            [sg.Push(), sg.Text("", font="Arial 12",key="-TNF_PREVIEW-"), sg.Push()],
            [sg.VPush()],
            [sg.Submit(button_color="#2a850e")]

        ]
        self.window = sg.Window("NEW TAG FORM", font="Arial 10").layout(layout).finalize()
        self.esc = self.window.bind("<Key-Escape>", "esc")
        self.enter = self.window.bind("<Key-Return>", "enter")

        while True:
            event, keys = self.window.read(timeout=100)

            #if keys list is not null (None), update the preview in the GUI
            if keys is not None :


                #turns the nested directory path into split directories
                dir_obj = pathlib.PurePath(keys['-FOLDER-'])

                #list the directories
                directories = list(dir_obj.parts)

                TNF_PREVIEW = "" #this is the text which will be shown in the GUI
                PATH = AUTOF #initial path to add up to the new directories
                NEW_DIRS = {} # a dictionary to storage the new tags and folders

                #loop through the directories list
                for index, dir in enumerate(directories):

                    inside_tag = keys['-TAG-'].upper() #this is the tag announced by the User

                    PATH += f"{dir}/" #increments the path the nested directories in the list



                    # verify if the directory already exists
                    #if the path already exists, it must not create a new tag.

                    AlreadyExist, key = ExistsOnConfigfile("value", PATH, return_alterElement=True)

                    if AlreadyExist:
                        inside_tag = key.upper()

                    #the tag announced by the User must always be assigned to the last directory
                    #if the directory is not the last one and it does not exists yet, create a new tag
                    if (index != len(directories)-1 and not AlreadyExist) or (keys['-TAG-'] is None or keys['-TAG-'] == ""):

                        #initially creates a tag based on the three first letters of directory's name
                        built_tag = dir[:3].upper()




                        inside_tag = built_tag
                    text = f"TAG: {inside_tag}  PATH: {PATH}\n\n"
                    NEW_DIRS[inside_tag] = PATH
                    TNF_PREVIEW += text
                self.window["-TNF_PREVIEW-"].update(TNF_PREVIEW)
                self.TNF_dict = NEW_DIRS


            if event == sg.WIN_CLOSED or event == self.esc or event == "Cancel":
                self.answer = False
                break

            elif event == "Submit" or event == self.enter:
                isSubmit = self.__submit(self.TNF_dict)
                if isSubmit:
                    break
                else:
                    continue




        self.window.close()
        time.sleep(5)
    def returnment(self):
        return self.answer
    def __submit(self, TNF_dict:dict):
        set = 0
        for tag, path in TNF_dict.items():
            AlreadyExist, _ = ExistsOnConfigfile("key", tag.lower())
            if AlreadyExist:
                continue

            if len(tag) != 3:
                sg.popup_error("Please, type a three letter tag.")
                return False

            self.config.set("TAGS", tag, path)
            set += 1

        if set > 0:
            with open(CONFIGFILE, "w") as configFile:
                self.config.write(configFile)
            self.answer = True
            sg.popup_ok("New Tags Created")
        return True

class verify_tag_window:
    answer = None
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
            self.answer = new_tag_window(tag).returnment()
    def returnment(self):
        return self.answer

class files_of_tag:
    config = Config()
    def __init__(self, tag:str):
        column = [[sg.Push(), sg.Text(f"FILES OF TAG {tag.upper()}", font="Arial 16 bold", text_color="#000000"), sg.Push(), sg.VPush()]]
        files = os.listdir(self.config["TAGS"][tag.lower()])
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
        self.tag_list = list(self.config["TAGS"])
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
            [sg.Push(), sg.Cancel("LEAVE", key="-EXIT-", font="Arial 12"), sg.Push()]
        ]
        self.window = sg.Window("CTF menu").layout(layout).finalize()

    def init(self):
        while True:
            event, value = self.window.read()
            if event == sg.WIN_CLOSED or event == "-EXIT-":
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
    new_tag_window("ACL")
