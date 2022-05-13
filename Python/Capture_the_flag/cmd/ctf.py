import os
import shutil
import paths as pts
import ctf_hq as hq
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
DOWNLOADS_DIR = pts.HOME + '/' + "Downloads"
def ctf():
    TAGS = list(pts.tags_and_folders.keys())

    files = os.listdir(DOWNLOADS_DIR)
    for file in files:
        print(file)
        split_file = file.split("--")
        print(split_file)
        if len(split_file) < 2:
            continue
        tag = split_file[0]
        if not hq.isTag(tag):
            print(f"tag {tag} do not exists")
            continue
        else:
            if not hq.tagExists(tag):
                hq.verify_tag_window(tag)

        file_newname = split_file[1]
        if tag in TAGS:
            shutil.move(pts.HOME + f"/Downloads/{file}", pts.tags_and_folders[f"{tag}"])
            os.rename(pts.tags_and_folders[f"{tag}"] + f"{file}", pts.tags_and_folders[f"{tag}"] + f"{file_newname}")
            print(f"{file_newname} moved to {tag} folder")

