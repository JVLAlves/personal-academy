from selenium.webdriver.common.by import By
from translate import Translator

en_bible = [
    'Genesis',
    'Exodus',
    'Leviticus',
    'Numbers',
    'Deuteronomy',
    'Joshua',
    'Judges',
    'Ruth',
    '1 Samuel',
    '2 Samuel',
    '1 Kings',
    '2 Kings',
    '1 Chronicles',
    '2 Chronicles',
    'Ezra',
    'Nehemiah',
    'Esther',
    'Job',
    'Psalms',
    'Psalm',
    'Proverbs',
    'Ecclesiastes',
    'Song of Solomon',
    'Isaiah',
    'Jeremiah',
    'Lamentations',
    'Ezekiel',
    'Daniel',
    'Hosea',
    'Joel',
    'Amos',
    'Obadiah',
    'Jonah',
    'Micah',
    'Nahum',
    'Habakkuk',
    'Zephaniah',
    'Haggai',
    'Zechariah',
    'Malachi',
    'Matthew',
    'Mark',
    'Luke',
    'John',
    'Acts',
    'Romans',
    '1 Corinthians',
    '2 Corinthians',
    'Galatians',
    'Ephesians',
    'Philippians',
    'Colossians',
    '1 Thessalonians',
    '2 Thessalonians',
    '1 Timothy',
    '2 Timothy',
    'Titus',
    'Philemon',
    'Hebrews',
    'James',
    '1 Peter',
    '2 Peter',
    '1 John',
    '2 John',
    '3 John',
    'Jude',
    'Revelation'
]

bible = {
    "Genesis": {"method":By.XPATH, "path": "//a[@aria-label='Genesis (opens in a new tab)']"},
    "Exodus": {"method":By.XPATH, "path": "//a[@aria-label='Exodus (opens in a new tab)']"},
    "Leviticus": {"method":By.XPATH, "path": "//a[@aria-label='Leviticus (opens in a new tab)']"},
    "Numbers": {"method":By.XPATH, "path": "//a[@aria-label='Numbers (opens in a new tab)']"},
    "Deuteronomy": {"method": By.XPATH, "path": "//a[normalize-space()='Deuteronomy']"},
    "Joshua": {"method": By.XPATH, "path": "//a[@aria-label='Joshua (opens in a new tab)']"},
    "Judges": {"method": By.XPATH, "path": "//a[@aria-label='Judges (opens in a new tab)']"},
    "Ruth": None,
    "1 Samuel": {},
    "2 Samuel": {},
    "1 Kings": {"method": By.XPATH, "path": "//a[contains(@aria-label,'1 Kings (opens in a new tab)')]"},
    "2 Kings": {"method": By.XPATH, "path": "//a[@aria-label='2 Kings (opens in a new tab)']"},
    "1 Chronicles": None,
    "2 Chronicles": {"method": By.CSS_SELECTOR, "path": "a[href='https://www.fullofeyes.com/skill/2-chronicles/']"},
    "Ezra": None,
    "Nehemiah": {"method": By.XPATH, "path": "//a[@aria-label='Nehemiah (opens in a new tab)']"},
    "Esther": None,
    "Job": {"method": By.XPATH, "path": "//a[contains(@aria-label,'Job (opens in a new tab)')]"},
    "Psalms": {"method": By.XPATH, "path": "//a[@aria-label='Psalms (opens in a new tab)']"},
    "Proverbs": {"method": By.XPATH, "path": "//a[@href='https://www.fullofeyes.com/skill/proverbs/']"},
    "Ecclesiastes": {"method": By.XPATH, "path": "//a[@aria-label='Ecclesiastes (opens in a new tab)']"},
    "Song of Songs": {"method": By.XPATH, "path": "//a[@aria-label='Song of Songs (opens in a new tab)']"},
    "Isaiah": {"method": By.XPATH, "path": "//a[@href='https://www.fullofeyes.com/skill/isaiah/']"},
    "Jeremiah": {"method": By.XPATH, "path": "//a[@aria-label='Jeremiah (opens in a new tab)']"},
    "Lamentations": {"method": By.XPATH, "path": "//a[@aria-label='Lamentations (opens in a new tab)']"},
    "Ezekiel": {"method": By.XPATH, "path": "//a[@href='//a[@aria-label=' Ezekiel (opens in a new tab)']"},
    "Daniel": {"method": By.XPATH, "path": "//a[@href='https://www.fullofeyes.com/skill/daniel/']"},
    "Hosea": {"method": By.XPATH, "path": "//a[@aria-label='Hosea (opens in a new tab)']"},
    "Joel": {"method": By.XPATH, "path": "//a[@href='https://www.fullofeyes.com/skill/joel/']"},
    "Amos": {"method": By.XPATH, "path": "//a[@aria-label='Amos (opens in a new tab)']"},
    "Obadiah": None,
    "Jonah": {"method": By.XPATH, "path": "//a[@href='https://www.fullofeyes.com/skill/jonah/']"},
    "Micah": {"method": By.XPATH, "path": "//a[contains(@aria-label,'Micah (opens in a new tab)')]"},
    "Nahum": {"method": By.XPATH, "path": "//a[@aria-label='Nahum (opens in a new tab)']"},
    "Habakkuk": {"method": By.XPATH, "path": "//a[@href='https://www.fullofeyes.com/skill/habakkuk/']"},
    "Zephaniah": {"method": By.XPATH, "path": "//a[@href='https://www.fullofeyes.com/skill/zechariah/']"},
    "Haggai": {"method": By.XPATH, "path": "//a[@href='https://www.fullofeyes.com/skill/haggai/']"},
    "Zechariah": {"method": By.XPATH, "path": "//a[@href='https://www.fullofeyes.com/skill/zechariah/']"},
    "Malachi": {"method": By.XPATH, "path": "//a[@href='https://www.fullofeyes.com/skill/malachi/']"},
    "Matthew": {"method": By.XPATH, "path": "//a[@aria-label='Matthew (opens in a new tab)']"},
    "Mark": {"method": By.XPATH, "path": "//a[@href='https://www.fullofeyes.com/skill/mark/']"},
    "Luke": {"method": By.XPATH, "path": "//a[@href='https://www.fullofeyes.com/skill/luke/']"},
    "John": {"method": By.XPATH, "path": "//a[contains(@href,'https://www.fullofeyes.com/skill/john/')]"},
    "Acts": {"method": By.XPATH, "path": "//a[@aria-label='Acts (opens in a new tab)']"},
    "Romans": {"method": By.XPATH, "path": "//a[@href='https://www.fullofeyes.com/skill/romans/']"},
    "1 Corinthians": {"method": By.CSS_SELECTOR, "path": "a[aria-label='1 Corinthians (opens in a new tab)']"},
    "2 Corinthians": {"method": By.CSS_SELECTOR, "path": "a[href='https://www.fullofeyes.com/skill/2-corinthians/']"},
    "Galatians": {"method": By.XPATH, "path": "//a[@aria-label='Deuteronomy (opens in a new tab)']"}, #This doesnt make sense
    "Ephesians": {"method": By.XPATH, "path": "//a[@aria-label='Ephesians (opens in a new tab)']"},
    "Philippians": {"method": By.XPATH, "path": "//a[@aria-label='Philippians (opens in a new tab)']"},
    "Colossians": {"method": By.XPATH, "path": "//a[@href='https://www.fullofeyes.com/skill/colossians/']"},
    "1 Thessalonians": {"method": By.CSS_SELECTOR, "path": "a[href='https://www.fullofeyes.com/skill/1=thessalonians/']"},
    "2 Thessalonians": {"method": By.XPATH, "path": "//a[@aria-label='2 Thessalonians (opens in a new tab)']"},
    "1 Timothy": {"method": By.XPATH, "path": "//a[@aria-label='1 Timothy (opens in a new tab)']"},
    "2 Timothy": {},
    "Titus": {"method": By.XPATH, "path": "//a[contains(@href,'https://www.fullofeyes.com/skill/titus/')]"},
    "Philemon": None,
    "Hebrews": {"method": By.XPATH, "path": "//a[contains(@href,'https://www.fullofeyes.com/skill/hebrews/')]"},
    "James": {"method": By.XPATH, "path": "//a[@aria-label='James (opens in a new tab)']"},
    "1 Peter": {"method": By.CSS_SELECTOR, "path": " a[aria-label='1 Peter (opens in a new tab)']"},
    "2 Peter": {},
    "1 John": {"method": By.XPATH, "path": "//a[contains(@aria-label,'1 John (opens in a new tab)')]"},
    "2 John": {"method": By.CSS_SELECTOR, "path": "a[aria-label='2 John (opens in a new tab)']"},
    "3 John": None,
    "Jude": {"method": By.XPATH, "path": "//a[contains(@href,'https://www.fullofeyes.com/skill/jude/')]"},
    "Revelation": {"method": By.XPATH, "path": "//a[@aria-label='Revelation (opens in a new tab)']"},
}

toBooks = {
    "Gênesis": "Genesis",
    "Êxodo": "Exodus",
    "Levítico":"Leviticus",
    "Números": "Numbers",
    "Deuteronômio": "Deuteronomy",
    "Josué":   "Joshua",
    "Juízes":    "Judges",
    "Rute":    "Ruth",
    "1 Samuel": "1 Samuel",
    "2 Samuel": "2 Samuel",
    "1 Reis": "1 Kings",
    "2 Reis": "2 Kings",
    "1 Crônicas": "1 Chronicles",
    "2 Crônicas": "2 Chronicles",
    "Esdras": "Ezra",
    "Neemias": "Nehemiah",
    "Ester": "Esther",
    "Jó": "Job",
    "Salmo": "Psalm",
    "Provérbios": "Proverbs",
    "Eclesiastes":   "Ecclesiastes",
    "Cantares":  "Song of Songs",
    "Cânticos":  "Song of Songs",
    "Cânticos dos Cânticos":  "Song of Songs",
    "Isaías": "Isaiah",
    "Jeremias": "Jeremiah",
    "Lamentações":    "Lamentations",
    "Ezequiel": "Ezekiel",
    "Daniel": "Daniel",
    "Oseias": "Hosea",
    "Joel": "Joel",
    "Amós": "Amos",
    "Obadias": "Obadiah",
    "Jonas": "Jonah",
    "Miqueias": "Micah",
    "Naum": "Nahum",
    "Habacuque": "Habakkuk",
    "Sofonias": "Zephaniah",
    "Ageu": "Haggai",
    "Zacarias": "Zechariah",
    "Malaquias": "Malachi",
    "Mateus": "Matthew",
    "Mattheus": "Matthew",
    "Marcos": "Mark",
    "Lucas": "Luke",
    "João": "John",
    "Atos": "Acts",
    "Romanos": "Romans",
    "1 Coríntios": "1 Corinthians",
    "2 Coríntios": "2 Corinthians",
    "Gálatas": "Galatians",
    "Efésios": "Ephesians",
    "Filipenses": "Philippians",
    "Colossenses": "Colossians",
    "1 Tessalonicenses": "1 Thessalonians",
    "2 Tessalonicenses": "2 Thessalonians",
    "1 Timóteo": "1 Timothy",
    "2 Timóteo": "2 Timothy",
    "Tito": "Titus",
    "Filemom": "Philemon",
    "Hebreus": "Hebrews",
    "Tiago": "James",
    "1 Pedro": "1 Peter",
    "2 Pedro": "2 Peter",
    "1 João": "1 John",
    "2 João": "2 John",
    "3 João": "3 John",
    "Judas": "Jude",
    "Apocalipse": "Revelation"
}
class Image:
    def __init__(self, href:str, src:str, dimensions:list):
        self.href = href
        self.src = src
        self.width = float(dimensions[0])
        self.height = float(dimensions[1])
        self.dimensions = (self.width, self.height)
class Passage:
    def __init__(self, book, chapter, verses, img=None):
        translator = Translator(from_lang="pt-br", to_lang="english")
        if book in en_bible:
            self.book = book
        else:
            try:
                eng_book = translator.translate(book).capitalize()
                if eng_book not in en_bible:
                    raise Exception
            except:
                self.book = toBooks[book.capitalize()]
                print("Manual Translate", self.book)
            else:
                if eng_book == book and book in toBooks:
                    self.book = toBooks[book.capitalize()]
                    print("Manual Translate", self.book)
                elif eng_book != book or (eng_book == book and book in bible):
                    self.book = eng_book
                    print("Translating", self.book)

        self.chapter = chapter
        self.verses = verses
        self.img = img

    def show(self):
        return f"{self.book} {self.chapter}:{self.verses}"
    def display(self):
        print(f"{self.book} {self.chapter}:{self.verses}")

