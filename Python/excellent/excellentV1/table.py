import PySimpleGUI as sg
from excellentV1 import exConsts as ex
from excellentV1 import excel as xl
from excellentV1 import confighelpers as cf

config = cf.init()

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
    FILE = config['account']['default_filepath']
    def __init__(self, pacient:list):
        if pacient[3] is None:
            sg.popup_error("Para visualizar a informação 'Total Pago' atualizada, acesse o arquivo Excel.", title="Arquivo desatualizado.")
        layout = [
            [sg.Text("INFORMAÇÕES:",size=15)],
            [sg.Text("Nome: "), sg.Text(str(pacient[1]), key="name")],
            [sg.Text("Célula no Excel: "), sg.Text(pacient[0],key="cell")],
            [sg.Text("Valor por Sessão (R$):"), sg.Text(str(pacient[2]),key="value_per_session")],
            [sg.Text("Total pago (R$): "), sg.Text(str(pacient[3]),key="total")],
            [sg.Text("\n")],
            [sg.Text("OUTROS:", size=15)],
            [sg.Listbox(values=ex.GetMonths(), size=(10, 1), key="month",),sg.Input(key="amount", size=(10,1)), sg.Button("Pagar", key="pay")],
            [sg.Button("Deletar Paciente", button_color="#c71f37", key="delete")]
        ]

        info_window = sg.Window("Perfil do Paciente", layout, modal=True)

        while True:
            event, values = info_window.read()
            if event == sg.WINDOW_CLOSED:
                break
            elif event == "pay":
                if values["amount"] is None or values["amount"] == '':
                    if values["month"] is None or values["month"] == []:
                        sg.popup_error("Marque o mês do pagamento antes de continuar.")
                        continue
                    xl.IncrementPayment(pacient[1], pacient[2], values["month"], self.FILE)
                    sg.popup("Pagamento realizado com sucesso!")
                else:
                    if values["month"] is None or values["month"] == []:
                        sg.popup_error("Marque o mês do pagamento antes de continuar.")
                        continue
                    xl.IncrementPayment(pacient[1], values["amount"], values["month"], self.FILE)
                    sg.popup("Pagamento realizado com sucesso!")
            elif event == "delete":
                popup = ConfirmationPopup()
                confirm = popup.alert()
                popup.window.close()
                if confirm:
                    xl.DeletePatient(pacient[1], self.FILE)
                    info_window.close()
                    sg.popup("PACIENTE DELETADO!")






def create( info_array:list, headings:list, name:str="TABELA"):
    layout=[
        [sg.Table(values=info_array,
        headings=headings,
        max_col_width=35,
        auto_size_columns=True,
        display_row_numbers=True,
        justification='right',
        num_rows=10,
        enable_events=True,
        key='-CONTACT_TABLE-',
        row_height=35,)]
    ]
    info_window = sg.Window(name, layout)

    while True:
        event, values = info_window.read()
        if event == sg.WINDOW_CLOSED:
            break
        if event == "-CONTACT_TABLE-":
            selected_row_index = values["-CONTACT_TABLE-"][0]
            contect_info = info_array[selected_row_index]
            pf_window = profile(contect_info)
            break

    info_window.close()