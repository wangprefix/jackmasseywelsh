import asyncio
import discord
import logging
import time
import random
from discord.ext.commands import Bot
from discord.ext import commands
prefix = "j."

client = commands.Bot(command_prefix=prefix)
helloRes = ["Hello! ", 'Hiya! ', 'Chip Chap ', 'Top of the morning to you laddy! ', 'Heelllllooooo. ', 'This is Augustus! :bear: ', 'Ight! ']
suffixBuy = ["SucksAtMC ", "LilScumbag ", "the Diddler ", "420 ", "Toixc ", "the Raider ", "the Hacker ", "PVP God ", "the Dictator ", "the Savage ", "the Lad ", "the Wang ", "Xx_xX "]

#playing j.help
@client.event
async def on_ready():
    print("Logged in as:")
    print(client.user.name)
    print(client.user.id)
    print('------------------')
    await client.change_status(game=discord.Game(name='j.help'))

#j.ping
@client.command(pass_context=True)
async def ping(ctx):
    await client.say("Pong!")
    print("Running j.ping!")
    print('------------------')

#j.rules
@client.command(pass_context=True)
async def rules(ctx):
    await client.say("Hacker Catching Rules:")
    await client.say("1. You can not diddle a diddle boy.")
    await client.say("2. Only a diddle boy can diddle a diddle boy.")
    await client.say("3. Buy the Wang Suffix")
    await client.say("4. You can't mess with a hacker's base unless we tp to them while they are at their base")
    print("Running j.rules!")
    print('------------------')

#j.burrito
@client.command(pass_context=True)
async def burrito(ctx):
    await client.say("https://www.youtube.com/watch?v=38zGVX7ewLI")
    print("Running j.burrito!")
    print('------------------')

#j.suffix
@client.command(pass_context=True)
async def suffix(ctx):
    random.seed(time.time())
    choiceSuffix = suffixBuy[random.randint(0, len(helloRes) - 1)]
    await client.say("Buy the " + choiceSuffix + "Suffix! " + "Avalible only at store.skycade.net!")
    print("Running j.suffix!")
    print('------------------')
    
#j.say
@client.command(pass_context = True)
async def say(ctx, *, say: str):
    await client.delete_message(ctx.message)
    await client.say(say)
    print("Running j.say!")
    print('------------------')

#j.scumbag
@client.command(pass_context = True)
async def scumbag(ctx, *, member : discord.Member = None):
    await client.say(ctx.message.author.mention + ", you little scumbag!")
    print("Running j.scumbag!")
    print('------------------')

#j.hug
@client.command(pass_context = True)
async def hug(ctx, *, member : discord.Member = None):
    print("Running j.hug")
    print('------------------')
    if member is None:
        await client.say(ctx.message.author.mention + " has been hugged!")
    elif member.id == "345642624348192788":
        await client.say("That's not physically possible.")
    elif member.id == ctx.message.author.id:
            await client.say(ctx.message.author.mention + " got hugged!")
    else:
        await client.say(member.mention + " has been hugged by Jack!")

#j.contribute
@client.command(pass_context = True)
async def contribute(ctx, *, member : discord.Member = None):
    await client.say(ctx.message.author.mention + ", here's the list of contributers:")
    await client.say("ShadowWizard")
    await client.say("BuyTheWangSuffix")
    await client.say("xCgKing23")
    await client.say("5BeanBurritos")
    await client.say("Potato Joe")
    await client.say("Erin")
    await client.say("EatDatFood")
    await client.say("HejaSwezo")
    print("Running j.contribute!")
    print('------------------')

#j.weatherspoons
@client.command(pass_context = True)
async def weatherspoons(ctx):
    await client.say(ctx.message.author.mention + " have you been at WeatherSpoons?")
    print("Running j.weatherspoons!")
    print('------------------')
    
#j.eyy
@client.command(pass_context = True)
async def eyy(ctx):
    await client.say("Eyy up! " + ctx.message.author.mention)
    print("Running j.eyy!")
    print('------------------')
    
#j.hello
@client.command(pass_context = True)
async def hello(ctx, *, member : discord.Member = None):
    random.seed(time.time())
    choice = helloRes[random.randint(0, len(helloRes) - 1)]
    await client.say(choice + ctx.message.author.mention)
    print("Running j.hello!")
    print('------------------')

    
#j.larry (art?)

#j.son
@client.command(pass_context = True)
async def son(ctx):
    await client.say(ctx.message.author.mention + " Go on son!")
    print("Running j.son!")
    print('------------------')

#j.eggplant
@client.command(pass_context = True)
async def eggplant(ctx):
    await client.say(":eggplant:")
    print("Running j.eggplant!")
    print('------------------')

#j.diddled
@client.command(pass_context = True)
async def diddled(ctx):
    await client.say(ctx.message.author.mention + " You just got diddled!")
    print("Running j.diddled")
    print('------------------')

#j.woman
@client.command(pass_context = True)
async def woman(ctx):
    await client.say("I'm a married woman!")
    print("Running j.woman!")
    print('------------------')

#j.fanart

#j.omg
@client.command(pass_context = True)
async def omg(ctx):
    await client.say("Bloody Noora! " + ctx.message.author.mention + ", what is that?")
    print("Running j.omg!")
    print('------------------')

#j.pufferfish
@client.command(pass_context = True)
async def pufferfish(ctx):
    await client.say(ctx.message.author.mention + ", do you have any? :scream_cat:")
    print("Running j.pufferfish!")
    print('------------------')

#j.scum
@client.command(pass_context = True)
async def scum(ctx):
    for member in ctx.message.server.members:
        try:
            await client.change_nickname (member, "Scumbag " + member.name)
        except discord.errors.Forbidden:
            pass
    await client.say(ctx.message.author.mention + ", everybody is now a Scumbag!")
    print("Running j.scum!")
    print('------------------')

#j.noscum
@client.command(pass_context = True)
async def noscum(ctx):
    for member in ctx.message.server.members:
        try:
            await client.change_nickname (member, member.name)
        except discord.errors.Forbidden:
            pass
    await client.say(ctx.message.author.mention + ", everybody is no longer a Scumbag!")
    print("Running j.noscum!")
    print('------------------')

#j.kta
@client.command(pass_context=True)
async def kta(ctx):
    await client.say("#KTA4ADMIN")
    print("Running j.kta!")
    print('------------------')

#j.dev
@client.command(pass_context = True)
async def dev(ctx):
    await client.say("BuyTheWangSuffix deveolped and tested the JackMasseyWelsh [Bot] :smile:")
    print("Running j.dev")
    print('------------------')

#j.purge
@client.command(pass_context = True)
async def purge(ctx):
    await client.delete_message(ctx.message)
    await client.say(ctx.message.author.mention + ", we don't talk about the purge. :knife:")
    print("Running j.purge!")
    print('------------------')

#j.egg
@client.command(pass_context=True)
async def egg(ctx):
    await client.say("plant")
    print("Running j.egg")
    print('------------------')
          
client.run("MzQ1NjQyNjI0MzQ4MTkyNzg4.DG-QXA.ycZt93FxZa2OI9iTAirfF2GJBEI")
