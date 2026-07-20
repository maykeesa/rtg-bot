import bot.embed as embed
import bot.formatting as formatting

from discord.ext import commands

class TeamCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.hybrid_command(
        name="registrar-time-lane",
        aliases=["registrarTimeLane"],
        description="Sorteia dois times e as lanes de cada jogador",
    )
    async def registrar_time_lane(self, ctx, jogadores: str):
        try:
            lista_time_a, lista_time_b = formatting.formatar_time_lane(jogadores)
        except ValueError as erro:
            await ctx.send(str(erro))
            return

        await embed.time_lane(ctx, lista_time_a, lista_time_b, self.bot)

    @commands.hybrid_command(
        name="registrar-time",
        aliases=["registrarTime"],
        description="Sorteia dois times aleatórios",
    )
    async def registrar_time(self, ctx, jogadores: str):
        try:
            lista_time_a, lista_time_b = formatting.formatar_time(jogadores)
        except ValueError as erro:
            await ctx.send(str(erro))
            return

        await embed.time(ctx, lista_time_a, lista_time_b, self.bot)

async def setup(bot):
    await bot.add_cog(TeamCommands(bot))
