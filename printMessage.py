# serverTest by Sidpatchy
# More info can be found on the GitHub here: https://github.com/Sidpatchy/Sidpatchy-s-Discord-Bot-Lib
# The serverTest allows you to list the number of servers and information about those servers discretely without having to bring your bot offline and without needing to write custom code for your bot.
# The bot uses ?servs for maximum discreteness


import discord
from discord.ext import commands
from discord.ext.commands import bot
import asyncio
import datetime as DT                           # Imports datetime as DT so instead of typing 'datetime.datetime.now()' you type 'DT.datetime.now()' it saves time and looks less dumb than 'datetime.datetime.now()'
import sLOUT as lout

# Checks time that bot was started
botStartTime = DT.datetime.now()

# Prefix to be entered before commmands. Ex. !test
bot = commands.Bot(command_prefix='?')      # In this case the prefix is '!' so before typing a command you type '!' and then 'test'
bot.remove_command('help')                  # Removes the default help command

# Notify in console when bot is loaded
@bot.event
async def on_ready():
    lout.log(botStartTime, None, lout.readConfig('bot.yml', 'botName'), True)

# The whole purpose of this file...
@bot.event
async def on_message(message):
    startTime = DT.datetime.now()
    print(message)
    channel = message.channel
    logChannel = 
    
    lout.log(startTime, 'message content printed', 'TestBot')



bot.run(lout.fetchToken('bot.yml'))
