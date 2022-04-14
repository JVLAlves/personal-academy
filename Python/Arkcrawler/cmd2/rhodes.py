import PySimpleGUI as sg
import originum as ori
class Main:
    def __init__(self):

        layout = [
            [sg.VPush()],
            [sg.Push(), sg.Text("Arknights News", font="Arial 16 bold", text_color="#000000"), sg.Push()],
            [sg.Text("News Number:"), sg.Push()],
            [sg.Push(),sg.Radio("The Latest","news_number",key="latest", default=True), sg.Radio("Fresh News", "news_number", key="nines"), sg.Radio("Other:","news_number" , key="other"), sg.Input(key="specific_news",size=(6,1)), sg.Push()],
            [sg.Text("News Type:"), sg.Push()],
            [sg.Push(), sg.Radio("ALL","news_type",key="all", default=True), sg.Radio("Contest","news_type" , key="contest"), sg.Radio("Event","news_type" , key="event"),sg.Push()],
            [sg.Push(), sg.Button("Search", key="search"), sg.Push()],
            [sg.VPush()]
        ]

        self.window = sg.Window("Arkrawler").layout(layout)

    def init(self):
        while True:
            event, values = self.window.Read()

            if event == sg.WIN_CLOSED:
                break
            elif event == 'search':
                news_number = ["latest", "other"]
                self.news = ''
                for value in values:
                    if value and value in news_number:
                        print(value)
                        self.news = value
                        break

                news_type = ['all', 'contest', 'event']
                self.category = ''
                for value in values:

                    if value and value in news_type:
                        print(value)
                        self.category = value
                        break
            self.new = ""
            if self.news in ["latest", "nines"]:
                self.new = ori.Search(self.news, self.category)
            elif self.news == "other":
                self.new = values['specific_news']

                for news in self.new:
                    news_content = ori.Focus(news)
                    if len(news_content) != 0:
                        self.window.close()
                        return news_content

        self.window.close()
        return None

main = Main()
new = main.init()
for n in new:
    print(n)


