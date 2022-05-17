import arknomicon as ark
import PySimpleGUI as sg
import table as tbl
from images.imgs import *

class create_field:

    def __init__(self):
        layout = [
            [sg.Push(), sg.Text("Create New Field", font="Arial 16 bold", text_color="#000000"), sg.Push()],
            [sg.VPush(), sg.Text("field name: "), sg.Input(key="-NAME-"), sg.Push()],
            [sg.Text("default value: "), sg.Input(key="-DEFAULT-"), sg.Push()],
            [sg.VPush()],
            [sg.Push(), sg.Button("ADD"), sg.Push()]

        ]

        self.window = sg.Window("create field", icon=kaltsit_application_icon).layout(layout)

    def open(self):
        while True:
            event, values = self.window.read()
            if event == sg.WIN_CLOSED:
                break
            elif event == "ADD":
                field_name = values["-NAME-"]
                try:
                    true_data = eval(values["-DEFAULT-"])
                except:
                    if values["-DEFAULT-"] != "":
                        default_value = values["-DEFAULT-"]
                    else:
                        default_value = None
                else:
                    default_value = true_data
                ark.add_field(field_name.lower(), default_value=default_value)
                sg.popup(f"field named {field_name.lower()} added")
        self.window.close()

class main:
    def __init__(self):
        layout = [
            [sg.Push(), sg.Text("Kal'tsit Clipboard HUB", font="Arial 16 bold", text_color="#000000"), sg.Push()],
            [sg.Button("add field", key="-FIELD-"), sg.Button("add operator", key="-OPER-"), sg.Button("see all", key="-ALL-")],
            [sg.Push(), sg.Cancel("Leave"), sg.Push()]
        ]

        self.window = sg.Window("KC HUB", icon=kaltsit_application_icon).layout(layout)

    def open(self):
        while True:
            event, _ = self.window.read()
            if event == sg.WIN_CLOSED or event == "Leave":
                break
            elif event == "-FIELD-":
                field = create_field()
                field.open()
            elif event == "-OPER-":
                pass
            elif event == "-ALL-":
                operators = ark.get_all_operator()
                operators_data = []
                for operator in operators:
                    operators_data.append([operator["name"], operator["type"], operator["archetype"], len(operator["skills"]) if operator["skills"] is not None else 0, len(operator["outfits"]) if operator["outfits"] is not None else 0, operator["url"], operator])
                operator_headings = ["NAME", "TYPE", "ARCHETYPE", "SKILL COUNT", "OUTFITS COUNT", "URL"]
                tbl.create(operators_data, operator_headings)
        exit()



if __name__ == "__main__":
    main = main()
    main.open()





