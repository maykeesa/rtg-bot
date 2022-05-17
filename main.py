import discord
from discord.ext import commands
import random_team_lane as rtl
import random_team as rt

bot = commands.Bot("?")

#Bot inicialização
@bot.event
async def on_ready():
    print(f'Logged on as {bot.user}!')

#Log do discord
#@bot.event
#async def on_message(message):
    #print(f'Message from {message.author}: {message.content}')
    #await bot.process_commands(message)

#Registrador de time e lanes aleatórias
@bot.command(name="registrarTimeLane")
async def registerTeamLane(message, jogadores):
    players = jogadores.split(",")

    timeA, timeB = rtl.select_team_lane(players)
    await message.channel.send("```-----| TIME A |-----```")
    for i in timeA.items():
        await message.channel.send(f"** {i[0]} ** - ** {i[1]} **")

    await message.send("```-----| TIME B |-----```")
    for i in timeB.items():
        await message.channel.send(f"** {i[0]} ** - ** {i[1]} **")

#Registrador de time aleatórios
@bot.command(name="registrarTime")
async def registerTeam(message, jogadores):
    players = jogadores.split(",")

    timeA, timeB = rt.select_players(players)
    await message.channel.send("```-----| TIME A |-----```")
    for i in timeA:
        await message.channel.send(f"** {i} **")

    await message.send("```-----| TIME B |-----```")
    for i in timeB:
        await message.channel.send(f"** {i} **")

bot.run('OTc1OTQ3MDcyNDg4NDg0OTI2.Gb9ZeN.5hY-s0g-TyjxedTjtWOj9Lz7ATK3Cojc3BaK0M')