import os
import glob
import consts


<<<<<<< HEAD
def verifynewsnumber(news_number):
    splitted_news_number = news_number.rsplit('/')
    news_number = splitted_news_number[2]
    news_register_dirpath = str(os.environ['HOME']) + '/arknights-news-portifolio/news-register'
    registerExists = os.path.exists(news_register_dirpath)
=======
def verifyExistentFiles(incomingFiles):
>>>>>>> 87f4dbc66585fab46bb38f3efcbeab5ae8f049a3

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


<<<<<<< HEAD
def writedown(paragraphs, images):
    dirpath = str(os.environ['HOME']) + "/arknights-news-portifolio"

    createnewsportifolio(dirpath)
    title = ''
    if paragraphs[0] != "":
        titleline = paragraphs[0].replace(" ", "_") + ".txt"
        title = dirpath + "/" + titleline
    else:
        for p in paragraphs:
            if p != "":
                titleline = p.replace(" ", "_")
                title = dirpath + "/" + titleline
                break
=======
def writedown(file, paragraphs, images):
>>>>>>> 87f4dbc66585fab46bb38f3efcbeab5ae8f049a3

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
