import PySimpleGUI as sg
from configparser import ConfigParser
import os

#TODO: Username, case sensitive or not?
#TODO: End of login block (login checked)
#TODO: If possible, bigger font size
#TODO: If possible, create a more secure config file (with outside acesses only through password)
import const


def quickVerify(file):
    # verify if file path exists
    if not os.path.exists(file):
        return False

    # verify if the file is actually a file
    if not os.path.isfile(file):
        return False

    return True

#all kinds of windows in this module has this default files, so a window-kind object should inherit this window object
class window:
    #the file in which the automations' paths will be stored
    automationCacheFile = ".automationChace.ini"
    #the file which stores the users login
    UsersFile = ".Users.ini"

class vericityConfirm:
    def __init__(self):
        layout = [
            [sg.Push(), sg.Text("Insert the Company Password:", font="Arial 16 bold", text_color="#000000"), sg.Push()],
            [sg.VPush()],
            [sg.Push(), sg.Input(size=(15, 1), key="-COMP_PASSWORD-", password_char="*", tooltip="To make a new account you must know is the Company Password."), sg.Push()],
            [sg.VPush()],
            [sg.Push(), sg.Button("confirm", key="-CONFIRM-"), sg.Push()]
        ]
        window = sg.Window("Insert the Company Password")
        retries_limit = 5
        retries = 0
        while True:
            event, value = window.Read()
            if event == sg.WIN_CLOSED:
                break
            elif event == "-CONFIRM-" and (value["-COMP_PASSWORD-"] is not None or value["-COMP_PASSWORD-"] != ""):
                if value["-COMP_PASSWORD-"] == const.FILE_COMPANY_PASSWORD:
                    return
                else:
                    if retries < retries_limit:
                        continue
                    else:
                        sg.popup_error("Password retries exceeded")
                        exit()

        window.Close()
class SIGN_IN(window):
    #the config parser to make the config changes
    config = ConfigParser()

    #variable which describes if a the username is available to SIGNIN
    section_available = None

    #in case of the login window wants to automatically fill the SIGNIN spaces
    #with the former user typed information, there is a preset field for that
    def __init__(self, USER:str="", PASSWORD:str=""):
        #READ THE CONFIG FILE
        vericityConfirm()
        self.config.read(self.UsersFile)

        #Window layout for SIGNIN window
        SIGNIN_layout = [
            [sg.Push(), sg.Text("SIGNIN"), sg.Push()],
            [sg.VPush()],
            [sg.Text("username: "), sg.Input(size=(15,1), key="-USER-", default_text=USER), sg.Text(key="-AVAILABLE-")],
            [sg.Text("password: "), sg.Input(size=(15,1), key="-PASS-", default_text=PASSWORD)],
            [sg.VPush()],
            [sg.Push(), sg.Button("SIGN IN", key="-SIGNIN-", size=(10,1)), sg.Push()],

        ]

        #verifiing the existence of the default files
        for file in [self.UsersFile, self.automationCacheFile]:
            Exists = quickVerify(file)
            if not Exists:
                with open(file, "x"):
                    pass

        #creating SIGNIN window
        SIGNIN_window = sg.Window("SIGN IN").layout(SIGNIN_layout)

        #running SIGNIN window
        while True:
            event, value = SIGNIN_window.read(timeout=100)

            #real-time update for checking if the username is available to SIGNIN
            if value is not None and value["-USER-"] is not None:
                sections = self.config.sections()
                if value["-USER-"] not in sections:
                    SIGNIN_window["-AVAILABLE-"].update("AVAILABLE")
                    self.section_available = True
                else:
                    SIGNIN_window["-AVAILABLE-"].update("NOT AVAILABLE")
                    self.section_available = False

            #in case the user closes the window it literally closes it
            if event == sg.WIN_CLOSED:
                break

            #SIGNIN process button
            elif event == "-SIGNIN-":
                self.doSIGNIN(value["-USER-"], value["-PASS-"])
                break
        SIGNIN_window.close()

    #SIGNIN process funtion
    def doSIGNIN(self, USER:str, PASSWORD:str):
        #create a new section which is the username
        self.config.add_section(USER)

        #adds the password element to it
        self.config.set(USER, "PASSWORD", PASSWORD)

        #writes all changes in the file
        with open(self.UsersFile, "w") as ConfigFile:
            self.config.write(ConfigFile)

        #alerts the end of the process with a greeting
        sg.popup_ok(f"Registration done.\nWelcome, {USER.title()}!")

class LOGIN(window):

    login_layout = [
        [sg.Push(), sg.Text("LOGIN"), sg.Push()],
        [sg.VPush()],
        [sg.Text("username: "), sg.Input(size=(15,1), key="-USER-")],
        [sg.Text("password: "), sg.Input(password_char="*", size=(15,1), key="-PASS-")],
        [sg.VPush()],
        [sg.Push(), sg.Button("LOGIN", key="-LOGIN-", size=(10,1)), sg.Push()],
    ]

    def __init__(self):

        #verifiing the existence of the default files
        for file in [self.UsersFile, self.automationCacheFile]:
            Exists = quickVerify(file)
            if not Exists:
                with open(file, "x"):
                    pass

        login_window = sg.Window("LOGIN").layout(self.login_layout)
        while True:
            event, values = login_window.read()
            if event == sg.WIN_CLOSED:
                break
            elif event == "-LOGIN-":

                if values is None:
                    continue
                else:

                    USER = values["-USER-"]
                    PASSWORD = values["-PASS-"]
                    answer = self.doLogin(USER, PASSWORD)
                    if answer is None:
                        continue
                    else:
                        if answer:
                            sg.popup_timed(f"Welcome back, {USER}!", title="Success!",auto_close_duration=1.5)
                            break
                        else:
                            sg.popup_error("Wrong user or password!", font="Arial 16 bold", text_color="#000000")
                            continue


        login_window.close()
    def doLogin(self, USER:str, PASSWORD:str):
        config = ConfigParser()
        config.read(self.UsersFile)
        users = config.sections()
        if USER in users:
            existent_password = config[USER]["PASSWORD"]
            if str(PASSWORD) == str(existent_password):
                return True
            else:
                return False
        else:
            ans = sg.popup_ok_cancel("Would you like to sign in?")
            if ans == "OK":
                SIGN_IN(USER, PASSWORD)
            elif ans == "Cancel":
                pass
            else:
                raise Exception("Invalid value passed")
        return None










if __name__ == "__main__":
    IsLogged = LOGIN()
    if IsLogged:
        print("Log In done!")
    else:
        print("User Unexistent")




