import os

import PySimpleGUI as sg
import LITTY.cmd.mongo.mongo_automation_cmds as mg_auto
import LITTY.cmd.fileaction.excel as xl
import LITTY.cmd.fileaction.word as wd
from LITTY.cmd.obj.popup_interfaces import popup_download
import LITTY.cmd.mongo.mongo_users_cmds as mg_users
from LITTY.glob.errors import DatabaseOutOfDateError
import LITTY.cmd.fileaction.zipper as zip


class automation_window:

    def __init__(self, automation_name: str, currentUser: str):
        auto = mg_auto.query_automation({"name": automation_name, "created_by": currentUser})
        user = mg_users.get_user(currentUser)

        #TODO: If the path moved location, it will be an error. Fix it
        self.download_path = user["download_folder"]
        self.automation = auto[0]

        try:
            self.docx = self.automation["docx"]
            self.table = self.automation["tbl"]
        except:
            raise DatabaseOutOfDateError(automation_name)
        else:
            self.docx = self.automation["docx"]["initial_path"]
            self.table = self.automation["tbl"]["initial_path"]

        layout = [
            [sg.Push(), sg.Text(f"{automation_name.upper()}", font="Arial 20 bold", text_color="#000000"), sg.Push()],
            [sg.VPush()],
            [sg.Text("DOCX Path: ", font="Arial 14"),
             sg.Text(self.docx, font="Arial 14", text_color="#000000", key="-DOCXPATH-")],
            [sg.Text("TABLE Path: ", font="Arial 14"),
             sg.Text(self.table, font="Arial 14", text_color="#000000", key="-TABLEPATH-")],
            [sg.Button("Edit", key="-EDIT-", button_color="#52b788"),
             sg.Button("Delete", key="-DELETE-", button_color="#e63946")],
            [sg.VPush()],
            [sg.VPush()],
            [sg.Push(), sg.Text("AUTO GENERATE:", font="Arial 16", text_color="#000000"), sg.Push()],
            [sg.VPush()],
            [sg.Push(), sg.Button("ALL", key="-ALL-"), sg.Button("SELECTED", key="-SEL-"), sg.Push()]

        ]

        window = sg.Window(f"{automation_name.upper()}").layout(layout)

        pop_down = popup_download()
        while True:
            download_path = pop_down.open()
            if download_path is None:
                sg.popup_error("The download path must be declared.", title="Download path not found.")
                continue
            else:
                break

        automation_info = mg_auto.get_automation(automation_name)
        try:
            docx_content = automation_info["docx"]["content"]
            tbl_content = automation_info["tbl"]["content"]
        except:
            raise DatabaseOutOfDateError

        docx_file = xl.File(automation_info["docx"]["initial_path"])
        tbl_file = xl.File(automation_info["tbl"]["initial_path"])

        # write the bytes of the docx file in the download_path
        out_docx_path = download_path + f"/{docx_file.file}"
        out_docx = open(out_docx_path, "wb")
        out_docx.write(docx_content)

        # write the bytes of the table file in the download_path
        out_tbl_path = download_path + f"/{tbl_file.file}"
        out_tbl = open(out_tbl_path, "wb")
        out_tbl.write(tbl_content)

        while True:
            event, _ = window.read(timeout=100)

            window["-DOCXPATH-"].update(self.automation["docx"]["initial_path"])
            window["-TABLEPATH-"].update(self.automation["tbl"]["initial_path"])

            if event == sg.WIN_CLOSED:
                break
            elif event == "-ALL-":
                if automation_info["tbl"]["orientation"] == "vertical":
                    GenerateContext = xl.CreateContextGenerator(out_tbl_path, True)
                    context = GenerateContext()
                    wd.GenerateFileFromDefaultDocx(context, out_docx_path, download_path)
                else:
                    GenerateContext = xl.CreateContextGenerator(out_tbl_path)
                    ContextList = GenerateContext()
                    itercounter = 1
                    for context in ContextList:
                        wd.GenerateFileFromDefaultDocx(context, out_docx_path, download_path, itercounter)
                        itercounter+= 1

                files = zip.track(download_path)
                if files is None or len(files) == 0:
                    exit()
                dirpath = zip.makefile(files, download_path)
                zip.ZipAndClose(dirpath, automation_name)

                os.remove(out_docx_path)
                os.remove(out_tbl_path)

                sg.popup_notify("Files Generated Sucessfully", title="Success!")
                break
            elif event == "-SEL-":
                pass  # TODO: Implement Individual clients interface
            elif event == "-DELETE-":
                mg_auto.delete_automation({"name": automation_name, "created_by": currentUser})
                sg.popup_notify("Section Deleted Successfully!", title="Success")
                break
            elif event == "-EDIT-":
                self.edit_window()

        window.close()

    def edit_window(self):
        layout = [
            [sg.Push(), sg.Text("EDIT", font="Arial 18 bold", text_color="#000000"), sg.Push()],
            [sg.FileBrowse(file_types=[("docx", "*.docx")], key="-DOCXFILE-", tooltip="This file must be a Microsoft Word .docx tagged file. It will be used to automatic generate files from the data in the table."), sg.Text("DOCX: ", font="Arial 18 bold", )],
            [sg.VPush()],
            [sg.FileBrowse(file_types=[("xlsx", "*.xlsx"), ("csv", "*.csv")], key="-TABLEFILE-", tooltip="This file must be a Microsoft Excel .xlsx table or a .csv file. This file must contain the data for the automation."), sg.Text("TABLE: ", font="Arial 18 bold", )]
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
                # TODO: CREATE SET OR UPDATE ATTRIBUTE ON MONGO AUTOMATION PACKAGE
                # EDIT --> DOCX, TABLE

                mg_auto.update_automation(
                    {
                        "name":self.automation["name"],
                        "created_by":self.automation["created_by"],
                        "files":{
                            "default_file_path": self.docx,
                            "data_table_path": self.table,
                        }
                    },

                    {
                        "name": self.automation["name"],
                        "created_by": self.automation["created_by"],
                        "files": {
                            "default_file_path": edit_value["-DOCXFILE-"],
                            "data_table_path": edit_value["-TABLEFILE-"],
                        }
                    }
                )

                sg.popup_notify("Automation Updated Sucessfully", title="Success!")


                pass
        edit_window.close()


