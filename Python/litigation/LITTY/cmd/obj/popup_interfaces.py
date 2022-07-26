import PySimpleGUI as sg

class popup_download:
    layout = [
        [sg.Push(), sg.Text("Choose a path to Download:", font=" 14 bold", text_color="#000000"), sg.Push()],
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
                self.window.close()
                return None
            elif event == "SUBMIT":
                if value is not None and value["-DOWNPATH-"] is not None:
                    self.window.close()
                    return value["-DOWNPATH-"]