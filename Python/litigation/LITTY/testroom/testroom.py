from pprint import pprint

import PySimpleGUI as sg



layout = [
    [sg.Push(), sg.Radio("Vertical", "TablePosition", key="vertical"), sg.Radio("Horizontal", "TablePosition", key="horizontal"), sg.Push()],
    [sg.Push(), sg.Button("SUBMIT"), sg.Push()],
]

if __name__ == '__main__':
    window = sg.Window("Radio Window").layout(layout)
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == "SUBMIT":
            pprint(values)
    window.close()