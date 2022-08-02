import os
from pprint import pprint

import PySimpleGUI as sg
import LITTY.cmd.mongo.mongo_automation_cmds as mg_auto
import LITTY.cmd.fileaction.excel as xl
import LITTY.cmd.fileaction.word as wd
from LITTY.cmd.obj.popup_interfaces import popup_download, popup_selector
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


        try:
            self.download_path = self.automation["download_path"]
            if self.download_path is None or self.download_path == "":
                raise Exception("Empty Field")
            elif not os.path.exists(self.download_path):
                raise FileNotFoundError
        except:
                pop_down = popup_download()
                self.download_path = pop_down.open()
                mg_auto.update_automation( {"name": automation_name, "created_by": currentUser},
                    {"name": automation_name, "created_by": currentUser, "download_path": self.download_path})


        layout = [
            [sg.Push(), sg.Text(f"{automation_name.upper()}", font="Arial 20 bold", text_color="#000000"), sg.Push()],
            [sg.VPush()],
            [sg.Text("DOCX Path: ", font="Arial 14"),
            sg.Text(self.docx, font="Arial 14", text_color="#000000", key="-DOCXPATH-")],
            [sg.Text("TABLE Path: ", font="Arial 14"),
            sg.Text(self.table, font="Arial 14", text_color="#000000", key="-TABLEPATH-")],
            [sg.Text("Download Path: ", font="Arial 14"),
            sg.Text(self.download_path, font="Arial 14", text_color="#000000", key="-DOWNPATH-")],
            [sg.Button("Edit", key="-EDIT-", button_color="#52b788"),
             sg.Button("Delete", key="-DELETE-", button_color="#e63946")],
            [sg.VPush()],
            [sg.VPush()],
            [sg.Push(), sg.Text("AUTO GENERATE:", font="Arial 16", text_color="#000000"), sg.Push()],
            [sg.VPush()],
            [sg.Push(), sg.Button("ALL", key="-ALL-"), sg.Button("SELECTED", key="-SEL-"), sg.Push()]

        ]

        window = sg.Window(f"{automation_name.upper()}").layout(layout)
        automation_info = mg_auto.get_automation(automation_name)


        try:
            docx_content = automation_info["docx"]["content"]
            tbl_content = automation_info["tbl"]["content"]
        except:
            raise DatabaseOutOfDateError

        docx_file = xl.File(automation_info["docx"]["initial_path"])
        tbl_file = xl.File(automation_info["tbl"]["initial_path"])

        # write the bytes of the docx file in the download_path
        self.out_docx_path = self.download_path + f"/{docx_file.file}"
        out_docx = open(self.out_docx_path, "wb")
        out_docx.write(docx_content)
        out_docx_file = xl.File(self.out_docx_path)

        # write the bytes of the table file in the download_path
        self.out_tbl_path = self.download_path + f"/{tbl_file.file}"
        out_tbl = open(self.out_tbl_path, "wb")
        out_tbl.write(tbl_content)
        out_tbl_file = xl.File(self.out_tbl_path)

        while True:
            event, _ = window.read(timeout=100)

            window["-DOCXPATH-"].update(self.automation["docx"]["initial_path"])
            window["-TABLEPATH-"].update(self.automation["tbl"]["initial_path"])
            window["-DOWNPATH-"].update(self.automation["download_path"])

            if event == sg.WIN_CLOSED:
                break
            elif event == "-ALL-":
                if automation_info["tbl"]["orientation"] == "vertical":
                    GenerateContext = xl.CreateContextGenerator(out_tbl_file, True)
                    context = GenerateContext()
                    pprint(context)
                    wd.GenerateFileFromDefaultDocx(context[0], out_docx_file, self.download_path)
                else:
                    GenerateContext = xl.CreateContextGenerator(out_tbl_file)
                    print(out_tbl_file.DF)
                    ContextList = GenerateContext()
                    itercounter = 1
                    for context in ContextList:
                        pprint(context)
                        wd.GenerateFileFromDefaultDocx(context, out_docx_file, self.download_path, itercounter)
                        itercounter+= 1

                files = zip.track(self.download_path)
                if files is None or len(files) == 0:
                    exit()
                dirpath = zip.makefile(files, self.download_path)
                print(dirpath)
                zip.ZipAndClose(dirpath, automation_name)

                #delete the transcrypted files
                os.remove(self.out_docx_path)
                os.remove(self.out_tbl_path)

                sg.popup_notify("Files Generated Sucessfully", title="Success!")
                break
            elif event == "-SEL-":
                if automation_info["tbl"]["orientation"] == "vertical":
                    GenerateContext = xl.CreateContextGenerator(out_tbl_file, True)
                    context = GenerateContext()[0]
                    context_elements_lists = []
                    for k, v in context.items():
                        if isinstance(v, list):
                            context_elements_lists.append({k:v})

                    selector = popup_selector(context_elements_lists)
                    overall_context = selector.open()
                    context.update(overall_context)
                    print(context)


                    wd.GenerateFileFromDefaultDocx(context, out_docx_file, self.download_path)

                    files = zip.track(self.download_path)
                    if files is None or len(files) == 0:
                        exit()
                    dirpath = zip.makefile(files, self.download_path)
                    print(dirpath)
                    zip.ZipAndClose(dirpath, automation_name)

                    # delete the transcrypted files
                    os.remove(self.out_docx_path)
                    os.remove(self.out_tbl_path)
                else:
                    pass

            elif event == "-DELETE-":
                mg_auto.delete_automation({"name": automation_name, "created_by": currentUser})
                sg.popup_notify("Section Deleted Successfully!", title="Success")
                break
            elif event == "-EDIT-":
                self.edit_window()
                break

        window.close()

    def edit_window(self):
        layout = [
            [sg.Push(), sg.Text("EDIT", font="Arial 18 bold", text_color="#000000"), sg.Push()],
            [sg.FileBrowse(file_types=[("docx", "*.docx")], initial_folder=os.path.dirname(self.docx), key="-DOCXFILE-", tooltip="This file must be a Microsoft Word .docx tagged file. It will be used to automatic generate files from the data in the table."), sg.Text("DOCX: ", font="Arial 18 bold")],
            [sg.VPush()],
            [sg.FileBrowse(file_types=[("xlsx", "*.xlsx"), ("csv", "*.csv")],initial_folder=os.path.dirname(self.table), key="-TABLEFILE-", tooltip="This file must be a Microsoft Excel .xlsx table or a .csv file. This file must contain the data for the automation."), sg.Text("TABLE: ", font="Arial 18 bold")],
            [sg.Radio("Vertical", "TablePosition", key="vertical"),
            sg.Radio("Horizontal", "TablePosition", default=True, key="horizontal")],
            [sg.VPush()],
            [sg.FolderBrowse(key="-DOWNPATH-", initial_folder=os.path.dirname(self.download_path),
                                        tooltip="This must be the folder in which you want your file to be downloaded."), sg.Text("DOWNLOAD: ", font="Arial 18 bold", )],
            [sg.VPush()],
            [sg.Push(), sg.Button("EDIT", key="-EDIT-", button_color="#52b788"), sg.Push()]
        ]

        edit_window = sg.Window("EDIT").layout(layout)
        while True:
            edit_event, edit_value = edit_window.read(timeout=100)
            if edit_event == sg.WIN_CLOSED:
                os.remove(self.out_docx_path)
                os.remove(self.out_tbl_path)
                break
            elif edit_event == "-EDIT-":

                docx = edit_value["-DOCXFILE-"]
                docx_file = open(docx, "rb")
                docx_content = docx_file.read()

                table = edit_value["-TABLEFILE-"]
                tbl_file = open(table, "rb")
                tbl_content = tbl_file.read()

                orientation = None
                if edit_value["vertical"]:
                    orientation = "vertical"
                elif edit_value["horizontal"]:
                    orientation = "horizontal"

                mg_auto.update_automation(

                    #query - existent one
                    {
                        "name":self.automation["name"],
                        "created_by":self.automation["created_by"]
                    },

                    #update - new one
                    {
                        "name":self.automation["name"],
                        "created_by":self.automation["created_by"],
                        "docx":
                            {
                                "initial_path":docx,
                                "content":docx_content
                            },
                        "tbl":
                            {
                                "initial_path": table,
                                "content":tbl_content,
                                "orientation": orientation
                            },
                        "download_path":edit_value["-DOWNPATH-"]
                    }
                )

                sg.popup_notify("Automation Updated Sucessfully", title="Success!")


                break
        edit_window.close()


