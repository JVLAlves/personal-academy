import re

import PyPDF2 as pdf
import os
import pathlib
import PySimpleGUI as sg

# HOME DIRECTORY (LINUX: home/username, MacOS: Users/username)
HOME = str(pathlib.Path.home())
print(HOME)


def GetPageContent(file:str, page:int):
    # Open the file reading the bytes of it
    f = open(file, "rb")

    # read the whole data of the pdf file
    data_pdf = pdf.PdfFileReader(f)

    Page01 = data_pdf.getPage(page)

    content = Page01.extractText()

    return content

if __name__ == '__main__':
    file = None

    window = sg.Window("FILE CHOOSE").layout([[sg.Push(), sg.FilesBrowse(key="-FILE-"), sg.Text(), sg.Push()], [sg.VPush()], [sg.Push(), sg.Button("Submit", key="-SUB-"), sg.Push()]])
    while True:
        event, v = window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == "-SUB-":
            file = v["-FILE-"]
            break

    window.close()

    if file is None:
        exit()

    print(GetPageContent(file, 1))


