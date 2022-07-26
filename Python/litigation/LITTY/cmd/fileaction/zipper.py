import datetime
import os
import shutil
import LITTY.glob.globals as glob


#track the automatically generated files through the File Watermark
def track(path:str):
    Track = [] #files which will be zipped

    #list the files in the current directory
    files = os.listdir(path)

    #check the file name by the file Watermark and Extension
    for file in files:

        #if ends with the Watermark and the correct Extension, it wll be appended to the Track list.
        if file.endswith(glob.FILE_WATERMARK + glob.FILE_EXTENSION):
            Track.append(file)
        else:
            print("Never mind!")
    return Track


#create a directory, move and rename the files on it
def makefile(files:list, path:str):
    dt = datetime.datetime
    dt_today = dt.now() # the datetime of today
    today = dt_today.strftime(glob.FILE_DATETIME_FORMAT) # stringfy the datetime of today
    os.mkdir(today) # the directory name must be the datetime
    dirpath = path + "/" + today # the path for the directory

    # iterate through the files with the file Watermark
    for file in files:
        file_newname = file.replace(f"{glob.FILE_WATERMARK}", "") # remove the file Watermark
        os.rename(file, file_newname) # rename the file
        shutil.move(file_newname, dirpath) # move it to the directory
    return dirpath

# zip the file and delete the directory
def ZipAndClose(dirpath:str, automation_name:str):

    global filename  # file name to zip it

    # in case of not assigned name for the zip file, use the datetime of today
    if automation_name == "":
        dt = datetime.datetime
        dt_today = dt.now()  # the datetime of today
        today = dt_today.strftime(glob.FILE_DATETIME_FORMAT)  # stringfy the datetime of today
        filename = today

    # in case of not None, the name of the zip file is the assigned one
    else:
        dt = datetime.datetime
        dt_today = dt.now()  # the datetime of today
        today = dt_today.strftime(glob.FILE_DATETIME_FORMAT)  # stringfy the datetime of today
        filename = automation_name+f"_{today}"


    # zip the file in the indicated directory path
    # also, it will be needed to indicate the name of the zipped file
    shutil.make_archive(filename, "zip", dirpath)

    # delete the directory with the files on it
    shutil.rmtree(dirpath)