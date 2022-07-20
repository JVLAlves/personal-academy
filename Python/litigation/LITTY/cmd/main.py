from pprint import pprint

import PySimpleGUI as sg
import mongo.mongo_automation_cmds as mg_auto
from login_interface import initiate_login_window
class AUTOMATION_INTERFACE:

    #THE FIRST TAB THE USER WILL SEE
    TAB_INTRO = [
        [sg.VPush()],
        [sg.Push(), sg.Text("LITTY", font="Times 16 bold", text_color="#000000"), sg.Push()],
        [sg.Push(), sg.Text("Automatização de Processos Litigiosos", font="Times 12", text_color="#000000"), sg.Push()],
        [sg.VPush()],
        [sg.VPush()],
        [sg.Push(), sg.Text("Made by J. V. L. Alves", font="Times 10 italic", text_color="#000000")]
    ]

    #THE TAB FOR CREATING A NEW AUTOMATION
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



    #THE BASE TAB WHICH WILL BE COMPLITED WITH THE AUTOMATION
    TAB_MINE = [
        [sg.Push(), sg.Text("MY AUTOMATIONS", font="Times 14 bold", text_color="#000000"), sg.Push()],
        [sg.VPush()],
    ]

    def __init__(self, currentUser=None):
        self.User = currentUser

        self.__get_automation_name()
        #################--| WINDOW SETTINGS |--##########################################
        self.layout = [
            [sg.Text(f"Account: {self.User}", font="Arial 10")],
            [sg.VPush()],
            [sg.TabGroup(
                [[
                    sg.Tab("WELCOME", self.TAB_INTRO, font="Tahoma, 12"),
                    sg.Tab("CREATE", self.TAB_CREATE, font="Tahoma, 12"),
                    sg.Tab("AUTOMATIONS", self.TAB_MINE,font="Tahoma, 12")
                ]], selected_title_color="#BF945A", selected_background_color="#13476A"
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

    def __get_automation_name(self):
        autos =  mg_auto.query_automation({"created_by":f"{self.User}"})
        for automation in autos:
            element = [sg.Push(), sg.Button(automation["name"], font="Times 16"), sg.Push()]
            self.TAB_MINE.append(element)

        self.TAB_MINE.append([sg.VPush()])

if __name__ == '__main__':
    USER = initiate_login_window()
    MAIN = AUTOMATION_INTERFACE(USER)



#TODO: add login and sigin tabs
#TODO: link automation to profiles