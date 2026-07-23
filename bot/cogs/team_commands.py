import bot.embed as embed
import bot.formatting as formatting
import bot.signup as signup
import bot.views as views

from discord import app_commands
from discord.ext import commands
from bot.constants import DESCRICAO_JOGADORES
from bot.exceptions import ValidacaoError

class TeamCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.hybrid_command(
        name="registrar-time-lane",
        aliases=["registrarTimeLane"],
        description="Sorteia dois times e as lanes de cada jogador",
    )
    @app_commands.describe(jogadores=DESCRICAO_JOGADORES)
    async def registrar_time_lane(self, ctx, jogadores: str = None):
        await self._registrar(
            ctx,
            jogadores,
            formatting.formatar_time_lane,
            formatting.formatar_time_lane_lista,
            embed.time_lane,
        )

    @commands.hybrid_command(
        name="registrar-time",
        aliases=["registrarTime"],
        description="Sorteia dois times aleatórios",
    )
    @app_commands.describe(jogadores=DESCRICAO_JOGADORES)
    async def registrar_time(self, ctx, jogadores: str = None):
        await self._registrar(
            ctx,
            jogadores,
            formatting.formatar_time,
            formatting.formatar_time_lista,
            embed.time,
        )

    async def _registrar(self, ctx, jogadores, formatar, formatar_lista, enviar_embed):
        try:
            if jogadores is None:
                nomes = await signup.coletar_jogadores(ctx, self.bot)
                lista_time_azul, lista_time_vermelho = formatar_lista(nomes)
            else:
                lista_time_azul, lista_time_vermelho = formatar(jogadores)
        except ValidacaoError as erro:
            await embed.erro(ctx, erro, self.bot)
            return

        view = views.IniciarPartidaView(ctx.author.id, lista_time_azul, lista_time_vermelho, self.bot)
        mensagem = await enviar_embed(ctx, lista_time_azul, lista_time_vermelho, self.bot, view=view)
        view.message = mensagem

async def setup(bot):
    await bot.add_cog(TeamCommands(bot))
