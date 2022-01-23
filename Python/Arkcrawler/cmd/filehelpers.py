import os

def createnewsportifolio(dirpath):

    isExists = os.path.exists(dirpath)

    if not isExists:
        os.makedirs(dirpath)

def writedown(paragraphs, images):
    dirpath = str(os.environ['HOME']) + "/desktop/arknights-news-portfolio"

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

    f = open(title, "w")

    for line in paragraphs:
        f.write(line + "\n")

    f.write("\n")
    f.write("Get the images displayed in the news by acessing this urls:")
    f.write("\n")
    for url in images:
        f.write(url + "\n")

    f.close()
