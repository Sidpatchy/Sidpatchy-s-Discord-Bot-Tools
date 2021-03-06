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
    lout.log('bot.yml', botStartTime, None, None, True)

# The whole purpose of this file...
@bot.command(pass_context=True)
async def servs(ctx):
    startTime = DT.datetime.now()
    guildsList = str(bot.guilds)
    guildsList = guildsList.replace('[', '')
    guildsList = guildsList.replace(']', '')
    guildsList = guildsList.split(",")
    names = []
    members = 0
    for i in guildsList:
        i = i.split(' ')
        name = i[3]
        name = name.replace('\'', '')
        name = name.replace('name=', '')
        names.append(name)

        member = i[6]
        member = member.replace('member_count=', '')
        members = members + str(member)

    for i in names:
        print(i)
    
    print('Member Count:', members)


    lout.log('bot.yml', startTime, 'servs; number of servers: {}'.format(len(bot.guilds)))

bot.run(lout.fetchToken('bot.yml'))
