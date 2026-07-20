import copy
from datetime import timedelta

import discord

import bot.embed as embed

CONFIRMACAO_TIMEOUT = 120 # 2m
PARTIDA_TIMEOUT = 9000  # 2h30m

class _AutorOnlyView(discord.ui.View):
    def __init__(self, autor_id, *, timeout=None):
        super().__init__(timeout=timeout)
        self.autor_id = autor_id
        self.message = None

    async def interaction_check(self, interaction: discord.Interaction) -> bool:
        if interaction.user.id != self.autor_id:
            await interaction.response.send_message(
                "Apenas quem sorteou o time pode usar estes botões.",
                ephemeral=True,
            )
            return False
        return True

class IniciarPartidaView(_AutorOnlyView):
    def __init__(self, autor_id, lista_time_azul, lista_time_vermelho, bot):
        super().__init__(autor_id, timeout=None)
        self.lista_time_azul = lista_time_azul
        self.lista_time_vermelho = lista_time_vermelho
        self.bot = bot

    @discord.ui.button(label="Iniciar Partida", style=discord.ButtonStyle.success, emoji="▶️")
    async def iniciar_partida(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed_original = copy.deepcopy(interaction.message.embeds[0])
        embed_original.set_thumbnail(url=f"attachment://{embed.TEAM_ICON_FILENAME}")

        confirm_view = ConfirmarPartidaView(
            self.autor_id, self.lista_time_azul, self.lista_time_vermelho, self.bot, embed_original
        )
        expira_unix = int((discord.utils.utcnow() + timedelta(seconds=CONFIRMACAO_TIMEOUT)).timestamp())
        embed_confirmacao = copy.deepcopy(embed_original)
        embed_confirmacao.add_field(
            name="Confirmação", value=f"Iniciar a partida? Expira <t:{expira_unix}:R>.", inline=False
        )
        await interaction.response.edit_message(embed=embed_confirmacao, view=confirm_view)
        confirm_view.message = interaction.message

class ConfirmarPartidaView(_AutorOnlyView):
    def __init__(self, autor_id, lista_time_azul, lista_time_vermelho, bot, embed_original):
        super().__init__(autor_id, timeout=CONFIRMACAO_TIMEOUT)
        self.lista_time_azul = lista_time_azul
        self.lista_time_vermelho = lista_time_vermelho
        self.bot = bot
        self.embed_original = embed_original

    @discord.ui.button(label="Sim", style=discord.ButtonStyle.success, emoji="✅")
    async def sim(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.stop()
        inicio_unix = int(discord.utils.utcnow().timestamp())
        novo_embed, file = embed.partida_em_andamento(
            self.bot, self.lista_time_azul, self.lista_time_vermelho, inicio_unix
        )
        match_view = PartidaEmAndamentoView(
            self.autor_id, self.lista_time_azul, self.lista_time_vermelho, self.bot
        )
        await interaction.response.defer()
        mensagem = await interaction.edit_original_response(
            content=None, embed=novo_embed, attachments=[file], view=match_view
        )
        match_view.message = mensagem

    @discord.ui.button(label="Não", style=discord.ButtonStyle.danger, emoji="✖️")
    async def nao(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.stop()
        view_original = IniciarPartidaView(
            self.autor_id, self.lista_time_azul, self.lista_time_vermelho, self.bot
        )
        await interaction.response.edit_message(embed=self.embed_original, view=view_original)
        view_original.message = interaction.message

    async def on_timeout(self):
        if self.message is None:
            return
        view_original = IniciarPartidaView(
            self.autor_id, self.lista_time_azul, self.lista_time_vermelho, self.bot
        )
        try:
            await self.message.edit(embed=self.embed_original, view=view_original)
            view_original.message = self.message
        except discord.HTTPException:
            pass

class PartidaEmAndamentoView(_AutorOnlyView):
    def __init__(self, autor_id, lista_time_azul, lista_time_vermelho, bot):
        super().__init__(autor_id, timeout=PARTIDA_TIMEOUT)
        self.lista_time_azul = lista_time_azul
        self.lista_time_vermelho = lista_time_vermelho
        self.bot = bot

    async def _finalizar(self, interaction: discord.Interaction, resultado: str):
        novo_embed, file = embed.partida_resultado(
            self.bot, resultado, self.lista_time_azul, self.lista_time_vermelho
        )
        self.stop()
        await interaction.response.defer()
        await interaction.edit_original_response(embed=novo_embed, attachments=[file], view=None)

    @discord.ui.button(label="Time Azul venceu", style=discord.ButtonStyle.primary)
    async def time_azul_venceu(self, interaction: discord.Interaction, button: discord.ui.Button):
        await self._finalizar(interaction, "azul")

    @discord.ui.button(label="Time Vermelho venceu", style=discord.ButtonStyle.danger)
    async def time_vermelho_venceu(self, interaction: discord.Interaction, button: discord.ui.Button):
        await self._finalizar(interaction, "vermelho")

    @discord.ui.button(label="Cancelar partida", style=discord.ButtonStyle.secondary)
    async def cancelar_partida(self, interaction: discord.Interaction, button: discord.ui.Button):
        await self._finalizar(interaction, "cancelada")

    async def on_timeout(self):
        if self.message is None:
            return
        novo_embed, file = embed.partida_resultado(
            self.bot, "expirada", self.lista_time_azul, self.lista_time_vermelho
        )
        try:
            await self.message.edit(embed=novo_embed, attachments=[file], view=None)
        except discord.HTTPException:
            pass
