import asyncio
import discord
import os

from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()

intents = discord.Intents.all()

class RtgBot(commands.Bot):
    async def setup_hook(self):
        await self.load_extension("bot.cogs.team_commands")

        sync_global = os.getenv("SYNC_GLOBAL", "false").lower() == "true"
        guild_id = os.getenv("GUILD_ID")

        if sync_global:
            await self.tree.sync()
        elif guild_id:
            guild = discord.Object(id=int(guild_id))
            self.tree.copy_global_to(guild=guild)
            await self.tree.sync(guild=guild)

bot = RtgBot(intents=intents, command_prefix="?")

@bot.event
async def on_ready():
    print(f'Logged on as {bot.user}!!')

@bot.event
async def on_message(message):
    await bot.process_commands(message)

async def main():
    token = os.getenv("TOKEN")
    if not token:
        raise RuntimeError("TOKEN não definido. Copie .env.example para .env e preencha o token do bot.")

    await bot.start(token)

asyncio.run(main())
