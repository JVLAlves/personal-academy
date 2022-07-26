import PySimpleGUI as sg
import LITTY.cmd.mongo.mongo_users_cmds as mg_users
import LITTY.glob.globals as glob


class REGISTRATION:
    layout = [
        [sg.Push(), sg.Text("USER REGISTRATION", font=glob.FONT_TITLE.toPySimpleGui(), text_color=glob.FONT_TITLE.color), sg.Push()],
        [sg.Push(), sg.Text("USER: "), sg.Input(size=(16, 1), key="-USER-"), sg.Text(key="-AVAILABLEUSER-"), sg.Push()],
        [sg.Push(), sg.Text("PASSWORD: "), sg.Input(size=(8, 1), key="-PSWD-", password_char="*"), sg.Text(key="-AVAILABLEPASS-"), sg.Push()],
        [sg.Push(), sg.FolderBrowse(key="-DPATH-"), sg.Text("choose a Download path"), sg.Push()],
        [sg.VPush()],
        [sg.Push(), sg.Button("REGISTER", key="-REGISTER-"), sg.Push()],
    ]

    def __init__(self):
        self.window = sg.Window("REGISTER").layout(self.layout)

        while True:
            event, values = self.window.read(timeout=100)

            if values is not None and values["-USER-"] is not None:
                # database verification
                exists = mg_users.user_exists(values["-USER-"])

                if not exists:
                    self.window["-AVAILABLEUSER-"].update("AVAILABLE")
                    self.username_available = True
                else:
                    self.window["-AVAILABLEUSER-"].update("NOT AVAILABLE")
                    self.username_available = False

            if values is not None and values["-PSWD-"] is not None:
                # Regular Expression to PASSWORD
                # password must contains:
                # minimum 8 characters
                #  at least 4 Numbers
                #  at least 2 letters (Upper and Lower)
                #  at least 1 special character
                PASSWORD = values["-PSWD-"]
                if len(PASSWORD) >= 8:
                    self.window["-AVAILABLEPASS-"].update("AVAILABLE")
                    self.password_available = True
                else:
                    self.window["-AVAILABLEPASS-"].update("NOT AVAILABLE")
                    self.password_available = False

            if event == sg.WIN_CLOSED:
                break

            elif event == "-REGISTER-":
                if values is None:
                    sg.popup_error("NOT ABLE TO REGISTER NONE.")
                    continue
                else:

                    USERNAME = values["-USER-"]
                    PASSWORD = values["-PSWD-"]
                    DOWNLOADS = values["-DPATH-"]

                    USER = {"username": USERNAME, "password": PASSWORD, "download_folder": DOWNLOADS}

                    if self.username_available and self.password_available:
                        mg_users.insert_user(USER)
                        sg.popup_notify(f"User {USERNAME} created sucessfully!")
                        break
                    else:
                        sg.popup_error("USERNAME OR PASSWORD UNAVAILABLE")
                        continue

        self.window.close()


class LOGIN:
    layout = [
        [sg.Push(), sg.Text("USER LOGIN", font="Times 14 bold", text_color="#000000"), sg.Push()],
        [sg.Push(), sg.Text("USER: "), sg.Input(size=(16, 1), key="-USER-"), sg.Push()],
        [sg.Push(), sg.Text("PASSWORD: "), sg.Input(size=(8, 1), key="-PSWD-", password_char="*"), sg.Push()],
        [sg.Push(), sg.Text("forgot my password", enable_events=True, key="-FORGOT-"), sg.Push()],
        [sg.VPush()],
        [sg.Push(), sg.Button("LOG IN", key="-LOGIN-"), sg.Push()],
        [sg.Push(), sg.Button("SIGN IN", key="-SIGNIN-"), sg.Push()]
    ]

    retries = 6

    def __init__(self):
        self.window = sg.Window("LOG IN").layout(self.layout)

    def open(self):

        while True:
            event, values = self.window.read()
            print(event)
            if event == sg.WIN_CLOSED:
                break

            elif event == "-LOGIN-":
                answer = self.__LOGIN(values)
                if answer is not None:
                    self.window.close()
                    return answer
                else:
                    continue

            elif event == "-SIGNIN-":
                self.__SIGNIN()
                continue
        self.window.close()

    def __SIGNIN(self):
        REGISTRATION()

    def __LOGIN(self, values: dict):
        if values is not None:
            USERNAME = values["-USER-"]
            PASSWORD = values["-PSWD-"]
            exists = mg_users.user_exists(USERNAME)
            if exists:
                USER = mg_users.get_user(USERNAME)

                if USER["password"] == PASSWORD:
                    return USERNAME
                else:
                    if self.retries > 0:
                        self.retries -= 1
                        sg.popup_error(f"USERNAME OR PASSWORD INCORRECT (retries {self.retries}/6)")
                        return
                    else:
                        sg.popup_error("NUMBERS OF RETRIES EXCEEDED")
                        exit()
            else:
                if self.retries > 0:
                    self.retries -= 1
                    sg.popup_error(f"USERNAME OR PASSWORD INCORRECT (retries {self.retries}/6)")
                    return
                else:
                    sg.popup_error("NUMBERS OF RETRIES EXCEEDED")
                    exit()

        else:
            sg.popup_error("Empty inputs")
            return


def initiate_login_window():
    if not mg_users.user_any():
        REGISTRATION()

    LOG = LOGIN()
    return LOG.open()


if __name__ == '__main__':
    pass
#TODO: fix first registration
#TODO: specific kind of password verification