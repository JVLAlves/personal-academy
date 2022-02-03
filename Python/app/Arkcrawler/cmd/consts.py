
# Variável que indica a necessidade de imprimir todas as noticias que existem na pagina
import os

GET_ALL = True
GET_LATESTS = False
GET_EVENTS = False
GET_CONTESTS = False
NEWS_BOX_XPATH = "//div[@class='news-box-wrap']/a[@class='news-box']"
DEBUGMODE = False

DIR_PATH = str(os.environ['HOME']) + "/desktop/arknights-news-portifolio"