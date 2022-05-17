import os.path
from pathlib import Path
from configparser import ConfigParser

FILE = 'tags.ini'


def Config():
    if not os.path.exists(FILE):
        open(FILE, "x")

    config = ConfigParser()
    config.read(FILE)
    return config

HOME = str(Path.home())
AUTOF = HOME + "/automatic_files/"

if __name__ != "__main__":
    config = Config()

    if len(config.sections()) == 0:
        config.add_section("tags")
        config.add_section("autofilter")

    if len(config["tags"]) == 0:
        config.set("tags", "ICO", AUTOF + "icons/")
        config.set("tags", "ART", AUTOF + "arts/")
        config.set("tags", "PDF", AUTOF + "pdf/")
        config.set("tags", "PHT", AUTOF + "photos/")
        with open(FILE, "w") as ConfigFile:
            config.write(ConfigFile)

    tags_and_folders = {}
    TAGS = config["tags"]
    for elem in TAGS:
        tags_and_folders[elem.upper()] = TAGS[elem]

    if not os.path.exists(HOME + "/automatic_files/"):
        os.mkdir(HOME + "/automatic_files/")
    for path in tags_and_folders.values():
        if not os.path.exists(path):
            os.mkdir(path)




