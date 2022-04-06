import PySimpleGUI as sg
import excel as xl
import confighelpers as cf
import traceback

config = cf.init()


class LoginWindow:
    STATUS = config['account']['status']
    USER = config['account']['user']
    PASSWORD = config['account']['password']

    def __init__(self):
        # layout
        layout = [
            [sg.Text("LOGIN")],
            [sg.Text("username:"), sg.Input(key="user")],
            [sg.Text("password:"), sg.Input(key="password")],
            [sg.Button("Login")]
        ]

        # Window
        window = sg.Window("LOGIN").layout(layout)
        self.window = window

    def init(self):
        _, self.value = self.window.Read()
        if self.STATUS == "active":
            if (self.value["user"] == self.USER) and (self.value["password"] == self.PASSWORD):
                return True
            else:
                return False
        elif self.STATUS == "inactive":
            config.set("account", "user", self.value["user"])
            config.set("account", "password", self.value["password"])
            config.set("account", "status", "active")
            with open(cf.FILE, "w") as configFile:
                config.write(configFile)
            return True
        else:
            raise NameError


class MainWindow:
    FILE = config['account']['default_filepath']
    if FILE is not None and (FILE.endswith(".xlsx") or FILE.endswith(".csv")):
        splitFILE = FILE.split("/")
        splitFILE.pop(-1)
        FILE = "/".join(splitFILE) + "/"
    def __init__(self):
        login = LoginWindow()

        successfullyLogged = login.init()
        if not successfullyLogged:
            tb = traceback.format_exc()
            sg.popup_error(f'ERRO NO LOGIN', "USUÁRIO OU SENHA INCORRETOS", tb)
            login.window.close()
        else:
            login.window.close()


        # layout
        layout = [
            [sg.Text("IMPORTAÇÃO DA TABELA")],
            [sg.Text("Escolha um arquivo:")],
            [sg.FileBrowse(initial_folder=self.FILE, file_types=(("xlsx", "*.xlsx"), ("csv", "*.csv")))],
            [sg.Button("Enviar")]
        ]

        # Window
        window = sg.Window("importação da tabela").layout(layout)
        self.window = window

    def init(self):
        _, self.value = self.window.Read()
        if self.value["Browse"] != self.FILE:
            config.set("account", "default_filepath", self.value["Browse"])
            with open(cf.FILE, "w") as configFile:
                config.write(configFile)
        self.window.close()


class MenuWindow():
    def __init__(self):
        # layout
        layout = [
            [sg.Text("MENU DE AÇÕES")],
            [sg.Text("Buscar por Paciente:"), sg.Input(key="Pname"), sg.Button("Buscar")],
            [sg.Text("Outras ações:")],
            [sg.Button("Adicionar Paciente"), sg.Button("Ver todos")]
        ]

        # Window
        window = sg.Window("Menu de ações").layout(layout)
        self.window = window

    def init(self):
        self.clickedButton, self.value = self.window.Read()
        print(self.clickedButton, self.value)


wind = MainWindow()
wind.init()
