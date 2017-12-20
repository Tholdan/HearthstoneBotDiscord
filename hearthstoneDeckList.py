# -*- coding: utf-8 -*-
"""
Created on Tue May 23 16:22:00 2017

@author: Ivan Ortiz
"""

class hearthstoneDeckList:
    deckList = {"Brujo" : [], "Cazador" : [], "Chamán" : [], "Druida" : [], "Guerrero" : [],
                "Mago" : [], "Paladín" : [], "Pícaro" : [], "Sacerdote" : []}

    def __init__(self):
        pass

    def __str__(self):
        string = ""
        for className in self.deckList:
            string += ("__**" + className + "**:__\n")
            if not self.deckList[className]:
                string += ("**  **No hay mazos disponibles para esta clase.\n")
            for deck in self.deckList[className]:
                string += ("**  **" + u"\u2022 " + str(deck) + "\n")
        return(string)

    def checkClass(self, className: str):
        return(className in self.deckList)

    def getClassDecks(self, className: str):
        string = ""
        if className in self.deckList:
            string += "__**" + className + "**:__\n"
            if not self.deckList[className]:
                string += ("**  **No hay mazos disponibles para esta clase.\n")
            for deck in self.deckList[className]:
                string += ("**  **" + u"\u2022 " + str(deck) + "\n")
        return(string)

    def addDeck(self, className: str, deckName: str, deckCost: int, deckUrl: str):
        if className in self.deckList:
            self.deckList[className].append("**" + deckName + "** - Coste: " + str(deckCost) + " de polvo - <" + deckUrl + ">")

    def removeDeck(self, className: str, deckName: str):
        found = False
        if className in self.deckList:
            for deck in self.deckList[className]:
                deckNParts = deck.split("**")
                deckN = deckNParts[1]
                if (deckName == deckN):
                    found = True
                    self.deckList[className].remove(deck)
        return found

    def exportDeckList(self):
        string = ""
        for className in self.deckList:
            string += (str(className) + "\n")
            for deck in self.deckList[className]:
                string += (str(deck) + "\n")
        return(string)

    def importDeck(self, className:str, deck: str):
        self.deckList[className].append(deck)
