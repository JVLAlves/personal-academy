from pprint import *
from images.imgs import *
import PySimpleGUI as sg
from cmd2.Amiya.Amiya import Getpic
import arknomicon as ark
import webbrowser
class ConfirmationPopup:
    def __init__(self):
        layout = [
            [sg.Text("VOCÊ TEM CERTEZA?")],
            [sg.Button("SIM", key="confirm", button_color="#80b918"), sg.Button("NÃO", key="deny", button_color="#c71f37")]
        ]
        self.window = sg.Window("CONFIRMAÇÃO",layout,modal=True)

    def alert(self):
        while True:
            event, _ = self.window.Read()
            if event == "confirm":
                return True
            elif event == sg.WINDOW_CLOSED or event == "deny":
                return False
            else:
                sg.popup_error("ERRO AO CONFIRMAR")


class profile:
    def __init__(self, operator:dict):
        self.operator = operator
        if operator is None:
            sg.popup_error("Para visualizar a informação 'Total Pago' atualizada, acesse o arquivo Excel.", title="Arquivo desatualizado.")
        layout = [
            [sg.Push(), sg.Text("OPERATOR: ", font="Arial 16 bold", text_color="#000000"), sg.Text(str(operator["name"]), key="name", font="Arial 16 bold", text_color="#000000"), sg.Push()],
            [[sg.VPush(), sg.Push(), sg.Image(data=Getpic(operator["img"], basewidth=400)), sg.Push(), sg.VPush()]],
            [sg.VPush()],
            [sg.Text("type:", font="Arial 14", text_color="#ffffff"), sg.Text(f"{str(operator['type'])}",key="-TYPE-", font="Arial 14", text_color="#000000")],
            [sg.Text("Archetype:", font="Arial 14", text_color="#ffffff"), sg.Text(f"{str(operator['archetype'])}",key="-ARC-", font="Arial 14", text_color="#000000")],
            [sg.Text("\n")],
            [sg.Text("STATUS:", font="Arial 14", text_color="#000000")],
            [sg.Button("BASE", key="-BASE-")],
            [sg.Button("E1", key="-E1-")],
            [sg.Button("E2", key="-E2-")],
            [sg.VPush()],
            [sg.Text("OTHER:", font="Arial 14", text_color="#000000")],
            [sg.Button("SKILLS", key="-SKILLS-"), sg.Button("OUTFITS", key="-OUTFITS-"), sg.Button("ON PAGE", key="-PAGE-")],
            [sg.VPush(), sg.Text("DB ACTS:")],
            [sg.Button("UPDATE", button_color="#ACD8AA", key="-UPDATE-"), sg.Button("DELETE", button_color="#c71f37", key="-DELETE-")]
        ]

        self.info_window = sg.Window(f"{operator['name'].upper()}", layout, modal=True, icon=operator_icon)

        while True:
            event, values = self.info_window.read()
            if event == sg.WINDOW_CLOSED:
                break
            elif event == "-BASE-":
                self.STATUS("base", self.operator["stats"]["base"])
            elif event == "-E1-":
                if self.operator["stats"]["elite_one"] != None:
                    self.STATUS("Elite 1", self.operator["stats"]["elite_one"])
                else:
                    sg.popup_error("this operator doesnt have a Elite 1")
                    continue
            elif event == "-E2-":
                if self.operator["stats"]["elite_two"] != None:
                    self.STATUS("Elite 2", self.operator["stats"]["elite_two"])
                else:
                    sg.popup_error("this operator doesnt have a Elite 2")
                    continue
            elif event == "-SKILLS-":
                self.SKILLS()
            elif event == "-OUTFITS-":
                self.OUTFITS()
            elif event == "-PAGE-":
                if self.operator["url"] is not None:
                    webbrowser.open(self.operator["url"])
                else:
                    sg.popup_error("There is no url for this Operator.")
            elif event == "-UPDATE-":
                self.UPDATE()
            elif event == "-DELETE-":
                popup = ConfirmationPopup()
                confirm = popup.alert()
                popup.window.close()
                if confirm:
                    print(f"{self.operator['name']} is going to be deleted.")
                    ark.delete_operator(self.operator)
                    break
        self.info_window.close()
    def STATUS(self, title:str, status:dict):
        layout = [
            [sg.Push(), sg.Text(f"{self.operator['name'].upper()} {title.upper()} STATUS", font="Arial 16 bold", text_color="#000000"), sg.Push()],
            [sg.Text(f"HP: {status['hp']}", font="Arial 12", text_color="#000000")],
            [sg.Text(f"ATK: {status['atk']}", font="Arial 12", text_color="#000000")],
            [sg.Text(f"DEF: {status['def']}", font="Arial 12", text_color="#000000")],
            [sg.Text(f"DP COST: {status['dp_cost']}", font="Arial 12", text_color="#000000")],
        ]

        window = sg.Window(f"{self.operator['name'].upper()} {title.upper()} STATUS", icon=operator_icon).layout(layout)
        while True:
            event, _ = window.read()
            if event == sg.WIN_CLOSED:
                break
        window.close()
    def SKILLS(self):
        MaxCount = len(self.operator['skills'].keys())
        count = 1
        layout = [[sg.Text("SKILLS")]]
        for skill in self.operator['skills']:
            if count < MaxCount:
                layout.append(sg.Button(f"{skill}", key=f"-SKILL-{count}-"))
            else:
                break

        skills_window = sg.Window(f"{self.operator['name']} Skills", icon=operator_icon).layout(layout)
        while True:
            event, _ = skills_window.read()
            if event == sg.WIN_CLOSED:
                break
            elif event == "-SKILL-1-":
                key_one = self.operator["skills"].keys()[0]
                skill_one =[
                    [sg.Push(), sg.Text(f"NAME: {key_one}", font="Arial 16 bold"), sg.Push()],
                    [sg.Text(f"SP Cost: {self.operator['skills'][key_one]['sp_cost']}", font="Arial 12")],
                    [sg.Text(f"Duration: {self.operator['skills'][key_one]['duration']}")],
                    [sg.VPush()],
                    [sg.Text(f"Description: {self.operator['skills'][key_one]['effect']}")]
                ]

                skill_one_window = sg.Window(f"{key_one}", icon=operator_icon).layout(skill_one)
                while True:
                    event, _ = skill_one_window.read()
                    if event == sg.WIN_CLOSED:
                        break
                skill_one_window.close()
            elif event == "-SKILL-2-":
                key_two = self.operator["skills"].keys()[1]
                skill_two = [
                    [sg.Push(), sg.Text(f"NAME: {key_two}", font="Arial 16 bold"), sg.Push()],
                    [sg.Text(f"SP Cost: {self.operator['skills'][key_two]['sp_cost']}", font="Arial 12")],
                    [sg.Text(f"Duration: {self.operator['skills'][key_two]['duration']}")],
                    [sg.VPush()],
                    [sg.Text(f"Description: {self.operator['skills'][key_two]['effect']}")]
                ]

                skill_two_window = sg.Window(f"{key_two}", icon=operator_icon).layout(skill_two)
                while True:
                    event, _ = skill_two_window.read()
                    if event == sg.WIN_CLOSED:
                        break
                skill_two_window.close()
            elif event == "-SKILL-3-":
                key_three = self.operator["skills"].keys()[2]
                skill_three = [
                    [sg.Push(), sg.Text(f"NAME: {key_three}", font="Arial 16 bold"), sg.Push()],
                    [sg.Text(f"SP Cost: {self.operator['skills'][key_three]['sp_cost']}", font="Arial 12")],
                    [sg.Text(f"Duration: {self.operator['skills'][key_three]['duration']}")],
                    [sg.VPush()],
                    [sg.Text(f"Description: {self.operator['skills'][key_three]['effect']}")]
                ]

                skill_three_window = sg.Window(f"{key_three}", icon=operator_icon).layout(skill_three)
                while True:
                    event, _ = skill_three_window.read()
                    if event == sg.WIN_CLOSED:
                        break
                skill_three_window.close()
        skills_window.close()

    def OUTFITS(self):
        self.info_window.close()
        outfit_names = list(self.operator['outfits'].keys())
        print(outfit_names)
        layout = [
            [sg.Push(), sg.Text(f"{self.operator['name'].upper()}'S OUTFITS", font="Arial 16 bold", text_color="#000000"), sg.Push()],
            [sg.VPush()]
        ]

        for outfit in outfit_names:
            semilayout = [sg.Push(), sg.Button(f"{outfit.title()}"),sg.Push()]
            layout.append(semilayout)

        outfits_window = sg.Window(f"{self.operator['name'].upper()}'S OUTFITS", icon=operator_icon).layout(layout)

        while True:
            event, _ = outfits_window.read()
            print(event)
            if event == sg.WIN_CLOSED:
                break
            elif event in outfit_names:
                outfit_layout = [
                    [sg.Push(), sg.Text(f"{self.operator['name'].upper()}'S {event.upper()}",font="Arial 16 bold", text_color="#000000"), sg.Push()],
                    [sg.Push(), sg.Image(Getpic(self.operator['outfits'][event]["img"], 1000)), sg.Push()],
                    [sg.Push(), sg.Cancel("Leave"), sg.Push()]
                ]
                oper_outfit_window = sg.Window(f"{self.operator['name'].upper()}'S {event.upper()}", icon=operator_icon).layout(outfit_layout)
                while True:
                    second_event, _ = oper_outfit_window.read()
                    if second_event == sg.WIN_CLOSED or second_event == "Leave":
                        break
                oper_outfit_window.close()
        outfits_window.close()


    def UPDATE(self):
        self.info_window.close()
        fields = list(self.operator.keys())
        fields.remove("name")
        fields.remove("_id")
        print(fields)
        update = [
            [sg.Push(), sg.Text(f"UPDATE {self.operator['name'].upper()}", font="Arial 16"), sg.Push()],
            [sg.VPush()],
            [sg.Text("Field: "), sg.Listbox(fields, key="-FIELD-", size=(8,1), font="Times 12")],
            [sg.Text("Value: "), sg.Input(key="-VALUE-")],
            [sg.VPush()],
            [sg.Push(), sg.Text("Preview:", font="Arial 14 bold"), sg.Push()],
            [sg.Text("", key="-PREVIEW-", font="Arial 12")],
            [sg.VPush()],
            [sg.Button("UPDATE", button_color="#ACD8AA", key="-UPDATE-")]
        ]

        update_window = sg.Window(f"UPDATE {self.operator['name'].upper() }", use_default_focus=False, icon=operator_icon).layout(update)
        while True:
            event, new_values = update_window.read(timeout=100)
            try:
                eval(new_values["-VALUE-"])
            except:
                continue
            else:
                update_window["-PREVIEW-"].update(pformat(eval(new_values["-VALUE-"])))
                pprint(new_values)
            if event == sg.WIN_CLOSED:
                break
            elif event == "-UPDATE-":
                if len(new_values["-FIELD-"]) == 0 or new_values["-FIELD-"] is None:
                    continue
                else:
                    new_values["-FIELD-"] = new_values["-FIELD-"][0]

                updated_operator = self.operator
                try:
                    eval(new_values["-VALUE-"])
                except:
                    pass
                else:
                    new_values["-VALUE-"] = eval(new_values["-VALUE-"])
                updated_operator[new_values["-FIELD-"]] = new_values["-VALUE-"]
                popup = ConfirmationPopup()
                confirm = popup.alert()
                popup.window.close()
                if confirm:
                    ark.update_operator(updated_operator)
                    sg.popup(f"Operator {self.operator['name']} updated")
                    pprint(f"UPDATED: {updated_operator}\n\nPREVIOUS: {self.operator}")
                keep = ConfirmationPopup()
                keep_confirm = keep.alert()
                keep.window.close()
                if keep_confirm:
                    continue
                else:
                    break
        update_window.close()


def create( info_array:list, headings:list, name:str="ALL OPERATORS"):
    layout=[
        [sg.Table(values=info_array,
        headings=headings,
        max_col_width=35,
        auto_size_columns=True,
        display_row_numbers=True,
        justification='right',
        num_rows=10,
        enable_events=True,
        key='-OPERATOR_TABLE-',
        row_height=35,)]
    ]
    info_window = sg.Window(name, layout, icon=kaltsit_application_icon)

    while True:
        event, values = info_window.read()
        if event == sg.WINDOW_CLOSED:
            break
        if event == "-OPERATOR_TABLE-":
            selected_row_index = values["-OPERATOR_TABLE-"][0]
            contect_info = info_array[selected_row_index][-1]
            profile(contect_info)

    info_window.close()