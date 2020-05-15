# serverTest by Sidpatchy
# More info can be found on the GitHub here: https://github.com/Sidpatchy/Sidpatchy-s-Discord-Bot-Lib
# The serverTest allows you to list the number of servers and information about those servers discretely without having to bring your bot offline and without needing to write custom code for your bot.
# The bot uses ?servs for maximum discreteness


import discord
from discord.ext import commands
from discord.ext.commands import bot
import asyncio
import datetime as DT                           # Imports datetime as DT so instead of typing 'datetime.datetime.now()' you type 'DT.datetime.now()' it saves time and looks less dumb than 'datetime.datetime.now()'
import sid

# Checks time that bot was started
botStartTime = DT.datetime.now()

# Prefix to be entered before commmands. Ex. !test
bot = commands.Bot(command_prefix='?')      # In this case the prefix is '!' so before typing a command you type '!' and then 'test'
bot.remove_command('help')                  # Removes the default help command

# Handles what needs to be printed in the console
def consoleOutput(commandName, commandTime):    # Defines consoleOutput()
    startTime = commandTime                     # (laziness) passing startTime from the beginning of the command into the function
    timeToRun = DT.datetime.now() - startTime
    print('')
    print('---------TestBot----------')         # Divider to make console readable
    print('Time to Run:', timeToRun)            # Prints how long it took the bot to run the command
    print('Current Time:', DT.datetime.now())   # Prints time command was run in the console, from the variable 'currentDT'
    print(commandName, 'has been run')          # Prints 'test has been run' in console
    print('--------------------------')         # Divider to make console readable

# Notify in console when bot is loaded
@bot.event
async def on_ready():
    print('---------TestBot----------')
    timeToLoad = DT.datetime.now() - botStartTime
    print('Time to load:', timeToLoad)              # Prints the time to load
    print('Current Time:', DT.datetime.now())       # Prints current time in console
    print('Done Loading!')                          # Prints 'Done Loading!' in console
    print('--------------------------')

# The whole purpose of this file...
@bot.command(pass_context=True)
async def servs(ctx):
    startTime = DT.datetime.now()
    numberOfServers = len(bot.guilds)
    await ctx.send(numberOfServers)
    await ctx.send(bot.guilds)
    consoleOutput('servers', startTime)

bot.run(sid.retrieveToken())
