import unittest
from globals import font
from errors import NotHexadecimalError, BadHexadecimalError

class TestFontConstants(unittest.TestCase):
    def testColorError(self):
        self.assertRaises(NotHexadecimalError, font, "Times", 14, "bold", "FFD100")  # Missing Hex Symbol
        self.assertRaises(BadHexadecimalError, font, "Times", 14, "bold", "#FFD10")  # Invalid Hex: Missing Numbers
        self.assertRaises(BadHexadecimalError, font, "Times", 14, "bold", "#F%D100") # Invalid Hex: Not alphanumeric


if __name__ == '__main__':
    unittest.main()
