import PySimpleGUI as sg
import mongo.mongo_automation_cmds as mg_auto

class AUTOMATION_INTERFACE:

    TAB_CREATE = [
        [sg.Push(), sg.Text("CREATE A AUTOMATION", font="Times 14 bold", text_color="#000000"), sg.Push()],
        [sg.VPush()],
        [sg.Text("Type a name: "), sg.Input(key="-AUTONAME-", default_text="Automation_name", tooltip="This name must be UNIQUE"), sg.Text(key="-AVAILABLE-")],
        [sg.VPush()],
        [sg.FileBrowse(file_types=[("xlsx", "*.xlsx"), ("csv", "*.csv")], key="-TBLPATH-", tooltip="This file must be a Microsoft Excel .xlsx table or a .csv file. This file must contain the data for the automation."), sg.Text("choose a table")],
        [sg.FileBrowse(file_types=[("docx", "*docx")], key="-DOCPATH-", tooltip="This file must be a Microsoft Word .docx tagged file. It will be used to automatic generate files from the data in the table."), sg.Text("choose a model")],
        [sg.VPush()],
        [sg.VPush(), sg.Push(), sg.Button("SUBMIT"), sg.Push()],
    ]
    def __init__(self, currentUser=None):
        self.User = currentUser

        self.layout = [
            [sg.TabGroup(
                [[
                    sg.Tab("CREATE", self.TAB_CREATE),
                ]]
            )
            ]
        ]
        self.window = sg.Window("AUTOMATION").layout(self.layout)

        while True:
            event, values = self.window.read(timeout=100)

            if values is not None and values["-AUTONAME-"] is not None:
                #database verification
                exists = mg_auto.automation_exists(values["-AUTONAME-"])


                if not exists:
                    self.window["-AVAILABLE-"].update("AVAILABLE")
                    self.section_available = True
                else:
                    self.window["-AVAILABLE-"].update("NOT AVAILABLE")
                    self.section_available = False

            if event == sg.WIN_CLOSED:
                break

            elif event == "SUBMIT":
                if values is not None:
                    if values["-DOCPATH-"] != "" and values["-TBLPATH-"] != '' and self.section_available:
                        name = values["-AUTONAME-"]
                        user = self.User
                        docx = values["-DOCPATH-"]
                        table = values["-TBLPATH-"]

                        automation = {"name": name, "files":{"default_file_path": docx, "data_table_path":table}, "create_by":user}

                        mg_auto.insert_automation(automation)
                        sg.popup_notify(f"`{name}`Automation created sucessfully!")


        self.window.close()

class MAIN_INTERFACE:
    WINDOW_NAME = "LITTY"

    def __init__(self):
        self.layout = [
            [sg.Push(), sg.Text(self.WINDOW_NAME, font="Times 14 bold", text_color="#000000"), sg.Push()],
            [sg.Push(), sg.Text("Automação de Processos Litigiosos", font="Times 10", text_color="#000000"), sg.Push()],
            [sg.VPush()],
            [sg.Push(), sg.Button("Automation", key='-AUTO-'), sg.Push()]

        ]

        self.window = sg.Window(self.WINDOW_NAME).layout(self.layout)

    def init(self):
        while True:
            event, _ = self.window.read()

            if event == sg.WIN_CLOSED:
                break
            elif event == '-AUTO-':
                self.window.close()
                self.automation()
                exit()
        self.window.close()



    def automation(self):
        AUTOMATION_INTERFACE()


if __name__ == '__main__':
    MAIN = MAIN_INTERFACE()
    MAIN.init()


#TODO: add login and sigin tabs
#TODO: link automation to profiles