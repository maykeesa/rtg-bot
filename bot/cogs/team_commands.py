import bot.embed as embed
import bot.formatting as formatting
import bot.signup as signup
import bot.views as views

from discord.ext import commands
from bot.exceptions import ValidacaoError

class TeamCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.hybrid_command(
        name="registrar-time-lane",
        aliases=["registrarTimeLane"],
        description="Sorteia dois times e as lanes de cada jogador",
    )
    async def registrar_time_lane(self, ctx, jogadores: str = None):
        try:
            if jogadores is None:
                nomes = await signup.coletar_jogadores(ctx, self.bot)
                lista_time_a, lista_time_b = formatting.formatar_time_lane_lista(nomes)
            else:
                lista_time_a, lista_time_b = formatting.formatar_time_lane(jogadores)
        except ValidacaoError as erro:
            await embed.erro(ctx, erro, self.bot)
            return

        view = views.IniciarPartidaView(ctx.author.id, lista_time_a, lista_time_b, self.bot)
        mensagem = await embed.time_lane(ctx, lista_time_a, lista_time_b, self.bot, view=view)
        view.message = mensagem

    @commands.hybrid_command(
        name="registrar-time",
        aliases=["registrarTime"],
        description="Sorteia dois times aleatórios",
    )
    async def registrar_time(self, ctx, jogadores: str = None):
        try:
            if jogadores is None:
                nomes = await signup.coletar_jogadores(ctx, self.bot)
                lista_time_a, lista_time_b = formatting.formatar_time_lista(nomes)
            else:
                lista_time_a, lista_time_b = formatting.formatar_time(jogadores)
        except ValidacaoError as erro:
            await embed.erro(ctx, erro, self.bot)
            return

        view = views.IniciarPartidaView(ctx.author.id, lista_time_a, lista_time_b, self.bot)
        mensagem = await embed.time(ctx, lista_time_a, lista_time_b, self.bot, view=view)
        view.message = mensagem

async def setup(bot):
    await bot.add_cog(TeamCommands(bot))
