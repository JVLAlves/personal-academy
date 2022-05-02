import PySimpleGUI as sg
import originum as ori
import multiprocessing as mp
import REunion as reun

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
    news_indication = ''
    category = ''
    news_to_focus = ''

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
            [sg.Push(), sg.Button("Search", key="search"), sg.Push()],
            [sg.VPush()]
        ]

        self.window = sg.Window("Main Window",icon=application_icon).layout(layout)

    def init(self):
        while True:
            event, values = self.window.Read()

            if event == sg.WIN_CLOSED:
                break
            elif event == 'search':
                self.window.close()
                #self.chargin.start()
                news_number = ["latest", "other", "nines"]

                for value in values:
                    if values[value] != '':
                        if values[value] and value in news_number:
                            self.news_indication = value

                news_type = ['all', 'contest', 'event']
                for value in values:
                    if values[value] != '':
                        if values[value] and value in news_type:
                            self.category = value

            if self.news_indication in ["latest", "nines"]:
                print("Searching for news")
                self.news_to_focus = ori.Search(self.news_indication, self.category)
                print(f"this is the searched news '{self.news_to_focus}'.")
            elif self.news_indication == "other":
                print(values['specific_news'])
                self.news_to_focus = f"/news/{values['specific_news']}"
                print(f"this is the specific new '{self.news_to_focus}'.")

            if isinstance(self.news_to_focus, list):
                for news in self.news_to_focus:
                    print(f"Focusing on News '{news}'")
                    news_content, url = ori.Focus(news)
                    if len(news_content) != 0:
                    #self.chargin.terminate()
                    #self.chargin_window.close()
                        return news_content, url

            else:
                news_content, url = ori.Focus(self.news_to_focus)
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
    main = Main()
    new, url = main.init()
    arknews = reun.Arknews(new, url)
    arknews.short()

"""

TODO LIST:

* Create a way to display the News (Display GUI, File, whatever)
* Error handling popups
* Remove prints

(kawaii)
https://github.com/JVLAlves/personal-academy/blob/master/Python/Arkcrawler/images/4148b681c1b08841f38ba3a275c435df-removebg-preview.png

(kowai)
https://github.com/JVLAlves/personal-academy/blob/master/Python/Arkcrawler/images/Liskarm.full.3266949.png
"""
