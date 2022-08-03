import PySimpleGUI as sg
import globals.constants as glob
class initial_window:
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
                FOLDERS.append(glob.auto_files_path+folder+"/")
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



def init():
    basefolder = initial_window()
    TAGS, FOLDERS = basefolder.init()

    tags_and_folders = {}
    for k,v in zip(TAGS, FOLDERS):
        tags_and_folders[k] = v

    return tags_and_folders

