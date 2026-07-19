import bot.embed as embed
import bot.formatting as formatting

from discord.ext import commands

class TeamCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="registrarTimeLane")
    async def registrar_time_lane(self, ctx, jogadores):
        lista_time_a, lista_time_b = formatting.formatar_time_lane(jogadores)
        await embed.time_lane(ctx, lista_time_a, lista_time_b, self.bot)

    @commands.command(name="registrarTime")
    async def registrar_time(self, ctx, jogadores):
        lista_time_a, lista_time_b = formatting.formatar_time(jogadores)
        await embed.time(ctx, lista_time_a, lista_time_b, self.bot)

async def setup(bot):
    await bot.add_cog(TeamCommands(bot))
