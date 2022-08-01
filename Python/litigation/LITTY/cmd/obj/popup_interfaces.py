import PySimpleGUI as sg
import LITTY.glob.globals as glob

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

        for element in list_elements:
            layout = []
            title = element.keys()[0]
            for value in element.values()[0]:
                checkbox = [sg.Checkbox(value, key=value)]
                layout.append(checkbox)
            frames.append([sg.Frame(title, layout)])

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








