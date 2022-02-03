import logging
import os
import glob
import time

from app.Arkcrawler.cmd import consts


def verifyExistentFiles(incomingFiles):

    filesRef = listExistentFiles()
    inCommon = set(filesRef).intersection(incomingFiles)
    if len(incomingFiles) == len(inCommon):

        return True, None
    else:
        for files in inCommon:
            incomingFiles.remove(files)
        return False, incomingFiles




def createnewsportifolio(dirpath):

    isExists = os.path.exists(dirpath)
    logging.info(f'PATH "{dirpath}" already exists.')

    if not isExists:
        os.makedirs(dirpath)
        time.sleep(2)
        logging.info(f'PATH "{dirpath}" did not exists. Now it was created.')


def writedown(file, paragraphs, images):

    try:
        f = open(file, "w")
    except:
        logging.fatal(f"NOT ABLE TO CREATE FILE NAMED '{file}'.")
    else:
        for line in paragraphs:
            f.write(line + "\n")

        f.write("\n")
        f.write("Get the images displayed in the news by acessing this urls:")
        f.write("\n")

        for url in images:
            f.write(url + "\n")

        f.close()

def listExistentFiles():
    dirpathsearch = str(os.environ['HOME']) + "/desktop/arknights-news-portifolio/*/*"
    files = glob.glob(dirpathsearch)
    return files

def init():

    createnewsportifolio(consts.DIR_PATH)
    createnewsportifolio(consts.DIR_PATH + '/logs')

    createnewsportifolio(consts.DIR_PATH + '/contest')
    createnewsportifolio(consts.DIR_PATH + '/events')
    createnewsportifolio(consts.DIR_PATH + '/etc')

    logging.info(f'FILE HELPERS INITIALIZED SUCCESSFULLY.')
