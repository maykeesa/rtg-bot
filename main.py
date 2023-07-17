import sample.embed as embed
import sample.formatting as formatting
import discord
from discord.ext import commands

intents = discord.Intents.all()
bot = commands.Bot(intents=intents, command_prefix="?")

#Bot inicialização
@bot.event
async def on_ready():
    print(f'Logged on as {bot.user}!')

#Log do discord
@bot.event
async def on_message(message):
    print(f'Message from {message.author}: {message.content}')
    await bot.process_commands(message)

#Registrador de time e lanes aleatórias
@bot.command(name="registrarTimeLane")
async def registrarTimeLane(message, jogadores):
    listaTimeA, listaTimeB = formatting.formatarTimeLane(jogadores)
    await embed.timeLane(message, listaTimeA, listaTimeB, bot)

#Registrador de time aleatórios
@bot.command(name="registrarTime")
async def registrarTime(message, jogadores):
    print("Ola")
    listaTimeA, listaTimeB = formatting.formatarTime(jogadores)
    await embed.time(message, listaTimeA, listaTimeB, bot)

bot.run('')
