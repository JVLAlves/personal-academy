#this module handles the information analysis with Regular Expressions
#TODO: map more efficiently the news text and make a full version of it with images
import logging
import re
import webbrowser

import PySimpleGUI as sg

from Amiya import Amiya
from cmd2.google import google as calendar

application_icon = "img/liskarm-icon.png"

TITLE_ONE = re.compile("^01\s(.*)\:\s(.*)$")
EVENT_DURATION = re.compile(
    "^EVENT DURATION:\s(\w+\s\d{1,2},\s\d{4},\s\d{2}\:\d{2}\s\(\w{3}\-\d{1}\)\s–\s\w+\s\d{1,2},\s\d{4},\s\d{2}\:\d{2}\s\(\w{3}\-\d{1}\))$")
STARTS_FROM = re.compile("^STARTS FROM:\s(\w+\s\d{1,2},\s\d{4},\s\d{2}\:\d{2}\s\(\w{3}\-\d{1}\))$")

TITLE_TWO = re.compile("^02\s(.*)$")

TITLE_THREE = re.compile("^03\s(.*)$")
OPERATOR_SEARCH = re.compile(
    "^(★{4,6}):\s(\w+.*)\s\[Limited\]\s\/\s(\w+)|^(★{4,6}):\s(\w+.*)\[Limited\]|^(★{4,6}):\s(\w+)\s\/\s(\w+)|^(★{4,6}):\s(\w+\s?\w*)\s")


SINGLE_NAMED_OPERATOR = re.compile("^(★+):\s(\w+)(?:\n|\s$)")
GROUP_SINGLE_NAMED_OPERATOR = re.compile("^(★+):\s(\w+)\s\/\s(\w+)(?:\n|\s$)")
SINGLE_NAMED_TAGGED_OPERATOR = re.compile("^(★+):\s(\w+)\s(?:\(.*\)|\[.*])(?:\n|\s$)")

TAG_LIMITED = re.compile(r"..*([\[\(]Limited[\]\)]).*")
TAGS = re.compile(r".*(\(.*\))(?:$|\n|\s$)|.*(\[.*])(?:$|\n|\s$)")
OUTFIT_TAG = re.compile(r"(\[.*])\s(?:.*)")
IS_OPERATOR = re.compile("^(★{3,6}):\s(\w+)(?:\s|\n)")
ALL_OPERATORS = re.compile("^(★+):\s(.*)(?:|\n|\s$)")


OUTFIT_STORE_UPDATE_TITLE = re.compile("^\d{2}\s(.*)\sAT\sOUTFIT\sSTORE")
DURATION = re.compile(
    "^DURATION:\s(\w+\s\d{1,2},\s\d{4},\s\d{2}\:\d{2}\s\(\w{3}\-\d{1}\)\s\S\s\w+\s\d{1,2},\s\d{4},\s\d{2}\:\d{2}\s\(\w{3}\-\d{1}\))$")
OUTFIT_STYLE = re.compile(
    "\d{2}\s(\D+)\s(?:(?<!AND )NEW\sARRIVALS|(?<!AND )RE-EDITION).*\sAT OUTFIT STORE")

OPERATORS_TITLE = re.compile("^\d{2}\s.*OPERATOR.*")

class Arknews:
    TWO_INDEX = -1
    THREE_INDEX = -1
    event_category = ""
    operators_stars = {}
    highlighted_operators = []
    outfits_available = []
    styles_available = []
    full_news = []
    news_abstract = []
    jumpable_duration = False
    jumpable_operators = False
    def __init__(self, new:list, url:str):
        self.url = url
        self.content = new
        for index, paragraphs in enumerate(self.content):
            self.full_news.append(paragraphs)
            # 01 TITLE
            if re.match(TITLE_ONE, paragraphs):
                self.news_abstract.append(paragraphs)
                logging.info(re.findall(TITLE_ONE, paragraphs))
                self.event_category, self.event_name=re.findall(TITLE_ONE, paragraphs)[0]

            ## EVENT DURATION
            if  self.event_category == "SIDE STORY" or "NEW STORY COLLECTION EVENT":
                if re.match(EVENT_DURATION, paragraphs):
                    self.news_abstract.append(paragraphs)
                    logging.info(re.findall(EVENT_DURATION, paragraphs))
                    self.event_duration = re.findall(EVENT_DURATION, paragraphs)[0]
            elif self.event_category == "NEW MAIN STORYLINE OPEN":
                self.news_abstract.append(paragraphs)
                if re.match(EVENT_DURATION, paragraphs):
                    logging.info(re.findall(EVENT_DURATION, paragraphs))
                    self.event_duration = re.findall(EVENT_DURATION, paragraphs)[0]

            # 02 TITLE
            if re.match(TITLE_TWO, paragraphs):
                self.news_abstract.append(paragraphs)
                self.TWO_INDEX = index

            ## 02 DURATION
            if not self.jumpable_duration and self.TWO_INDEX < index:
                if re.match(DURATION, paragraphs):
                    self.news_abstract.append(paragraphs)
                    self.jumpable_duration = True

            ## 02 OPERATORS
            if not self.jumpable_operators and (self.THREE_INDEX != -1 and self.TWO_INDEX < index):
                if re.match(OPERATOR_SEARCH, paragraphs):
                    self.news_abstract.append(paragraphs)
                    self.jumpable_operators = True

            #03 TITLE
            if re.match(TITLE_THREE, paragraphs):
                self.news_abstract.append(paragraphs)
                self.THREE_INDEX = index
                self.jumpable_duration = False
                self.jumpable_operators = False

            ## 03 DURATION
            if not self.jumpable_duration and (self.THREE_INDEX != -1 and self.THREE_INDEX < index):
                if re.match(DURATION, paragraphs):
                    self.news_abstract.append(paragraphs)
                    self.jumpable_duration = True

            ## 03 OPERATORS
            if not self.jumpable_operators and self.THREE_INDEX < index:
                if re.match(OPERATOR_SEARCH, paragraphs):
                    self.news_abstract.append(paragraphs)
                    self.jumpable_operators = True

            # OPERATORS
            if re.match(IS_OPERATOR, paragraphs):
                logging.info(repr(paragraphs))
                logging.info(re.findall(IS_OPERATOR, paragraphs))
                collect = re.findall(ALL_OPERATORS, paragraphs)[0]
                collection = list(collect)
                logging.info(collection)
                recollection = []
                for data in collection:
                    if data.find(" / ") != -1:
                        data = data.split(" / ")
                        for d in data:
                            recollection.append(d)
                    else:
                        recollection.append(data)
                logging.info(recollection)
                collection = tuple(recollection)
                star_count, *operators = collection
                logging.info(f"STAR COUNT: {star_count}, OPERATOR NAME: {operators}")

                for operator in operators:
                    logging.info(f"{repr(operator)}, {re.match(TAGS, operator)}")
                    if re.match(TAGS, operator):
                        tag_list = []
                        logging.info(f"Tags: {re.findall(TAG_LIMITED, operator)}")
                        limited_tag_list = re.findall(TAG_LIMITED, operator)
                        if len(limited_tag_list) != 0:
                            if limited_tag_list[0]!= '':
                                tag_list.append(limited_tag_list[0])
                        tag , *blank = re.findall(TAGS, operator)[0]
                        if tag != '':
                            tag_list.append(tag)

                        for b in blank:
                            if b != '':
                                tag_list.append(b)



                        logging.info(f"tags found tags: {tag_list if len(tag_list) != 0 else None}")
                        for tag in tag_list:
                            operator = operator.replace(tag, "").strip()

                    if operator not in self.operators_stars.keys():
                        self.operators_stars[operator] = star_count
                    if operator not in self.highlighted_operators:
                        self.highlighted_operators.append(operator)

            # OUTFIT STORE
            if re.match(OUTFIT_STYLE, paragraphs):
                self.news_abstract.append(paragraphs)
                logging.info(re.findall(OUTFIT_STYLE, paragraphs))
                style = re.findall(OUTFIT_STYLE, paragraphs)[0]
                logging.info(style)
                if re.match(OUTFIT_TAG, style):
                    logging.info(f"tags found in outfit brand: {re.findall(OUTFIT_TAG, style)}")
                    tag = re.findall(OUTFIT_TAG, style)[0]
                    style = style.replace(tag, "").strip()
                    logging.info(f"tag of outfit: {tag}")
                if style.find("&") != -1:
                    styles = style.split("&")
                    for s in styles:
                        if s not in self.styles_available:
                            s = s.title()
                            if s == "Epoque":
                                s = s.upper()
                                s += "Collection"
                            self.styles_available.append(s)
                else:
                    style = style.title()
                    if style == "Epoque":
                        style = style.upper()
                        style += " Collection"
                    self.styles_available.append(style)
                logging.info(f"Styles list: {self.styles_available}")
            if len(self.styles_available) != 0:
                for style in self.styles_available:
                    if re.match(f"{style}\s\S\s(.*)$", paragraphs):
                        logging.info(paragraphs)
                        self.news_abstract.append(paragraphs)
                        logging.info(re.findall(f"{style}\s\S\s(.*)$", paragraphs))
                        outfit = re.findall(f"{style}\s\S\s(.*)$", paragraphs)[0]
                        self.outfits_available.append(outfit)
        self.title = f"{self.event_category}: {self.event_name}"
    def short(self):

        layout = [
            [sg.VPush(), sg.Push(), sg.Text(f"{self.event_category}: {self.event_name}", font="Arial 16 bold"), sg.Push()],
            [sg.Push(), sg.Text(f"{self.event_duration}", font="Arial 14"), sg.Button("Add to Agenda", key="-add-"), sg.Push()],
            [sg.VPush(), sg.VPush(), sg.Text(f"HIGHLIGHTED OPERATORS:", font="Arial 14 bold")],
        ]

        for operator in self.highlighted_operators:
            line = [sg.Button(f"{operator}", font="Arial 12", key=f"{operator}")]
            layout.append(line)
        layout.append([sg.VPush()])
        layout.append([sg.VPush(), sg.Text(f"OUTFITS AVAILABLE:", font="Arial 14 bold")])
        for outfit in self.outfits_available:
            line = [sg.Text(f"{outfit}", font="Arial 12")]
            layout.append(line)
        layout.append([sg.VPush(), sg.Push(), sg.Button("see on page", key="-see-"),sg.VPush()])

        window = sg.Window(f"{self.event_name}", icon=application_icon).layout(layout).finalize()
        window.bind("<Key-Escape>", "esc")

        while True:
            event, _ = window.Read()
            logging.info(event)
            if event == sg.WIN_CLOSED or event == "esc":
                break
            elif event == "-see-":
                webbrowser.open(self.url)
            elif event == "-add-":
                try:
                    created = calendar.CreateEvent(self.title, self.event_duration)
                except Exception as Exp:
                    sg.popup_error(Exp)
                    logging.error("Error in creating event on Google Calendar")
                else:
                    if created:
                        sg.popup("Event Created")
                        logging.info("Event Created successfully")
                    else:
                        sg.popup_error("Event already over")
                        logging.error("Event already over")
            elif not (event == "-add-" or event == "-see-"):
                try:
                    logging.info(f"Searching for operator {event}")
                    op = Amiya.liskcraw(event)
                except Exception as Exp:
                    sg.popup_error(Exp)
                    logging.error("Operator not found")
                else:
                    logging.info("Operator found successfully")
                    op_win = Amiya.Operator_window(op)
                    op_win.init()

        window.close()



