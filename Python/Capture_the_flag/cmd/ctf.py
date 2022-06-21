import os
import shutil
import paths as pts
import time
import ctf_hq as hq
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
DOWNLOADS_DIR = pts.HOME + '/' + "Downloads"
def ctf():

    files = os.listdir(DOWNLOADS_DIR)
    for file in files:
        tags_and_folders = pts.start()
        TAGS = list(tags_and_folders.keys())
        split_file = file.split("--")
        #print(split_file)
        if len(split_file) < 2:
            continue
        tag = split_file[0]
        if not hq.isTag(tag):
            #print(f"tag {tag} do not exists")
            continue
        else:
            if not hq.tagExists(tag):
                #print("Something went wrong")
                isCreated = hq.verify_tag_window(tag).returnment()
                if isCreated:
                    files.append(file)
                    continue
                else:
                    exit()

        file_newname = split_file[1]
        if tag in TAGS:
            shutil.move(pts.HOME + f"/Downloads/{file}", tags_and_folders[f"{tag}"])
            os.rename(tags_and_folders[f"{tag}"] + f"{file}", tags_and_folders[f"{tag}"] + f"{file_newname}")
            #print(f"{file_newname} moved to {tag} folder")

if __name__ == "__main__":
    ctf()