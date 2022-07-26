#!/usr/bin/env python

"""globals.py: Globals is the file which contains the constant values used through the LITTY code. 

"""
__author__ = "João Vítor de Luiz Alves"
__copyright__ = "Copyright 2022, JVL Alves"
__credits__ = ["João Vítor de Luiz Alves", "Amiel Dias de Luiz"]

__maintainer__ = "Amiel Dias de Luiz"
__email__ = "joaovitordeluizalves@gmail.com"
__status__ = "production"

from LITTY.glob.errors import NotHexadecimalError, BadHexadecimalError

# TEMPORARY GLOBALS
default_download = "/Users/joaovitor/Desktop"

# CODE GLOBALS
FILE_DATETIME_FORMAT = "%d-%m-%YT%H:%M"
FILE_WATERMARK = "_litigation"
FILE_EXTENSION = ".docx"


# AESTHETICS GLOBALS
class font:
    def __init__(self, family: str, size: int, style: str = None, color: str = "#000000"):
        self.family = family
        self.size = size
        self.style = style

        ############# COLOR TEST ####################

        if color.find("#") == -1:
            raise NotHexadecimalError(hex)

        hex_values = color.strip()[1:]

        if len(hex_values) != 6 or (not hex_values.isalnum()):
            raise BadHexadecimalError(hex_values)

        self.color = color

    def toPySimpleGui(self):
        return f"{self.family.capitalize()} {self.size}" + (f" {self.style.lower()}" if self.style is not None else "")


FONT_P1 = font("Arial", 14)
FONT_P2 = font("Arial", 12)
FONT_P3 = font("Arial", 10)
FONT_TITLE = font("Times", 16, "bold")
FONT_H1 = font("Times", 14, "bold")
FONT_SUBTITLE = font("Times", 12)
FONT_FOOTER = font("Times", 10, "italic")

COMPANY_YELLOW = "#BF945A"
COMPANY_BLUE = "#13476A"



if __name__ == '__main__':
    pass
