import asyncio
import discord
import os

from dotenv import load_dotenv
from discord.ext import commands

intents = discord.Intents.all()
bot = commands.Bot(intents=intents, command_prefix="?")
load_dotenv()

#Bot inicialização
@bot.event
async def on_ready():
    print(f'Logged on as {bot.user}!!')

#Log do discord
@bot.event
async def on_message(message):
    print(f'Message from {message.author}: {message.content}')
    await bot.process_commands(message)

async def main():
    token = os.getenv("TOKEN")
    if not token:
        raise RuntimeError("TOKEN não definido. Copie .env.example para .env e preencha o token do bot.")

    await bot.load_extension("bot.cogs.team_commands")
    await bot.start(token)

asyncio.run(main())
