import os


def verifynewsnumber(news_number):
    splitted_news_number = news_number.rsplit('/')
    news_number = splitted_news_number[2]
    news_register_dirpath = str(os.environ['HOME']) + '/desktop/arknights-news-portifolio/news-register'
    registerExists = os.path.exists(news_register_dirpath)

    if not registerExists:
        os.makedirs(news_register_dirpath)

    register_file = news_register_dirpath + "/.news_number_register.txt"
    register_fileExist = os.path.exists(register_file)
    if not register_fileExist:
        f = open(register_file, 'w')
        f.write(news_number)
        f.close()
        return True
    else:
        f = open(register_file, 'r')
        news_read = f.read()
        alreadyRead = news_read == news_number

        if not alreadyRead:
            return True
        else:
            return False


def createnewsportifolio(dirpath):
    isExists = os.path.exists(dirpath)

    if not isExists:
        os.makedirs(dirpath)


def writedown(paragraphs, images):
    dirpath = str(os.environ['HOME']) + "/desktop/arknights-news-portifolio"

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

verifynewsnumber('/news/142')