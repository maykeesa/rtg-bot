import asyncio
from datetime import timedelta

import discord

import bot.embed as embed

from bot.exceptions import InscricaoExpiradaError

INSCRICAO_TIMEOUT = 120 # 2m

async def coletar_jogadores(ctx, bot):
    emoji = "✅"
    expira_em = discord.utils.utcnow() + timedelta(seconds=INSCRICAO_TIMEOUT)
    expira_unix = int(expira_em.timestamp())
    inscritos = {}

    novo_embed, file = embed.inscricao(bot, [], expira_unix, emoji)
    mensagem = await ctx.send(file=file, embed=novo_embed)
    await mensagem.add_reaction(emoji)

    def check(payload):
        return (
            payload.message_id == mensagem.id
            and str(payload.emoji) == emoji
            and payload.user_id != bot.user.id
        )

    while len(inscritos) < 10:
        restante = (expira_em - discord.utils.utcnow()).total_seconds()
        if restante <= 0:
            break

        try:
            payload = await bot.wait_for("raw_reaction_add", check=check, timeout=restante)
        except asyncio.TimeoutError:
            break

        membro = payload.member
        if membro is None or membro.bot or payload.user_id in inscritos:
            continue

        inscritos[payload.user_id] = membro.display_name
        novo_embed, _ = embed.inscricao(bot, list(inscritos.values()), expira_unix, emoji)
        await mensagem.edit(embed=novo_embed)

    if len(inscritos) < 10:
        raise InscricaoExpiradaError(mensagem)

    return _nomes_unicos(list(inscritos.values()))

def _nomes_unicos(nomes):
    vistos = {}
    resultado = []
    for nome in nomes:
        vistos[nome] = vistos.get(nome, 0) + 1
        resultado.append(nome if vistos[nome] == 1 else f"{nome} ({vistos[nome]})")
    return resultado