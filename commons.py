# -*- coding: utf-8 -*-
"""
Created on Sun May 21 14:22:00 2017

@author: Ivan Ortiz
"""

import json
import unicodedata
import urllib
from urllib.request import Request, urlopen
from urllib.parse import quote
import hearthstoneDeckList

#Local Urls
_DECK_LIST_FILE = "deckList.txt"

#Bot stuff
BOT_TOKEN = "YourBotToken"
BOT_DESCRIPTION = "Hearthstone Bot"
COMMAND_PREFIX = '.'

# URLS:
_SINGLE_CARD_URL = "https://omgvamp-hearthstone-v1.p.mashape.com/cards/"
_CARD_SEARCH_URL = "https://omgvamp-hearthstone-v1.p.mashape.com/cards/search/"



def loadDeckList():
    deckList = hearthstoneDeckList.hearthstoneDeckList()
    f = open(_DECK_LIST_FILE, 'r', encoding='utf-8')
    className = ""
    for line in f:
        line = line[:-1]
        if(deckList.checkClass(line)):
            className = line
        elif(line != ""):
            if(className != ""):
                deckList.importDeck(className, line)
            else:
                print("Error!")
    return deckList



def saveDeckList(deckList: hearthstoneDeckList.hearthstoneDeckList):
    string = deckList.exportDeckList()
    f = open(_DECK_LIST_FILE, 'w', encoding='utf-8')
    f.write(string)


def removeAccents(string):
    s = ''.join((c for c in unicodedata.normalize('NFD',str(string)) if unicodedata.category(c) != 'Mn'))
    return s


async def _fetchGet(url, request, locale="esES"):
    error = False
    request = Request(url+quote(request)+"?locale="+locale)
    request.add_header("X-Mashape-Key", "1RuRTcmiUumshnybOhBVGWJgDi7xp1PvJEOjsnlFFwa0R3uPQ5")
    try:
        info = urlopen(request).read()
        jsonResponse = json.loads(info.decode('utf-8'))
        return(jsonResponse)
    except urllib.error.HTTPError:
        return(-1)


async def getSingleCard(cardName, lang="esES"):
    info = await _fetchGet(_CARD_SEARCH_URL, cardName, locale=lang)
    if info == -1:
        info = await _fetchGet(_CARD_SEARCH_URL, cardName, locale="enUS")
    return info


async def getCardByID(cardId, lang="esES"):
    return(await _fetchGet(_SINGLE_CARD_URL,cardId,locale=lang))


async def getSingleCardEnglishImage(cardId, imgType):
    cardInfo = await _fetchGet(_SINGLE_CARD_URL, cardId, locale="enUS")
    return(cardInfo[0][imgType])
