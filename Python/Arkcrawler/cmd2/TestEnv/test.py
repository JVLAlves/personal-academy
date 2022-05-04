import cmd2.REunion as reun

with open("arknew_near_light", 'r') as f:
    lines = f.readlines()
    print(lines)
    news = reun.Arknews(lines, "https://www.arknights.global/news/156")
    news.short()