import webhelpers
import oshelpers

url = "https://www.arknights.global"
news_url = webhelpers.getlatestnews(url)

paragraphs, srcs = webhelpers.transcriptnews(news_url)

for p in paragraphs:
    print(p)
for img in srcs:
    print(img)