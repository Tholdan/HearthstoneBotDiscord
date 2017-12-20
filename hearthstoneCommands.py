# -*- coding: utf-8 -*-
"""
Created on Sun May 21 14:22:00 2017

@author: Ivan Ortiz
"""

import commons
import discord
import random
import hearthstoneDeckList

async def getDeckCommand(bot, deckList: hearthstoneDeckList, ctx):
    commands = ctx.message.content.split(" ")
    if(len(commands) < 2):
        await bot.say(str(deckList))
    else:
        className = commands[1]
        className = className[0].upper() + className[1:]
        if className == "Chaman":
            className = "Chamán"
        if className == "Paladin":
            className = "Paladín"
        if className == "Picaro":
            className = "Pícaro"
        if deckList.checkClass(className):
            string = deckList.getClassDecks(className)
            await bot.say(string)
        else:
            await bot.say("**No he podido encontrar la clase especificada.**")

async def addDeckCommand(bot, deckList: hearthstoneDeckList, ctx):
    commands = ctx.message.content.split(" ")
    nCommands = len(commands)
    if (nCommands < 5):
        await bot.say("**Formato:** " + commons.COMMAND_PREFIX + "addDeck className deckName cost hearthpwnUrl")
    else:
        className = commands[1]
        className = className[0].upper() + className[1:]
        if className == "Chaman":
            className = "Chamán"
        if className == "Paladin":
            className = "Paladín"
        if className == "Picaro":
            className = "Pícaro"
        if (nCommands > 5):
            deckName = ""
            for i in range(2, nCommands-3):
                deckName += (commands[i] + " ")
            deckName += commands[nCommands-3]
        else:
            deckName = commands[2]
        cost = int(commands[nCommands-2])
        deckUrl = commands[nCommands-1]
        if deckList.checkClass(className):
            if "http://www.hearthpwn.com" in deckUrl:
                deckList.addDeck(className, deckName, cost, deckUrl)
                commons.saveDeckList(deckList)
                await bot.say("**Mazo añadido correctamente!**")
            else:
                await bot.say('**La url especificada no es válida, introduce una url que contenga "http://www.hearthpawn".**')
        else:
            await bot.say("**No he podido encontrar la clase especificada.**")

async def removeDeckCommand(bot, deckList: hearthstoneDeckList, ctx):
    commands = ctx.message.content.split(" ")
    nCommands = len(commands)
    if (len(commands) < 3):
        await bot.say("**Formato:** " + commons.COMMAND_PREFIX + "removeDeck className deckName")
    else:
        className = commands[1]
        className = className[0].upper() + className[1:]
        if className == "Chaman":
            className = "Chamán"
        if className == "Paladin":
            className = "Paladín"
        if className == "Picaro":
            className = "Pícaro"
        if (nCommands > 3):
            deckName = (commands[2] + " ")
            for i in range(3, nCommands-1):
                deckName += (commands[i] + " ")
            deckName += commands[nCommands-1]
        else:
            deckName = commands[2]
        if deckList.checkClass(className):
            found = deckList.removeDeck(className, deckName)
            commons.saveDeckList(deckList)
            if (found):
                await bot.say("**Mazo eliminado correctamente!**")
            else:
                await bot.say("**No he podido encontrar el mazo especificado.**")
        else:
            await bot.say("**No he podido encontrar la clase especificada.**")

async def getCardCommand(bot, ctx):
    commands = ctx.message.content.split(" ")
    command = commands[0].lower()
    if len(commands) < 2:
        await bot.say("**Formato:** " + commons.COMMAND_PREFIX + "card/goldCard cardName")
    else:
        if command == commons.COMMAND_PREFIX + "card":
            imgType = "img"
        else:
            imgType = "imgGold"

        if command == commons.COMMAND_PREFIX + "card":
            cardName = ctx.message.content[6:]
        elif command == commons.COMMAND_PREFIX + "gcard":
            cardName = ctx.message.content[7:]
        else:
            cardName = ctx.message.content[10:]

        cards = await commons.getSingleCard(cardName)

        if cards == -1:
            await bot.say("**Lo siento, no he podido encontrar la carta.**")
        else:
            found = False
            prevCard = 0
            sameCard = False
            for card in cards:
                if prevCard != 0:
                    sameCard = prevCard in card
                if imgType in card and card['type'] != "Hero" and card['type'] != "Enchantment" and card['type'] != "Hero Power" and not sameCard:
                    cardName = commons.removeAccents(cardName).lower()
                    name = commons.removeAccents(card['name']).lower()
                    if cardName == name or (cardName in name and len(cards) == 1):
                        found = True
                        imageUrl = await commons.getSingleCardEnglishImage(card['cardId'], imgType)
                        imgEmbed = discord.Embed().set_image(url=imageUrl)
                        await bot.send_message(ctx.message.channel, embed=imgEmbed)
                        prevCard = card


            if not found:
                msg = "**Lo siento, no he podido encontrar la carta.**\n\nQuizás quisiste decir:"
                if len(cards) <= 6:
                    sameCard = False
                    for card in cards:
                        if prevCard != 0:
                            sameCard = prevCard in card
                        if card['type'] != "Hero" and card['type'] != "Enchantment" and card['type'] != "Hero Power" and not sameCard:
                            msg = msg+("\n**   **- " + card['name'])
                else:
                    indexList = []
                    for i in range(6):
                        indexList.append(random.randint(0, len(cards)-1))
                    indexList.sort()

                    for index in indexList:
                        if cards[index]['type'] != "Hero" and cards[index]['type'] != "Enchantment" and cards[index]['type'] != "Hero Power":
                            msg = msg + ("\n**    **- " + cards[index]['name'])
                await bot.say(msg)
