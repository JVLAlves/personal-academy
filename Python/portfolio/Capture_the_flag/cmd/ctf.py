import os
import shutil
import paths as pts
import time
import ctf_hq as hq
from cleanschedule import Schedule

DOWNLOADS_DIR = pts.HOME + '/' + "Downloads"
def ctf():
    untagged = []


    files = os.listdir(DOWNLOADS_DIR)
    for file in files:
        tags_and_folders = pts.start()
        TAGS = list(tags_and_folders.keys())
        split_file = file.split("--")
        print(split_file)
        if len(split_file) < 2:
            untagged.append(file)
            continue
        tag = split_file[0]
        if not hq.isTag(tag):
            if file not in untagged:
                untagged.append(file)
            continue
        else:
            if not hq.tagExists(tag):
                isCreated = hq.verify_tag_window(tag).returnment()
                if isCreated:
                    files.append(file)
                continue

        file_newname = split_file[1]
        if tag in TAGS:
            shutil.move(pts.HOME + f"/Downloads/{file}", tags_and_folders[f"{tag}"])
            os.rename(tags_and_folders[f"{tag}"] + f"{file}", tags_and_folders[f"{tag}"] + f"{file_newname}")
            print(f"{file_newname} moved to {tag} folder")

    if len(untagged) > 0 :
        schedule = Schedule()
        if schedule.isTime():
            for file in untagged:
                print(file, "Got here")
                if not file.startswith("."):
                    os.remove(pts.HOME + f"/Downloads/{file}")
            schedule.UserSet()
        else:
            pass



if __name__ == "__main__":
    ctf()