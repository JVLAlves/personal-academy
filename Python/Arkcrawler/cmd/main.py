import webhelpers
import adhelpers
import filehelpers

url = "https://www.arknights.global"
news_url = webhelpers.getlatestnews(url)

paragraphs, srcs = webhelpers.transcriptnews(news_url)

filehelpers.writedown(paragraphs, srcs)

