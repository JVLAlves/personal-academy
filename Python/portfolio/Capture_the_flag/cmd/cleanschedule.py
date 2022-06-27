import datetime
import PySimpleGUI as sg
from paths import Config, CONFIGFILE

class Schedule:
    config = Config()
    def __init__(self, timestamp:float=None):
        if timestamp is None:
            self.timestamp = self.__getTime()
        else:
            self.timestamp = timestamp

        self.date = datetime.datetime.fromtimestamp(self.timestamp)


    @classmethod
    def withTimestamp(cls, timestamp:float):
        return cls(timestamp)

    @classmethod
    def withDatetime(cls, datetime:datetime.datetime):
        timestamp = datetime.timestamp()
        return cls(timestamp)

    def __getTime(self):

        if "CLEANING" not in self.config.sections():
            self.config.add_section("CLEANING")
            self.config.set("CLEANING", "timestamp", "")
            with open(CONFIGFILE, "w") as ConfigFile:
                self.config.write(ConfigFile)
            return None

        if "timestamp" not in self.config["CLEANING"].keys():
            self.config.set("CLEANING", "timestamp", "")
            with open(CONFIGFILE, "w") as ConfigFile:
                self.config.write(ConfigFile)
            return None

        if self.config["CLEANING"]["timestamp"] == "":
            return None

        timestamp = self.config["CLEANING"]["timestamp"]
        timestamp = float(timestamp)
        return timestamp

    def setTime(self, days: float = 30, hours: float = 0, minutes: float = 0, Settimestamp=None):

        if Settimestamp is None:

            timestamp = self.timestamp

            if timestamp is None:
                timestamp = datetime.datetime.today()
            else:
                timestamp = datetime.datetime.fromtimestamp(timestamp)

            timestamp += datetime.timedelta(days=days, hours=hours, minutes=minutes)


        else:

            timestamp = Settimestamp


        self.config.set("CLEANING", "timestamp", str(timestamp))
        with open(CONFIGFILE, "w") as ConfigFile:
            self.config.write(ConfigFile)
        return

    def UserSet(self):

        fnt = 'Arial 12'
        layout = \
            [
            [sg.Push(), sg.Text("Schedule a Clean date", font="Arial 16", text_color="#000000"), sg.Push()],
            [sg.VPush()],
            [sg.Push(),sg.Input(tooltip="Hour:Minute", default_text="00:00", key="-TIME-", size=(5,1), font="Arial 14"), sg.Push()],
            [sg.Push(), sg.In(key='-INCAL1-', enable_events=True, visible=False),
            sg.Col([[sg.CalendarButton('Change date', target='-INCAL1-', font=fnt, format=('%Y-%m-%d'))]]), sg.Push()]

            ]

        window = sg.Window('Calendar', resizable=True).Layout(layout).finalize()

        while True:
            event, values = window.Read()
            print(event, values)
            if event == sg.WIN_CLOSED:
                sg.popup_ok("You must choose a date to Clean.", font="Arial 14 bold", text_color="#000000")
                continue
            elif event == "-INCAL1-" and values is not None:
                print(values["-INCAL1-"], type(values["-INCAL1-"]))
                time = datetime.datetime.strptime(f"{values['-INCAL1-']}T{values['-TIME-']}",'%Y-%m-%dT%H:%M')
                print(time)
                today = datetime.datetime.now()
                todaystamp = today.timestamp()
                timestamp = time.timestamp()

                if todaystamp > timestamp:
                    sg.popup_error("You must choose another date.",title="Past has Past", font="Arial 14 bold", text_color="#000000")
                    continue
                if today.year < time.year and today.month != 12:
                    res = sg.popup_ok_cancel("Are you sure you wanna schedule a cleaning a year ahead?", title="Too far away", font="Arial 14 bold", text_color="#000000")

                    if res.lower() == "cancel":
                        continue

                self.setTime(Settimestamp=timestamp)
                sg.popup("Clean date scheduled.", font="Arial 14")
                break

        window.close()


    def isTime(self):
        timestamp = float(self.timestamp)
        if timestamp is None:
            self.UserSet()
            return False

        today = datetime.datetime.today().timestamp()

        if today >= timestamp:
            return True
        else:
            return False

if __name__ == '__main__':
    sc = Schedule()
    sc.UserSet()
    print(sc.timestamp, sc.date)


