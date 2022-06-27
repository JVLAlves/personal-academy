from configparser import ConfigParser

import edit as edit
from docxtpl import DocxTemplate
import file_management as filem
import const
import excel as xl
import PySimpleGUI as sg
from login import *

TEMPLATE, TABLE= xl.init()
configFile = "deluiz_config.ini"
conf = ConfigParser()
conf.read(configFile)


def GenerateFileFromDefaultDocx(context:dict, template:xl.File=xl.File(TEMPLATE)):
    # Opens the DOCX Template and turns it into a object
    doc = DocxTemplate(template.path) # Always needs to be a Path

    # Make the changes and generate a new document
    doc.render(context)

    # saves the new document with the wishing name
    #TODO: Custom place of saving
    doc.save(f"{context['cliente_fullname'].replace(' ', '')}{const.FILE_WATERMARK}{const.FILE_EXTENSION}")



# Configures the values which will be changed in the Template --> Observation: the keys of the Dictionary
# MUST be the same found the Template document between double brackets I.E.: {{company_name}}
#TODO: Create a better function which handles custom headers
def GenerateContext(pDict:dict):
    splitname = pDict["CLIENTE"].split(" ")
    social_name = [splitname[0], splitname[-1]]
    socialname = " ".join(social_name).title()

    Context =  {
        'process_number': pDict["# PROCESSO"],
        'cliente_socialname': socialname,
        'cliente_fullname': pDict["CLIENTE"].title(),
        'lawyer_fullname': pDict["ADVOGADO ENCARREGADO"].title(),
        "expected_value": float(pDict["VALOR ESPERADO"]),
        "wishing_value": float(pDict["VALOR PEDIDO"]),
        "lawyer_cost": float(pDict["RETORNO DO ADVOGADO"])
        }
    return Context

class automation_window:
    Config = conf
    def __init__(self, automation:str):
        self.section = automation
        self.docx = xl.File(self.Config[self.section]["docx"])
        self.table = xl.File(self.Config[self.section]["table"])
        layout = [
            [sg.Push(), sg.Text(f"{automation.upper()}", font="Arial 20 bold", text_color="#000000"), sg.Push()],
            [sg.VPush()],
            [sg.Text("DOCX Path: ", font="Arial 14"), sg.Text(self.docx.path, font="Arial 14", text_color="#000000", key="-DOCXPATH-")],
            [sg.Text("TABLE Path: ", font="Arial 14"), sg.Text(self.table.path, font="Arial 14", text_color="#000000", key="-TABLEPATH-")],
            [sg.Button("Edit", key="-EDIT-", button_color="#52b788"), sg.Button("Delete", key="-DELETE-", button_color="#e63946")],
            [sg.VPush()],
            [sg.VPush()],
            [sg.Push(), sg.Text("AUTO GENERATE:", font="Arial 16", text_color="#000000"), sg.Push()],
            [sg.VPush()],
            [sg.Push(), sg.Button("ALL", key="-ALL-"), sg.Button("SELECTED", key="-SEL-"), sg.Push()]

        ]

        window = sg.Window(f"{automation.upper()}").layout(layout)
        while True:
            event, _ = window.read(timeout=100)

            window["-DOCXPATH-"].update(xl.File(self.Config[self.section]["docx"]).path)
            window["-TABLEPATH-"].update(xl.File(self.Config[self.section]["table"]).path)

            if event == sg.WIN_CLOSED:
                break
            elif event == "-ALL-":
                Processes = xl.getAllProcesses(self.table)
                for process in Processes:
                    ctx = GenerateContext(process)
                    print(ctx)
                    GenerateFileFromDefaultDocx(ctx, self.docx)
                sg.popup_ok("Files Generated Sucessfully", title="Success!")
                break
            elif event == "-SEL-":
                pass #TODO: Implemet Select interface
            elif event == "-DELETE-":
                self.Config.remove_section(automation)
                with open(configFile, "w") as ConfigFile:
                    self.Config.write(ConfigFile)
                sg.popup_ok("Section Deleted Successfully!", title="Success")
                break
            elif event == "-EDIT-":
                self.edit_window()

        window.close()
    def edit_window(self):
        layout = [
            [sg.Push(), sg.Text("EDIT", font="Arial 18 bold", text_color="#000000"), sg.Push()],
            [sg.Text("DOCX: ", font="Arial 18 bold",), sg.Input(default_text=self.docx.path, key="-DOCXFILE-")],
            [sg.Text(self.docx.path, key="-ACTUALDOCXPATH-", font="Arial 16")],
            [sg.VPush()],
            [sg.Text("TABLE: ", font="Arial 18 bold", ), sg.Input(default_text=self.table.path, key="-TABLEFILE-")],
            [sg.Text(self.docx.path, key="-ACTUALTABLEPATH-", font="Arial 16")],
            [sg.VPush()],
            [sg.Push(), sg.Button("EDIT", key="-EDIT-", button_color="#52b788"), sg.Push()]
        ]

        edit_window = sg.Window("EDIT").layout(layout)
        while True:
            edit_event, edit_value = edit_window.read(timeout=100)
            if edit_value is not None:
                edit_window["-ACTUALDOCXPATH-"].update(edit_value["-DOCXFILE-"])
                edit_window["-ACTUALTABLEPATH-"].update(edit_value["-TABLEFILE-"])
            if edit_event == sg.WIN_CLOSED:
                break
            elif edit_event == "-EDIT-":
                self.Config.set(self.section, "docx", edit_value["-DOCXFILE-"])
                self.Config.set(self.section, "table", edit_value["-TABLEFILE-"])
                with open(configFile, "w") as ConfigFile:
                    self.Config.write(ConfigFile)
                    break
        edit_window.close()


class choose_automation_window:
    Config = conf
    def __init__(self):
        layout = [

            [sg.Push(), sg.Text("CHOOSE AUTOMATION"), sg.Push()],
            [sg.VPush()],
        ]

        sections = self.Config.sections()
        for sec in sections:
            semilayout = [sg.Push(), sg.Button(sec.upper(), size=(15,1), key=f"{sec}"), sg.Push()]
            layout.append(semilayout)

        layout.append([sg.VPush()])
        layout.append([sg.Cancel("LEAVE", key="-LEAVE-", button_color="#e63946")])

        window = sg.Window("Automations Available").layout(layout)

        while True:
            event, _  = window.Read()
            if event == sg.WIN_CLOSED or event == "-LEAVE-":
                break
            else:
                #TODO: Verify if exists
                automation = event
                automation_window(automation)
                continue
        window.close()


class new_automation_window:
    Config = conf
    section_available = False
    def __init__(self):
        layout = [
            [sg.Push(), sg.Text("CREATE A NEW AUTOMATION", font="Arial 20 bold", text_color="#000000"), sg.Push()],
            [sg.VPush()],
            [sg.Text("Give a name to the Automation: "), sg.Input(key="-AUTONAME-", default_text="Automation_name"), sg.Text(key="-AVAILABLE-")],
            [sg.VPush()],
            [sg.Text("Choose a docx template: "), sg.Button("(?)", size=(3,1), key="-DOCXDESC-")],
            [sg.FileBrowse(file_types=(('docx', '*.docx'),), key="-DOCXFILE-"), sg.Text(key="-DOCXRES-")],
            [sg.VPush()],
            [sg.Text("Choose a table template: "), sg.Button("(?)", size=(3, 1), key="-TABLEDESC-")],
            [sg.FileBrowse(file_types=(("xlsx", "*.xlsx"), ("csv", "*.csv"),), key="-TABLEFILE-"), sg.Text(key="-TABLERES-")],
            [sg.VPush()],
            [sg.VPush()],
            [sg.Push(), sg.Button("SUBMIT", key="-SUBMIT-", button_color="#aacc00"),sg.Push()]
        ]

        window = sg.Window("CREATE AUTOMATION").layout(layout)

        while True:
            event, value = window.Read(timeout=100)
            if value is not None and value["-AUTONAME-"] is not None:
                sections = self.Config.sections()
                if value["-AUTONAME-"] not in sections:
                    window["-AVAILABLE-"].update("AVAILABLE")
                    self.section_available = True
                else:
                    window["-AVAILABLE-"].update("NOT AVAILABLE")
                    self.section_available = False

            if event == sg.WIN_CLOSED:
                break
            if event == "-DOCXDESC-":
                sg.popup("This file MUST be of DOCX extension\n Also, the document MUST contain the automation keys written in the document text.\n\n Automation Keys Ex.: {{automation_key_name}}", title="Document Description", font="Arial 14", text_color="#000000")
            if event == "-TABLEDESC-":
                sg.popup("This file MUST be a information table - literally, as a XLSX file - or a simpler one as a CSV.\n No other extension supported.\n\n Be Sure every header is correctly written avoinding any spaces within the header's name.", title="Table Description", font="Arial 14", text_color="#000000")
            if event == "-SUBMIT-":
                if value is not None:
                    if value["-DOCXFILE-"] != "" and value["-TABLEFILE-"] != '' and self.section_available:
                        docx = xl.File(value["-DOCXFILE-"])
                        table = xl.File(value["-TABLEFILE-"])
                        self.submit(value["-AUTONAME-"],docx, table)
                        resp = sg.popup_ok_cancel("Do you want to stay in this page?", title="Confirmation Window",  font="Arial 14", text_color="#000000")
                        if resp == "OK":
                            continue
                        else:
                            break

        window.Close()
    def submit(self,automation:str, docx:xl.File, table:xl.File):
        answer = sg.popup_ok_cancel("Are you sure you want to save this automation?", title="Confirmation Window", font="Arial 14", text_color="#000000")
        if answer == "OK":
            self.Config.add_section(automation)
            self.Config.set(automation, "docx", docx.path)
            self.Config.set(automation, "table", table.path)
            with open(configFile, "w") as ConfigFile:
                self.Config.write(ConfigFile)
        elif answer == "CANCEL":
            return
        else:
            raise InterruptedError



class main_window:
    def __init__(self):
        layout =  [

            [sg.Push(), sg.Text("LITTY", font="Times 20 bold", text_color="#000000"), sg.Push()],
            [sg.Push(), sg.Text("De Luiz ltda.'s Application to create automatic files", font="Arial 14 italic", text_color="#000000"), sg.Push()],
            [sg.VPush()],
            [sg.Push(), sg.Button("New automation", key="-NEW-", size=(22,1), font="Arial 16"), sg.Push()],
            [sg.Push(), sg.Button("Choose a automation", key="-CHOOSE-", size=(22, 1),font="Arial 16"), sg.Push()],
            [sg.Push(), sg.Cancel("LEAVE", key="-LEAVE-", button_color="#e63946"), sg.Push()],

        ]

        self.window = sg.Window("LITTY").layout(layout)

    def open(self):
        while True:
            event, _ = self.window.read()
            print(event)
            if event == sg.WIN_CLOSED or event == "-LEAVE-":
                break
            elif event == "-NEW-":
                new_automation_window()
            elif event == "-CHOOSE-":
                choose_automation_window()
        self.window.close()
        return

if __name__ == "__main__":
    IsLogged = LOGIN()
    if IsLogged:
        main = main_window()
        main.open()
        files = filem.track()
        if files is None or len(files) == 0:
            exit()
        dirpath = filem.makefile(files)
        filem.ZipAndClose(dirpath)
    else:
        exit()

