import os.path
import os
import shutil
import time
from pathlib import Path
import subprocess as sub



#file path windows
class path_window:
    def __init__(self):
        layout = [
            [sg.Push(), sg.Text("CTF INSTALLER", font="Arial 16 bold", text_color="#000000"), sg.Push()],
            [sg.VPush()],
            [sg.Text("select your desktop file: ", font="Arial 12"), sg.FolderBrowse(initial_folder=HOME, key="-DESKTOP-")],
            [sg.Push(), sg.Button("Submit", key="-SUBMIT-"), sg.Push()]
        ]

        self.window = sg.Window("CTF INSTALLER").layout(layout)

    def init(self):
        while True:
            event, value = self.window.read()

            if event == sg.WIN_CLOSED:
                exit()
            elif event == "-SUBMIT-":
                self.window.close()
                return value["-DESKTOP-"]



import PySimpleGUI as sg

#track the executable file
HOME = str(Path.home())
HERE = os.getcwd()
filename = ".AUTOCTF"

def FindTheFlag():
    if os.path.exists(HERE+"/"+filename):
        return True
    else:
        return False

#run a first time
def TouchTheFlag():
    pathwindow = path_window()
    desktop = pathwindow.init()
    if os.path.exists(desktop):
        pass
    else:
        raise FileExistsError

    shutil.move(HERE+"/"+filename, desktop)
    return desktop

def CaptureTheFlagOunce(DESKTOP:str):
    print(DESKTOP)
    sub.run([f"{DESKTOP}/{filename}"])
    if not os.path.exists(DESKTOP+"/.tags.ini"):
        if os.path.exists(".tags.ini"): #in INSTALLER FOLDER
            shutil.move(".tags.ini", DESKTOP)
    sg.popup("Now, for you to automate the process, read the instructions in the README.md file.\n\n Thank you for the patience!", font="Arial 16")

#make sure the files were created sucessfully
#create an standar GUI for the user to decide what will be the basics folders

if __name__ == "__main__":
    FlagFound = FindTheFlag()
    if FlagFound:
        DESKTOP = TouchTheFlag()
        CaptureTheFlagOunce(DESKTOP)
