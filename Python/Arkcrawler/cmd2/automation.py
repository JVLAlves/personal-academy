
import os
import time

import schedule
import originum as ori
from REunion import *
import google.google as google
import Amiya.Amiya as amiya
def automates():
    config = ori.Config()
    print(config.sections())
    liskarm = config["liskarm"]

    if eval(liskarm["automation"]):
        news_type = liskarm["news_type"]
        news_category = liskarm["news_category"]
        latest_news = liskarm["latest"]
        hrefs = ori.Search(news_type, news_category)
        if len(hrefs) == 1:
            securety_counter = 0
            for href in hrefs:
                securety_counter += 1
                print(securety_counter)
                if href == latest_news:
                    break
                else:
                    text_content, link = ori.Focus(href)
                    liskarm["latest"] = href

                    with open(f".{href.replace('/', '-')}.txt", "x") as file:
                        for line in text_content:
                            file.write(f"{line}\n")

                    with open(f".{href.replace('/', '-')}.txt", 'r') as f:
                        lines = f.readlines()
                    os.remove(f".{href.replace('/', '-')}.txt")

                    if eval(liskarm["interface_call"]):
                        arknews = Arknews(lines, link)
                        arknews.short()
                    else:
                        arknews = Arknews(lines, link)
                        if liskarm["last_google_event_created"] != arknews.event_name:
                            description = "Highlighted Operators: \n"
                            for oper in arknews.operators_stars.keys():
                                operator = amiya.search_operator(oper)
                                presentation = f"\n{arknews.operators_stars[oper]}: {oper} ({operator['url']})"
                                description += presentation
                            description += "\n\nOutfits availabe:\n"
                            for outfit in arknews.outfits_available:
                                presentation = f"\n{outfit}"
                                description += presentation

                            print(description)
                            if google.CreateEvent(arknews.event_name, arknews.event_duration, description=description):
                                liskarm["last_google_event_created"] = arknews.event_name
                        else:
                            pass

        with open(ori.CONFIG_FILE, "w") as ConfigFile:
            config.write(ConfigFile)

def automation():

    schedule.every(12).hours.do(automates())

    while 1:
        schedule.run_pending()
        time.sleep(1)