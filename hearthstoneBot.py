# -*- coding: utf-8 -*-
"""
Created on Sun May 21 14:22:00 2017

@author: Ivan Ortiz
"""

import commons
import hearthstoneCommands
import hearthstoneDeckList
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix=commons.COMMAND_PREFIX, description=commons.BOT_DESCRIPTION)
bot.remove_command("help")
deckList = commons.loadDeckList()

@bot.event
async def on_ready():
    print('Logged in as:')
    print('Name: ' + bot.user.name)
    print('ID: ' + bot.user.id)

@bot.event
async def on_command_error(error, ctx):
    print(error)

#Command format: !card cardName(cardName can contain spaces)
@bot.command(aliases=['card', 'Card', 'gcard', 'Gcard', 'gCard', 'GCard', 'goldcard', 'Goldcard', 'goldCard', 'GoldCard'], pass_context=True)
async def getCardCommand(ctx):
    await hearthstoneCommands.getCardCommand(bot, ctx)

@bot.command(aliases=['deck', 'Deck', 'decks', 'Decks', 'mazo', 'Mazo', 'mazos', 'Mazos', 'decklist', 'deckList'], pass_context=True)
async def getDecksCommand(ctx):
    await hearthstoneCommands.getDeckCommand(bot, deckList, ctx)

@bot.command(aliases=['adddeck', 'addDeck'], pass_context=True)
async def addDecksCommand(ctx):
    await hearthstoneCommands.addDeckCommand(bot, deckList, ctx)

@bot.command(aliases=['removedeck', 'removeDeck'], pass_context=True)
async def removeDeckCommand(ctx):
    await hearthstoneCommands.removeDeckCommand(bot, deckList, ctx)

@bot.command(aliases=['help', 'ayuda', 'hearthstonehelp', 'hearthstoneHelp'])
async def helpCommand():
    await bot.say("__**Comandos disponibles:**__\n**  **" + u"\u2022 " + "**" + commons.COMMAND_PREFIX + "card** *cardName* : Muestra la imagen de la carta especificada.\n"
                                                  "**  **" + u"\u2022 " + "**" + commons.COMMAND_PREFIX + "goldCard** *cardName* : Muestra la imagen de la carta especificada en su versión dorada.\n"
                                                  "**  **" + u"\u2022 " + "**" + commons.COMMAND_PREFIX + "deck** *<className>(Opcional)* : Muestra lista de mazos total o de la clase especificada.\n"
                                                  "**  **" + u"\u2022 " + "**" + commons.COMMAND_PREFIX + "addDeck** *className deckName cost hearthpwnUrl* : Añade el mazo especificado a la lista de mazos.\n"
                                                  "**  **" + u"\u2022 " + "**" + commons.COMMAND_PREFIX + "removeDeck** *className deckName* : Elimina el mazo especificado de la lista de mazos.\n")

def main():
    bot.run(commons.BOT_TOKEN)

if __name__ == "__main__":
    main()