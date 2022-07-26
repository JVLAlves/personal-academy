import PySimpleGUI as sg

import LITTY.cmd.mongo.mongo_automation_cmds as mg_auto
from LITTY.cmd.obj.login_interface import initiate_login_window
import LITTY.glob.globals as glob
from LITTY.cmd.obj.automation_interface import automation_window

class AUTOMATION_INTERFACE:

    user_automations = []
    user_automations_headers = ["AUTOMATION"]

    #THE FIRST TAB THE USER WILL SEE
    TAB_INTRO = [
        [sg.VPush()],
        [sg.Push(), sg.Text("LITTY", font=glob.FONT_TITLE.toPySimpleGui(), text_color=glob.FONT_TITLE.color), sg.Push()],
        [sg.Push(), sg.Text("Automatização de Processos Litigiosos", font=glob.FONT_SUBTITLE.toPySimpleGui(), text_color=glob.FONT_SUBTITLE.color), sg.Push()],
        [sg.VPush()],
        [sg.VPush()],
        [sg.Push(), sg.Text("Made by J. V. L. Alves", font=glob.FONT_FOOTER.toPySimpleGui(), text_color=glob.FONT_FOOTER.color), sg.Push()]
    ]

    #THE TAB FOR CREATING A NEW AUTOMATION

    TAB_CREATE = [
        [sg.Push(), sg.Text("CREATE A AUTOMATION", font=glob.FONT_H1.toPySimpleGui(), text_color=glob.FONT_H1.color), sg.Push()],
        [sg.VPush()],
        [sg.Text("Type a name: "), sg.Input(key="-AUTONAME-", default_text="Automation_name", tooltip="This name must be UNIQUE"), sg.Text(key="-AVAILABLE-")],
        [sg.VPush()],
        [sg.FileBrowse(file_types=[("docx", "*.docx")], key="-DOCPATH-",tooltip="This file must be a Microsoft Word .docx tagged file. It will be used to automatic generate files from the data in the table."),sg.Text("choose a model")],
        [sg.FileBrowse(file_types=[("xlsx", "*.xlsx"), ("csv", "*.csv")], key="-TBLPATH-", tooltip="This file must be a Microsoft Excel .xlsx table or a .csv file. This file must contain the data for the automation."), sg.Text("choose a table")],
        [sg.Radio("Vertical", "TablePosition", key="vertical"), sg.Radio("Horizontal", "TablePosition", default=True, key="horizontal")],
        [sg.VPush()],
        [sg.VPush(), sg.Button("SUBMIT")],
    ]



    #THE BASE TAB WHICH WILL BE COMPLITED WITH THE AUTOMATION
    TAB_MINE = [
        [sg.Push(), sg.Text("MY AUTOMATIONS", font=glob.FONT_H1.toPySimpleGui(), text_color=glob.FONT_H1.color), sg.Push()],
        [sg.VPush()],
        [sg.Push(), sg.Table(values=user_automations, headings=user_automations_headers, display_row_numbers=False, justification="center", key="-AUTO_TABLE-", tooltip="Automations' table", enable_click_events=True), sg.Push()],
    ]


    def __init__(self, currentUser=None):
        self.User = currentUser

        #################--| WINDOW SETTINGS |--##########################################
        self.layout = [
            [sg.Text(f"Account: {self.User}", font=glob.FONT_P3.toPySimpleGui())],
            [sg.VPush()],
            [sg.TabGroup(
                [[
                    sg.Tab("WELCOME", self.TAB_INTRO, font=glob.FONT_P2.toPySimpleGui()),
                    sg.Tab("CREATE", self.TAB_CREATE, font=glob.FONT_P2.toPySimpleGui()),
                    sg.Tab("AUTOMATIONS", self.TAB_MINE, font=glob.FONT_P2.toPySimpleGui())
                ]], selected_title_color=glob.COMPANY_YELLOW, selected_background_color=glob.COMPANY_BLUE
            )
            ]
        ]
        self.window = sg.Window("AUTOMATION").layout(self.layout)

        while True:
            event, values = self.window.read(timeout=100)
            if event != "__TIMEOUT__":
                print(event)

            autos = mg_auto.query_automation({"created_by": f"{self.User}"})
            if autos is not None:
                for auto in autos:
                    if auto["name"] not in self.user_automations:
                        print(self.user_automations)
                        self.user_automations.append(auto["name"])
                        self.window["-AUTO_TABLE-"].update(values=self.user_automations)



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
                        docx_file = open(docx, "rb")
                        docx_content = docx_file.read()

                        table = values["-TBLPATH-"]
                        tbl_file = open(table, "rb")
                        tbl_content = tbl_file.read()

                        orientation = None
                        if values["vertical"]:
                            orientation = "vertical"
                        elif values["horizontal"]:
                            orientation = "horizontal"



                        automation = {"name": name, "docx":{"initial_path":docx, "content":docx_content},"tbl":{"initial_path":table, "content":tbl_content, "orientation":orientation}, "created_by":user}

                        mg_auto.insert_automation(automation)
                        sg.popup_notify(f"`{name}`Automation created sucessfully!")
            elif event != sg.TIMEOUT_EVENT:
                automation_window(event, self.User)

if __name__ == '__main__':
    USER = initiate_login_window()
    MAIN = AUTOMATION_INTERFACE(USER)



#TODO: add login and sigin tabs
#TODO: link automation to profiles