import openpyxl as xl

class excel:
    def __init__(self, filename:str):
        try:
            xl.load_workbook(filename)
        except:
            raise Exception("This file does not exists")
        else:
            pass
        self.workbook = xl.load_workbook(filename)

