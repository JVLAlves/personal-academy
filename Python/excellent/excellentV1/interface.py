import PySimpleGUI as sg
import excel as xl
import confighelpers as cf
from excellentV1 import table as tbl

config = cf.init()


class LoginWindow:
    STATUS = config['account']['status']
    USER = config['account']['user']
    PASSWORD = config['account']['password']
    THEME = config['account']['default_theme']

    def __init__(self):
        sg.theme(self.THEME)
        # layout
        self.layout_login = [
            [sg.Text("LOGIN")],
            [sg.Text("Usuário:"), sg.Input(key="user", size=(10,1))],
            [sg.Text("Senha:  "), sg.Input(key="password",size=(10,1), password_char='*')],
            [sg.Button("Login")]
        ]

        self.layout_register = [
            [sg.Text("REGISTRE-SE")],
            [sg.Text("Nome:  "), sg.Input(key="user", size=(18,1))],
            [sg.Text("Senha: "), sg.Input(key="password", size=(18,1))],
            [sg.Text("Tema:  "), sg.Input(default_text="Ex.: {}".format(sg.theme()), key="theme", size=(18,1)),
             sg.Button("Ver Temas", key="SearchThemes")],
            [sg.Button("Registrar", key="register")]
        ]

    def init(self):

        # Window
        if self.STATUS == "inactive":
            window = sg.Window("REGISTRO").layout(self.layout_register)
            self.window = window

            while True:
                self.event, self.value = self.window.read()
                if self.event == sg.WIN_CLOSED:
                    exit()
                elif self.event == "SearchThemes":
                    sg.theme_previewer()
                elif self.event == "register":
                    config.set("account", "user", self.value["user"])
                    config.set("account", "password", self.value["password"])
                    config.set("account", "status", "active")
                    config.set("account", "default_theme", self.value["theme"])
                    with open(cf.FILE, "w") as configFile:
                        config.write(configFile)
                    break
        elif self.STATUS == "active":
            window = sg.Window("LOGIN").layout(self.layout_login)
            self.window = window
            tries = 5
            while True:
                self.event, self.value = self.window.Read()
                if (self.value["user"] == self.USER) and (self.value["password"] == self.PASSWORD):
                    return True
                elif self.event == sg.WIN_CLOSED:
                    exit()
                else:
                    tries -= 1
                    if tries <= 0:
                        return False
                    sg.popup_error("SENHA OU LOGIN INCORRETO {}/5 tentativas".format(tries), title="ERRO",
                                   text_color="#ff0000")


class FileWindow:
    FILE = config['account']['default_filepath']
    if FILE is not None:
        splitFILE = FILE.split("/")
        splitFILE.pop(-1)
        FILE = "/".join(splitFILE) + "/"

    def __init__(self):
        login = LoginWindow()
        confirm = login.init()
        if not confirm:
            return
            # layout
        login.window.close()
        layout = [
            [sg.Text("IMPORTAÇÃO DA TABELA")],
            [sg.Text("Escolha um arquivo:")],
            [sg.FileBrowse(initial_folder=self.FILE, file_types=(("xlsx", "*.xlsx"), ("xlsm", "*.xlsm"), ("xltx", "*.xltx"), ("xltm", "*.xltm")))],
            [sg.Text("arquivo atual:"), sg.Text(str(self.FILE), key="-file-OUTPUT-")],
            [sg.Button("Enviar", key="send")]
        ]

        # Window

        self.window = sg.Window("importação da tabela").layout(layout)

    def init(self):
        while True:
            event, value = self.window.Read(timeout=100)
            if event == "send":
                if value["Browse"] != self.FILE and (value["Browse"] != '' and value["Browse"] is not None):
                    self.window["-file-OUTPUT-"].update(value["Browse"])
                    config.set("account", "default_filepath", value["Browse"])
                    with open(cf.FILE, "w") as configFile:
                        config.write(configFile)
                break
            elif event == sg.WIN_CLOSED:
                exit()
        self.window.close()


class ShowTableWindow:
    megalist = []
    FILE = config['account']['default_filepath']

    def __init__(self, name=''):
        self.megalist.clear()
        pat_ls = xl.SearchPatientByName(name, self.FILE)
        for pat in pat_ls:
            info = xl.SearchPatientByCell(pat['cll'], self.FILE)
            print(info)
            ls = list(info.values())
            self.megalist.append(ls)

        headings = ["CELL", "Paciente", "Valor por Sessão", "Total pago"]
        tbl.create(self.megalist, headings, "TODOS OS PACIENTES")


class AddPatWindow:
    FILE = config['account']['default_filepath']

    def __init__(self):
        # layout
        layout = [
            [sg.Text("ADICIONAR PACIENTE")],
            [sg.Text("Nome:", size=(17, 1)), sg.Input(key='addname', size=(20, 1), do_not_clear=False)],
            [sg.Text("Valor por Sessão:", size=(17, 1)),
             sg.Input(key="valuepersession", size=(20, 1), do_not_clear=False)],
            [sg.Button("Adicionar", key="add")]
        ]

        # window
        self.window = sg.Window("Adicionar Paciente").layout(layout)

    def init(self):
        while True:
            self.event, self.value = self.window.read()
            if self.event == sg.WIN_CLOSED:
                break
            elif self.event == "add":
                name = self.value["addname"].capitalize()
                sessionValue = self.value["valuepersession"]
                try:
                    xl.InsertPatient(name, sessionValue, self.FILE)
                except Exception as e:
                    sg.popup_error("ERRO AO TENTAR ADICIONAR PACIENTE.", e, title="ERRO!")
                else:
                    sg.popup("PACIENTE ADICIONADO COM SUCESSO.", title="sucesso!")


class MenuWindow():
    FILE = config['account']['default_filepath']
    def __init__(self):
        print(self.FILE)
        # layout
        layout = [
            [sg.Text("MENU DE AÇÕES")],
            [sg.Text("Buscar por Paciente:"), sg.Input(key="Pname"), sg.Button("Buscar", key="search"), ],
            [sg.Text("Outras ações:")],
            [sg.Button("Adicionar Paciente", key="add"), sg.Button("Ver todos", key="all"), sg.Button("Apagar Tabela", button_color="#c71f37", key="delete")]
        ]

        # Window
        self.window = sg.Window("Menu de ações").layout(layout)

    def init(self):

        while True:
            self.clickedButton, self.value = self.window.Read(timeout=100)

            if self.clickedButton == sg.WIN_CLOSED:
                break

            if self.clickedButton == "add":
                add_window = AddPatWindow()
                add_window.init()
            if self.clickedButton == "all":
                ShowTableWindow()
            if self.clickedButton == "search":
                ShowTableWindow(self.value["Pname"])
            if self.clickedButton == "delete":
                popup = tbl.ConfirmationPopup()
                confirm = popup.alert()
                popup.window.close()
                if confirm:
                    xl.DeleteAll(self.FILE)
                    sg.popup("TABELA APAGADA! Reinicie o software.")
                    break


class system:
    def __init__(self):
        self.window1 = FileWindow()
        self.window2 = MenuWindow()

    def init(self):
        self.window1.init()
        self.window2.init()
