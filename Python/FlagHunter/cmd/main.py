import socket
from pathlib import Path
from actions.computer_profile import getComputerProfile
from objects.first_settings import init
import os
print(Path.home())
import uuid as id
import mongo.mongo_cmds as mg
if __name__ == '__main__':
    profile = getComputerProfile()
    if not mg.Exists(profile):
        tags = init()

        profile.update({"tags":tags})

        mg.insert(profile)
    else:
        #TODO: CTF PROCESS including scanning, moving, renaming and cleaning
        print("MAKE BETTER")
        pass


