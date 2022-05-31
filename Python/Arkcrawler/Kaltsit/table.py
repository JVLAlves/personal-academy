from pprint import *
import PySimpleGUI as sg
from Amiya import Getpic, myScreen
import arknomicon as ark
import webbrowser

class ConfirmationPopup:
    def __init__(self, text: str = "VOCÊ TEM CERTEZA?"):
        layout = [
            [sg.Text(f"{text}")],
            [sg.Button("SIM", key="confirm", button_color="#80b918", font=f"Arial {int(10 * (myScreen().width / 1000))}"),
             sg.Button("NÃO", key="deny", button_color="#c71f37", font=f"Arial {int(10 * (myScreen().width / 1000))}")]
        ]
        self.window = sg.Window("CONFIRMAÇÃO", layout, modal=True)

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
    def __init__(self, operator: dict):
        self.operator = operator
        if operator is None:
            sg.popup_error("Para visualizar a informação 'Total Pago' atualizada, acesse o arquivo Excel.",
                           title="Arquivo desatualizado.")
        button_size = (8, 1)
        """
        Status_col = [
            [sg.Text("STATUS:", font=f"Arial {int(10 * (myScreen().width / 1000))}", text_color="#000000")],
            [sg.Button("BASE", key="-BASE-", font=f"Arial {int(10 * (myScreen().width / 1000))}", size=button_size)],
            [sg.Button("E1", key="-E1-", font=f"Arial {int(10 * (myScreen().width / 1000))}", size=button_size)],
            [sg.Button("E2", key="-E2-", font=f"Arial {int(10 * (myScreen().width / 1000))}", size=button_size)],
        ]

        other_col = [
            [sg.Text("OTHER:", font=f"Arial {int(10 * (myScreen().width / 1000))}", text_color="#000000")],
            [sg.Button("SKILLS", key="-SKILLS-", font=f"Arial {int(10 * (myScreen().width / 1000))}", size=button_size)],
            [sg.Button("OUTFITS", key="-OUTFITS-", font=f"Arial {int(10 * (myScreen().width / 1000))}", size=button_size)],
            [sg.Button("ON PAGE", key="-PAGE-", font=f"Arial {int(10 * (myScreen().width / 1000))}", size=button_size)]
        ]
        """

        layout = [
            [sg.Push(), sg.Text("OPERATOR: ", font=f"Arial {int(16 * (myScreen().width / 1000))} bold", text_color="#000000"),
             sg.Text(str(operator["name"]), key="name", font=f"Arial {int(16 * (myScreen().width / 1000))} bold",
                     text_color="#000000"), sg.Push()],
            [[sg.VPush(), sg.Push(), sg.Image(data=Getpic(operator["img"], factor=2.5)), sg.Push(), sg.VPush()]],
            [sg.VPush()],
            [sg.Push(), sg.Text("Type:", font=f"Arial {int(12 * (myScreen().width / 1000))}", text_color="#ffffff"),
             sg.Text(f"{str(operator['type'])}", key="-TYPE-", font=f"Arial {int(12 * (myScreen().width / 1000))}",
                     text_color="#000000"),
             sg.Text(" | ", font=f"Arial {int(12 * (myScreen().width / 1000))}", text_color="#000000"),
             sg.Text("Archetype:", font=f"Arial {int(12 * (myScreen().width / 1000))}", text_color="#ffffff"),
             sg.Text(f"{str(operator['archetype'])}", key="-ARC-", font=f"Arial {int(12 * (myScreen().width / 1000))}",
                     text_color="#000000"), sg.Push()],
            [sg.VPush()],
            [sg.VPush()],
            [sg.Push(), sg.Text("STATUS", font=f"Arial {int(10 * (myScreen().width / 1000))}"), sg.Push()],
            [sg.Push(), sg.Button("BASE", key="-BASE-", font=f"Arial {int(10 * (myScreen().width / 1000))}", size=button_size),
             sg.Button("E1", key="-E1-", font=f"Arial {int(10 * (myScreen().width / 1000))}", size=button_size),
             sg.Button("E2", key="-E2-", font=f"Arial {int(10 * (myScreen().width / 1000))}", size=button_size), sg.Push()],
            [sg.VPush()],
            [sg.Push(), sg.Text("OTHER", font=f"Arial {int(10 * (myScreen().width / 1000))}"), sg.Push()],
            [sg.Push(),
             sg.Button("SKILLS", key="-SKILLS-", font=f"Arial {int(10 * (myScreen().width / 1000))}", size=button_size),
             sg.Button("OUTFITS", key="-OUTFITS-", font=f"Arial {int(10 * (myScreen().width / 1000))}", size=button_size),
             sg.Button("ON PAGE", key="-PAGE-", font=f"Arial {int(10 * (myScreen().width / 1000))}", size=button_size),
             sg.Push()],
            [sg.VPush()],
            [sg.VPush()],
            [sg.Push(), sg.Text("DB ACTS:", font=f"Arial {int(12 * (myScreen().width / 1000))}"), sg.Push()],
            [sg.Push(),
             sg.Button("UPDATE", button_color="#ACD8AA", key="-UPDATE-", font=f"Arial {int(10 * (myScreen().width / 1000))}"),
             sg.Button("DELETE", button_color="#c71f37", key="-DELETE-", font=f"Arial {int(10 * (myScreen().width / 1000))}"),
             sg.Push()]
        ]

        self.info_window = sg.Window(f"{operator['name'].upper()}", layout, modal=True, icon="Operator.png")

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
                try:
                    self.SKILLS()
                except:
                    sg.popup_error("THIS OPERATOR HAVE NO SKILLS IN THE DATABASE")
                    continue
            elif event == "-OUTFITS-":
                try:
                    self.OUTFITS()
                except:
                    sg.popup_error("THIS OPERATOR HAVE NO OUTFITS IN THE DATABASE")
                    continue
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

    def STATUS(self, title: str, status: dict):
        layout = [
            [sg.Push(), sg.Text(f"{self.operator['name'].upper()} {title.upper()} STATUS",
                                font=f"Arial {int(16 * (myScreen().width / 1000))} bold", text_color="#000000"), sg.Push()],
            [sg.Text(f"HP: {status['hp']}", font=f"Arial {int(12 * (myScreen().width / 1000))}", text_color="#000000")],
            [sg.Text(f"ATK: {status['atk']}", font=f"Arial {int(12 * (myScreen().width / 1000))}", text_color="#000000")],
            [sg.Text(f"DEF: {status['def']}", font=f"Arial {int(12 * (myScreen().width / 1000))}", text_color="#000000")],
            [sg.Text(f"DP COST: {status['dp_cost']}", font=f"Arial {int(12 * (myScreen().width / 1000))}",
                     text_color="#000000")],
        ]

        window = sg.Window(f"{self.operator['name'].upper()} {title.upper()} STATUS", icon="Operator.png").layout(
            layout)
        while True:
            event, _ = window.read()
            if event == sg.WIN_CLOSED:
                break
        window.close()
        # TODO: Review SKILLS function - It is not working

    def SKILLS(self):
        MaxCount = len(self.operator['skills'].keys())
        print(MaxCount)
        count = 1
        layout = [[sg.Push(),
                   sg.Text(f"{self.operator['name'].upper()}'S SKILLS", font=f'Arial {int(14 * (myScreen().width / 1000))}',
                           text_color="#000000"), sg.Push()]]
        print(self.operator['skills'].values())
        for skill in self.operator['skills']:
            if count <= MaxCount:
                layout.append([sg.Push(), sg.Button(f"{skill}", key=f"-SKILL-{count}-",
                                                    font=f"Arial {int(10 * (myScreen().width / 1000))}"), sg.Push()])
            else:
                continue
            count += 1

        skills_window = sg.Window(f"{self.operator['name']} Skills", icon="Operator.png").layout(layout)
        while True:
            event, _ = skills_window.read()
            if event == sg.WIN_CLOSED:
                break
            elif event == "-SKILL-1-":
                key_one = self.operator["skills"].keys()[0]
                skill_one = [
                    [sg.Push(), sg.Text(f"NAME: {key_one}", font=f"Arial {int(16 * (myScreen().width / 1000))} bold"),
                     sg.Push()],
                    [sg.Text(f"SP Cost: {self.operator['skills'][key_one]['sp_cost']}",
                             font=f"Arial {int(12 * (myScreen().width / 1000))}")],
                    [sg.Text(f"Duration: {self.operator['skills'][key_one]['duration']}")],
                    [sg.VPush()],
                    [sg.Text(f"Description: {self.operator['skills'][key_one]['effect']}")]
                ]

                skill_one_window = sg.Window(f"{key_one}", icon="Operator.png").layout(skill_one)
                while True:
                    event, _ = skill_one_window.read()
                    if event == sg.WIN_CLOSED:
                        break
                skill_one_window.close()
            elif event == "-SKILL-2-":
                key_two = self.operator["skills"].keys()[1]
                skill_two = [
                    [sg.Push(), sg.Text(f"NAME: {key_two}", font=f"Arial {int(16 * (myScreen().width / 1000))} bold"),
                     sg.Push()],
                    [sg.Text(f"SP Cost: {self.operator['skills'][key_two]['sp_cost']}",
                             font=f"Arial {int(12 * (myScreen().width / 1000))}")],
                    [sg.Text(f"Duration: {self.operator['skills'][key_two]['duration']}")],
                    [sg.VPush()],
                    [sg.Text(f"Description: {self.operator['skills'][key_two]['effect']}")]
                ]

                skill_two_window = sg.Window(f"{key_two}", icon="Operator.png").layout(skill_two)
                while True:
                    event, _ = skill_two_window.read()
                    if event == sg.WIN_CLOSED:
                        break
                skill_two_window.close()
            elif event == "-SKILL-3-":
                key_three = self.operator["skills"].keys()[2]
                skill_three = [
                    [sg.Push(), sg.Text(f"NAME: {key_three}", font=f"Arial {int(16 * (myScreen().width / 1000))} bold"),
                     sg.Push()],
                    [sg.Text(f"SP Cost: {self.operator['skills'][key_three]['sp_cost']}",
                             font=f"Arial {int(12 * (myScreen().width / 1000))}")],
                    [sg.Text(f"Duration: {self.operator['skills'][key_three]['duration']}")],
                    [sg.VPush()],
                    [sg.Text(f"Description: {self.operator['skills'][key_three]['effect']}")]
                ]

                skill_three_window = sg.Window(f"{key_three}", icon="Operator.png").layout(skill_three)
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
            [sg.Push(),
             sg.Text(f"{self.operator['name'].upper()}'S OUTFITS", font=f"Arial {int(16 * (myScreen().width / 1000))} bold",
                     text_color="#000000"), sg.Push()],
            [sg.VPush()]
        ]

        for outfit in outfit_names:
            semilayout = [sg.Push(), sg.Button(f"{outfit}", font=f"Arial {int(10 * (myScreen().width / 1000))}"), sg.Push()]
            layout.append(semilayout)

        outfits_window = sg.Window(f"{self.operator['name'].upper()}'S OUTFITS", icon="Operator.png").layout(layout)

        while True:
            event, _ = outfits_window.read()
            print(event)
            if event == sg.WIN_CLOSED:
                break
            elif event in outfit_names:
                outfit_layout = [
                    [sg.Push(), sg.Text(f"{self.operator['name'].upper()}'S {event.upper()}",
                                        font=f"Arial {int(16 * (myScreen().width / 1000))} bold", text_color="#000000"),
                     sg.Push()],
                    [sg.Push(), sg.Image(Getpic(self.operator['outfits'][event]["img"], factor=1.5)), sg.Push()],
                    [sg.Push(), sg.Cancel("Leave"), sg.Push()]
                ]
                oper_outfit_window = sg.Window(f"{self.operator['name'].upper()}'S {event.upper()}",
                                               icon="Operator.png").layout(outfit_layout)
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
            [sg.Push(),
             sg.Text(f"UPDATE {self.operator['name'].upper()}", font=f"Arial {int(16 * (myScreen().width / 1000))}"),
             sg.Push()],
            [sg.VPush()],
            [sg.Text("Field: "),
             sg.Listbox(fields, key="-FIELD-", size=(8, 1), font=f"Times {int(12 * (myScreen().width / 1000))}")],
            [sg.Text("Value: "), sg.Input(key="-VALUE-")],
            [sg.VPush()],
            [sg.Push(), sg.Text("Preview:", font=f"Arial {int(14 * (myScreen().width / 1000))} bold"), sg.Push()],
            [sg.Text("", key="-PREVIEW-", font=f"Arial {int(12 * (myScreen().width / 1000))}")],
            [sg.VPush()],
            [sg.Button("UPDATE", button_color="#ACD8AA", key="-UPDATE-", font=f"Arial {int(10 * (myScreen().width / 1000))}")]
        ]

        update_window = sg.Window(f"UPDATE {self.operator['name'].upper()}", use_default_focus=False,
                                  icon="Operator.png").layout(update)
        previous_field = None
        while True:
            event, new_values = update_window.read(timeout=100)
            if event == sg.WINDOW_CLOSED:
                break
            if len(new_values["-FIELD-"]) != 0:
                field = self.operator[new_values["-FIELD-"][0]]
                if field != previous_field:
                    print(field)
                    update_window["-VALUE-"].update(field if field is not None else "")
                    previous_field = field
                else:
                    pass
            else:
                pass
            try:
                eval(new_values["-VALUE-"])
            except:
                update_window["-PREVIEW-"].update(new_values["-VALUE-"])
                pprint(new_values)
            else:
                update_window["-PREVIEW-"].update(pformat(eval(new_values["-VALUE-"])))
                pprint(new_values)

            if event == "-UPDATE-":
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
                keep = ConfirmationPopup("DESEJA PERMANECER?")
                keep_confirm = keep.alert()
                keep.window.close()
                if keep_confirm:
                    continue
                else:
                    break
        update_window.close()


def operators_data(name: str = ""):
    operators = ark.get_all_operator(operator=name.title())
    if operators is None:
        return []
    operators_data = []
    for operator in operators:
        operators_data.append([operator["name"], operator["type"], operator["archetype"],
                               len(operator["skills"]) if operator["skills"] is not None else 0,
                               len(operator["outfits"]) if operator["outfits"] is not None else 0, operator["url"],
                               operator])
    return operators_data


# TODO: Create a search bar or filter bar
def create():
    operator_data = operators_data()
    operator_headings = ["NAME", "TYPE", "ARCHETYPE", "SKILL COUNT", "OUTFITS COUNT", "URL"]
    layout = [
        [sg.Text("Search: ", font=f"Arial {int(14 * (myScreen().width / 1000))}"), sg.Input(key="-OPERATOR-")],
        [sg.Table(values=operator_data,
                  headings=operator_headings,
                  max_col_width=35,
                  auto_size_columns=True,
                  display_row_numbers=True,
                  justification='right',
                  num_rows=10,
                  enable_events=True,
                  key='-OPERATOR_TABLE-',
                  row_height=35, )]
    ]
    info_window = sg.Window("ALL OPERATORS", layout, icon="Kaltsitssmall.png")
    previous_data = operator_data
    while True:
        event, values = info_window.read(timeout=100)
        if event == sg.WINDOW_CLOSED:
            break
        operator_data = operators_data(values["-OPERATOR-"])
        if previous_data != operator_data:
            info_window["-OPERATOR_TABLE-"].update(operator_data)
            previous_data = operator_data
        else:
            pass

        if event == "-OPERATOR_TABLE-":
            try:
                values["-OPERATOR_TABLE-"][0]
            except:
                continue
            else:
                selected_row_index = values["-OPERATOR_TABLE-"][0]
            contect_info = operator_data[selected_row_index][-1]
            profile(contect_info)

    info_window.close()

    """
    {
        "farming_plan": {
                "1-7":{"runs":152, "sanity":9{int(12 * (myScreen().width / 1000))}},
                "JT8-2":{"runs":90, "sanity":1890},
                "9-10":{"runs":78, "sanity":{int(14 * (myScreen().width / 1000))}04},
                "S3-6":{"runs":76, "sanity":1{int(14 * (myScreen().width / 1000))}0},
                "S4-1":{"runs":52, "sanity":936},
                "7-10":{"runs":48, "sanity":864},
                "3-3":{"runs":43, "sanity":645},
                "9-6":{"runs":38, "sanity":684},
                "9-18":{"runs":34, "sanity":7{int(14 * (myScreen().width / 1000))}},
                "LS-5":{"runs":33, "sanity":990},
                "CE-5":{"runs":32, "sanity":960},
                "R8-11":{"runs":27, "sanity":567},
                "6-11":{"runs":27, "sanity":567},
                "3-2":{"runs":27, "sanity":405},
                "CA-5":{"runs":24, "sanity":720},
                "2-5":{"runs":22, "sanity":264},
                "AP-5":{"runs":13, "sanity":390},
                "PR-A-2":{"runs":{int(12 * (myScreen().width / 1000))}, "sanity":432},
                "7-4":{"runs":9, "sanity":{int(16 * (myScreen().width / 1000))}2},
                "PR-A-1":{"runs":8, "sanity":{int(14 * (myScreen().width / 1000))}4},
                "JT8-3":{"runs":7, "sanity":{int(12 * (myScreen().width / 1000))}6},
                "S3-4":{"runs":4, "sanity":60},
                "S3-2":{"runs":3, "sanity":45},
                "S2-8":{"runs":3, "sanity":36},
                "3-7":{"runs":3, "sanity":45},
                "S3-1":{"runs":2, "sanity":30},
                },
        "materials": {
            "farming_materials": {
                "medic_chip_pack": 6,
                "skill_summary_3":48,
                "compound_cutting_fluid":10,
                "semi-synthetic_solvent":11,
                "crystalline_component":{int(14 * (myScreen().width / 1000))},
                "incandescent_alloy":30,
                "coagulation_gel":30,
                "medic_chip": 4,
                "skill_summary_2":18,
                "RMA70-{int(12 * (myScreen().width / 1000))}":{int(16 * (myScreen().width / 1000))},
                "grindstone":{int(14 * (myScreen().width / 1000))},
                "manganese_ore":10,
                "loxic_kohl":13,
                "aketon":3,
                "oriron_cluster":{int(16 * (myScreen().width / 1000))},
                "sugar_pack":8,
                "polyester_pack":5,
                "integrated_device":26,
                "purchase_certificate":267,
                "skill_summary_1":8,
                "polyketon":3,
                "sugar":3
                "polyester":4,
                "device":3,
                "orirock_cube":190,
                "oriron_shard":5
            },
            "crafting_materials":{
                "crystalline_electronic_unit": 4,
                "medic_dualchip":3,
                "bipolar_nanoflake":4,
                "refined_solvent":7,
                "crystalline_circuit":7,
                "incandescent_alloy_block":7,
                "polymerized_gel":{int(16 * (myScreen().width / 1000))},
                "RMA70-24":3,
                "manganese_trihydrate":5,
                "white_horse_kohl":8,
                "optimized_device":7,
                "orirock_concentration":3,
                "orirock_cluster":38
            }
        }
    
    }
    
    """
