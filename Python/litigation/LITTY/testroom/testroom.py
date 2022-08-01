from pprint import pprint
import pymongo as mg
import PySimpleGUI as sg
from openpyxl.chart import layout

from LITTY.cmd.mongo.mongo_automation_cmds import automation_collection




if __name__ == '__main__':

    layout_one = [
        [sg.Checkbox("Pink", key="Pink")],
        [sg.Checkbox("Red", key="Red")],
        [sg.Checkbox("Green", key="Green")],
        [sg.Checkbox("Yellow", key="Yellow")],
    ]
    layout_two = [
        [sg.Checkbox("Blue", key="Blue")],
        [sg.Checkbox("Purple", key="Purple")],
        [sg.Checkbox("Orange", key="Orange")],
        [sg.Checkbox("White", key="White")],
    ]

    layout_three = [
        [sg.Checkbox("Brown", key="Brown")],
        [sg.Checkbox("Ice", key="Ice")],
        [sg.Checkbox("Gray", key="Gray")],
        [sg.Checkbox("Black", key="Black")],
    ]


    layout_frame = [[sg.Frame("Colour One",layout_one, key="AIT"), sg.Frame("Colour Two",layout_two), sg.Frame("Colour Three",layout_three)],[sg.VPush()], [sg.Push(), sg.Button("SEND"), sg.Push()],]



    layout_listbox = [
        [sg.Listbox(["Pink","Red", "Yellow", "Orange"], key="Color1")],
        [sg.Listbox(["Blue", "Greem", "Purple", "White"], key="Color2")]
    ]

    layout =[[sg.Frame("Colors", layout_listbox)]]






    window = sg.Window("Choose a Color").layout(layout_frame)
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            exit()
        elif event == "SEND":
            print(event, values)