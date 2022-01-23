import filehelpers
import webhelpers
import adhelpers

url = "https://www.arknights.global"
news_url, news_number = webhelpers.getlatestnews(url)
notRead = filehelpers.verifynewsnumber(news_number)

if notRead:
    paragraphs, srcs = webhelpers.transcriptnews(news_url)

    filehelpers.writedown(paragraphs, srcs)
    adhelpers.newsnotification(paragraphs[0], "A new event was announced")
else:
    adhelpers.newsnotification("no 'new' news", "There is no new information.")

