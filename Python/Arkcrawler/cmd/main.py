import filehelpers
import webhelpers

files = []
dictAllNews = {}
url = "https://www.arknights.global"

filehelpers.init()
news_numbers = webhelpers.getlatestnews(url)

for num in news_numbers:
    news_url = url + num
    news = webhelpers.getContent(news_url)
    files.append(news["path"])
    dictAllNews.update({news["path"]: news})

alreadyExists, fileQueue = filehelpers.verifyExistentFiles(files)

if not alreadyExists:
    for file in fileQueue:
        filehelpers.writedown(file, dictAllNews[file]["paragraphs"], dictAllNews[file]["srcs"])
else:
    print("There is nothing to see here.")