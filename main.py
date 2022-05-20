import discord
import jokes as jk
from discord.ext import commands
import randomTeam.randomTeam as rt
import randomTeam.randomTeamLane as rtl

bot = commands.Bot("$")

#Bot inicialização
@bot.event
async def on_ready():
    print(f'Logged on as {bot.user}!')

#Log do discord
@bot.event
async def on_message(message):
    print(f'Message from {message.author}: {message.content}')
    await bot.process_commands(message)

#Get das listas que irão para o Embed
listaTimeLaneA = []
listaTimeLaneB = []

#Registrador de time e lanes aleatórias
@bot.command(name="registrarTimeLane")
async def dividirTimeLane(message, jogadores):
    players = jogadores.split(",")

    timeA, timeB = rtl.select_team_lane(players)
    for i in timeA.items():
        listaTimeLaneA.append(f"{i[0]} - {i[1]}")

    for i in timeB.items():
        listaTimeLaneB.append(f"{i[0]} - {i[1]}")

    await ambedTimeLane(message)
    listaTimeLaneA.clear()
    listaTimeLaneB.clear()

#Embed do !registrarTimeLane
async def ambedTimeLane(ctx):
    embed = discord.Embed(
        title="Time e Lanes aleatórias",
        description=f"{jk.choiceJoke()}",
        color=0xFEE581,
    )

    embed.set_author(name = bot.user.name, icon_url= bot.user.avatar_url)
    lolIcon = "https://cdn.discordapp.com/attachments/975993751455559680/976940532251127918/lolIcon.png"
    embed.set_thumbnail(url=lolIcon)
    embed.add_field(name="-----| TIME BLUE |-----", value= "\n".join(listaTimeLaneA))
    embed.add_field(name="-----| TIME RED |-----", value="\n".join(listaTimeLaneB), inline=False)
    embed.set_footer(text="Feito por " + bot.user.name, icon_url= bot.user.avatar_url)
    await ctx.send(embed=embed)

#Get das listas que irão para o Embed
listaTimeA = []
listaTimeB = []

#Registrador de time aleatórios
@bot.command(name="registrarTime")
async def dividirTime(message, jogadores):

    players = jogadores.split(",")             

    timeA, timeB = rt.select_players(players)
    for i in timeA:
        listaTimeA.append(f" {i} ")

    for i in timeB:
        listaTimeB.append(f" {i} ")

    await ambedTime(message)
    listaTimeA.clear()
    listaTimeB.clear()

#Embed do !registrarTime
async def ambedTime(ctx):
    embed = discord.Embed(
        title="Times aleatórios",
        description=f"{jk.choiceJoke()}",
        color=0xFEE581,
    )

    embed.set_author(name = bot.user.name, icon_url= bot.user.avatar_url)
    lolIcon = "https://cdn.discordapp.com/attachments/975993751455559680/976940532251127918/lolIcon.png"
    embed.set_thumbnail(url=lolIcon)
    embed.add_field(name="-----| TIME BLUE |-----", value= "\n".join(listaTimeA))
    embed.add_field(name="-----| TIME RED  |-----", value= "\n".join(listaTimeB), inline=False)
    embed.set_footer(text="Feito por " + bot.user.name, icon_url= bot.user.avatar_url)
    await ctx.send(embed=embed)

bot.run('')
