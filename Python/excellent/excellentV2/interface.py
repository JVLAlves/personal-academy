import PySimpleGUI as sg
import excel as xl
"""
class TelaPython:
    def __init__(self):
        # layout
        layout = [
            [sg.Text("Nome", size=(5,0)), sg.Input(size=(15,0))],
            [sg.Text("Idade", size=(5,0)), sg.Input(size=(15,0))],
            [sg.Button("Enviar")]
        ]
        # Window
        window = sg.Window("Dados do Usuário").layout(layout)
        # Extrair dados
        self.button, self.value = window.Read()

    def init(self):
        print(self.value)
        return self.value


class presentation:
    def __init__(self, name):
        # layout
        layout = [
            [sg.Text(f"Welcome, {name} to our virtual environment!")]
        ]

        # window
        window = sg.Window("Welcome").layout(layout)
        window.Read()


tela = TelaPython()

data = tela.init()
tela2 = presentation(data[0])
"""
classes = ["sam", "dwf", "elf", "mag"]
subtitle = {
    "sam": "Samurai",
    "dwf": "Dwarf",
    "elf": "Elf",
    "mag": "Mage"
}
IMG_PATH = {
    "Samurai": ["images/Sword.svg", "images/Sword.png"],
    "Dwarf": ["images/waraxe.svg", "images/waraxe.png"],
    "Elf": ["images/Axe.svg", "images/axe.png"],
    "Mage":["images/staff.svg", "images/staff.png"]
}
class mainWindow:

    def __init__(self):
        # layout
        self.initted = False
        layout = [
            [sg.Text("SWORDPLAY OFFLINE")],
            [sg.Text("Name:"), sg.Input(key="name")],
            [sg.Text("Classes:")],
            [sg.Checkbox("Samurai",key=classes[0]),sg.Checkbox("Dwarf",key=classes[1]),sg.Checkbox("Elf",key=classes[2]),sg.Checkbox("Mage",key=classes[3])],
            [sg.Button("Submit")]
        ]

        # window
        window = sg.Window("SPOFF - Register page").layout(layout)
        self.window = window
    def init(self):
        if not self.initted:
            self.initted = True
        else:
            raise RuntimeError
        # Extraction
        self.button, self.value = self.window.Read()

        print(self.value)


        infoKey = []
        infoValue = []
        for key in self.value:
            if key not in classes:
                infoKey.append(key)
                infoValue.append(self.value[key])

        classesDict = dict()
        infoDict = dict()
        for k in classes:
            classesDict[k] = self.value[k]
        for index, k in enumerate(infoKey):
            infoDict[k] = infoValue[index]

        return [infoDict, classesDict]

    def close(self):
        if self.initted:
            self.initted = False
            self.window.close()
        else:
            raise RuntimeError




class classWindow:
    def __init__(self, values:list):
        self.initted = False
        self.info = values[0]
        self.classname = values[1]
        for key in self.classname:
            print(key, self.classname[key])
            if self.classname[key]:
                self.Class = subtitle[key]
                break

        if self.Class in IMG_PATH:
            self.img = IMG_PATH[self.Class][1]
        else:
            raise KeyError

        ######################################
        # Layout - Window - Extraction (/)   #

        # layout
        layout = [
            [sg.Text("SWORDPLAY OFFLINE")],
            [sg.Text(f'CHOSEN CLASS: {self.Class}')],
            [sg.Image(self.img,size=(500,500))],
        ]

        # Window
        window = sg.Window("SPOFF - Class page").layout(layout)
        self.window = window

    def init(self):
        if not self.initted:
            self.initted = True
            self.window.Read()
        else:
            raise RuntimeError
    def close(self):
        if self.initted:
            self.window.close()
            self.initted = False
        else:
            raise RuntimeError

class System:
    def __init__(self):
        self.classPage = None
        self.register = mainWindow()

    def run(self):
        values = self.register.init()
        self.register.close()
        self.classPage = classWindow(values)
        self.classPage.init()


sys = System()
sys.run()


