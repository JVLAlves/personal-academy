import os
import glob
import consts


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

    if not isExists:
        os.makedirs(dirpath)


def writedown(file, paragraphs, images):

    f = open(file, "w")

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
