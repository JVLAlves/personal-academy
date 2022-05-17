#this is the main module
#TODO: Error handling popups (half-way done. I dont see any other use yet)
#TODO: Remover prints ou substituir por logs
#TODO: transformar codigo fonte em software ou app de Desktop
#TODO: Separar melhor os paragrafos (tentar objetificar as linhas)
#TODO: Anexar as imagens as noticias
#TODO: Gerenciar requests de mais de uma noticia (Fresh News)
#TODO: Rever tudo e comentar

import datetime
import os

import PySimpleGUI as sg
import originum as ori
import multiprocessing as mp
import REunion as reun
import logging
from automation import automates



application_icon = "img/liskarm-icon.png"

class charge:
    def __init__(self):
        layout = [
            [sg.Image('img/liskarm-chargin.gif', key="-lisgif-")]
        ]

        self.window = sg.Window("Loading...",icon=application_icon).layout(layout)

    def init(self):
        while True:
            event, _ = self.window.read(timeout=500)
            self.window.find_element("-lisgif-").UpdateAnimation("img/liskarm-chargin.gif", time_between_frames=500)
            if event == sg.WIN_CLOSED:
                self.window.close()

    def close(self):
        self.window.close()


class Main:
    chargin_window = charge()
    chargin = mp.Process(target=chargin_window.init)
    news_indication = None
    category = None
    news_to_focus = None

    def __init__(self):

        layout = [
            [sg.VPush()],
            [sg.Push(), sg.Text("Liskraw", font="Arial 20 bold", text_color="#000000"), sg.Push()],
            [sg.Text("News Number:"), sg.Push()],
            [sg.Push(), sg.Radio("The Latest", "news_number", key="latest"),
             sg.Radio("Fresh News", "news_number", key="nines"), sg.Radio("Other:", "news_number", key="other"),
             sg.Input(key="specific_news", size=(6, 1)), sg.Push()],
            [sg.Text("News Type:"), sg.Push()],
            [sg.Push(), sg.Radio("ALL", "news_type", key="all"), sg.Radio("Contest", "news_type", key="contest"),
             sg.Radio("Event", "news_type", key="event"), sg.Push()],
            [sg.Push(), sg.Button("Search", key="Search"), sg.Button("Automate", key="-AUTO-"), sg.Push()],
            [sg.VPush()]
        ]

        self.window = sg.Window("Main Window",icon=application_icon).layout(layout)

    def init(self):
        opened = 0
        while True:
            opened+=1
            event, values = self.window.Read()
            logging.info(f"Main window opened ({opened})")

            if event == sg.WIN_CLOSED:
                break
            elif event == 'Search':
                #self.chargin.start()
                news_number = ["latest", "other", "nines"]

                for value in values:
                    if values[value] != '':
                        if values[value] and value in news_number:
                            self.news_indication = value

                if self.news_indication is None:
                    sg.popup_error("No indication marked.\nPlease, choose a new indication.",title="Error", font="Arial 16 bold")
                    logging.error("indication not marked")
                    continue


                news_type = ['all', 'contest', 'event']
                for value in values:
                    if values[value] != '':
                        if values[value] and value in news_type:
                            self.category = value

                if self.category is None:
                    if self.news_indication == "other":
                        pass
                    else:
                        sg.popup_error("No category marked.\nPlease, choose a new category.",title="Error", font="Arial 16 bold")
                        logging.error("category not marked")
                        continue

                if self.news_indication in ["latest", "nines"]:
                    logging.info("Searching for news")
                    self.news_to_focus = ori.Search(self.news_indication, self.category)
                    logging.info(f"this is the found news '{self.news_to_focus}'.")
                elif self.news_indication == "other":
                    logging.info(values['specific_news'])
                    self.news_to_focus = f"/news/{values['specific_news']}"
                    logging.info(f"this is the specific new '{self.news_to_focus}'.")

                if self.news_to_focus is None:
                    sg.popup_error("Error founding news", title="Error", font="Arial 16 bold")
                    logging.error("news not found")
                    continue

                if isinstance(self.news_to_focus, list):
                    for news in self.news_to_focus:
                        logging.info(f"Focusing on News '{news}'")
                        try:
                            news_content, url = ori.Focus(news)
                        except:
                            sg.popup_error(f"{news} not found", title="Error", font="Arial 16 bold")
                            logging.error(f"{news} not exists")
                            exit()
                        else:
                            if len(news_content) != 0:
                                # self.chargin.terminate()
                                # self.chargin_window.close()
                                return news_content, url

            elif event == "-AUTO-":
                today_moment = datetime.datetime.today()
                today_str = today_moment.strftime("%Y-%m-%dT%H:%M")
                ori.Config_init()
                config = ori.Config()
                liskarm = config["liskarm"]
                liskarm["last_time_run"] = today_str

                # self.chargin.start()
                news_number = ["latest", "other", "nines"]

                for value in values:
                    if values[value] != '':
                        if values[value] and value in news_number:
                            self.news_indication = value

                if self.news_indication is None:
                    sg.popup_error("No indication marked.\nPlease, choose a new indication.", title="Error",
                                  font="Arial 16 bold")
                    logging.error("indication not marked")
                    continue

                news_type = ['all', 'contest', 'event']
                for value in values:
                    if values[value] != '':
                        if values[value] and value in news_type:
                            self.category = value


                if self.category is None:
                        sg.popup_error("No category marked.\nPlease, choose a new category.", title="Error",
                                       font="Arial 16 bold")
                        logging.error("category not marked")
                        continue

                if not eval(liskarm["automation"]):
                    liskarm["automation"] = "True"
                else:
                    liskarm["automation"] = "False"

                liskarm["news_type"] = self.news_indication
                liskarm["news_category"] = self.category

                with open(ori.CONFIG_FILE, "w") as ConfigFile:
                    config.write(ConfigFile)
                automates()
                exit()

            else:
                try:
                    news_content, url = ori.Focus(self.news_to_focus)
                except:
                    sg.popup_error(f"{self.news_to_focus} not found", title="Error", font="Arial 16 bold")
                    exit()
                else:
                    if len(news_content) != 0:
                        # self.chargin.terminate()
                        # self.chargin_window.close()
                        return news_content, url


        exit()
class Return:
    def __init__(self, paragraphs:list):
        content = []
        for p in paragraphs:
            if p.isupper():
                column = [sg.Push(), sg.Text(p, font="Arial 12 bold", text_color="#000000"), sg.Push()]
            else:
                column = [sg.Push(), sg.Text(p, font="Arial 10", text_color="#000000"), sg.Push()]
            content.append(column)
        layout = [
            [sg.VPush()],
            [sg.Column(content, justification="justify", scrollable=True)],
            [sg.VPush()],
            [sg.Push(), sg.Button("see on page", key="-see-")],
            [sg.VPush()]
        ]

        self.window = sg.Window("News", icon=application_icon, auto_size_text=True, size=(1250, 625)).layout(layout).finalize()
        self.window.maximize()
        self.window.bind("<Key-Escape>", "esc")
        while True:
            event, _ = self.window.Read()
            if event == sg.WIN_CLOSED or event == "esc":
                break
            elif event == "-see-":
                pass
        self.window.close()


if __name__ == "__main__":
    date = datetime.datetime.today()
    today = date.strftime("%Y_%m_%d")
    if os.path.exists("../log/"):
        if os.path.exists(f"../log/process_run_{today}.log"):
            pass
        else:
            with open(f"../log/process_run_{today}.log", "x"):
                pass
    else:
        os.mkdir("../log/")
        with open(f"../log/process_run_{today}.log", "x"):
            pass

    logging.basicConfig(filename=f"../log/process_run_{today}.log", filemode="w", format="%(asctime)s - %(levelname)s : %(message)s", level=logging.DEBUG)
    logging.warning(f"Process started {date.now()}")
    main = Main()
    new, url = main.init()
    with open(".arknew.txt", "w") as file:
        for line in new:
            file.write(f"{line}\n")

    with open(".arknew.txt", 'r') as f:
        lines = f.readlines()

    os.remove(".arknew.txt")

    arknews = reun.Arknews(lines, url)
    arknews.short()
