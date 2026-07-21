import os
import discord
import bot.jokes as jk

TEAM_ICON_FILENAME = "blitz_angry.png"
ERRO_IMAGE_FILENAME = "blitz_broken.png"
MATCH_ICON_FILENAME = "blitz_happy.png"
WIN_ICON_FILENAME = "blitz_love.png"

_RESULTADOS = {
    "azul": (":trophy: Time Azul venceu!", 0x3498DB, WIN_ICON_FILENAME),
    "vermelho": (":trophy: Time Vermelho venceu!", 0xE74C3C, WIN_ICON_FILENAME),
    "cancelada": ("Partida cancelada", 0x95A5A6, ERRO_IMAGE_FILENAME),
    "expirada": ("Partida expirada", 0x95A5A6, ERRO_IMAGE_FILENAME),
}

def _image_file(filename):
    path = os.path.join(os.path.dirname(__file__), "..", "imgs", filename)
    return discord.File(path, filename=filename)

#Embed do ?registrarTimeLane
async def time_lane(ctx, lista_time_blue, lista_time_red, bot, view=None):
    icon_file = _image_file(TEAM_ICON_FILENAME)
    embed = discord.Embed(
        title="Time e Lanes aleatórias",
        description=f"{jk.choice_joke()}",
        color=0xFEE581,
    )

    embed.set_author(name = bot.user.name, icon_url= bot.user.display_avatar.url)
    embed.set_thumbnail(url=f"attachment://{TEAM_ICON_FILENAME}")
    embed.add_field(name="─────| TIME BLUE |─────", value= "\n".join(lista_time_blue))
    embed.add_field(name="─────| TIME RED  |─────", value="\n".join(lista_time_red), inline=False)
    embed.set_footer(text="Feito por " + bot.user.name, icon_url= bot.user.display_avatar.url)
    return await ctx.send(file=icon_file, embed=embed, view=view)

#Embed do ?registrarTime
async def time(ctx, lista_time_blue, lista_time_red, bot, view=None):
    icon_file = _image_file(TEAM_ICON_FILENAME)
    embed = discord.Embed(
        title="Times aleatórios",
        description=f"{jk.choice_joke()}",
        color=0xFEE581,
    )

    embed.set_author(name = bot.user.name, icon_url= bot.user.display_avatar.url)
    embed.set_thumbnail(url=f"attachment://{TEAM_ICON_FILENAME}")
    embed.add_field(name="─────| TIME BLUE |─────", value= "\n".join(lista_time_blue))
    embed.add_field(name="─────| TIME RED  |─────", value= "\n".join(lista_time_red), inline=False)
    embed.set_footer(text="Feito por " + bot.user.name, icon_url= bot.user.display_avatar.url)
    return await ctx.send(file=icon_file, embed=embed, view=view)

#Embed genérico de erro; edita a mensagem de origem do erro, se houver
async def erro(ctx, erro, bot):
    image_file = _image_file(ERRO_IMAGE_FILENAME)
    embed = discord.Embed(
        title=":x: " + erro.titulo,
        description=str(erro),
        color=0xE74C3C,
    )

    embed.set_author(name=bot.user.name, icon_url=bot.user.display_avatar.url)
    embed.set_thumbnail(url=f"attachment://{ERRO_IMAGE_FILENAME}")

    if erro.mensagem_origem is not None:
        await erro.mensagem_origem.edit(embed=embed, attachments=[image_file])
    else:
        await ctx.send(file=image_file, embed=embed)

#Embed de inscrição via reação, editado a cada jogador que entra
def inscricao(bot, nomes, expira_unix, emoji):
    file = _image_file(TEAM_ICON_FILENAME)
    embed = discord.Embed(
        title="Inscrições abertas",
        description=f"Reaja com {emoji} para entrar na partida. Encerra <t:{expira_unix}:R>.",
        color=0xFEE581,
    )

    embed.set_author(name=bot.user.name, icon_url=bot.user.display_avatar.url)
    embed.set_thumbnail(url=f"attachment://{TEAM_ICON_FILENAME}")
    embed.add_field(
        name=f"─────| JOGADORES ({len(nomes)}/10) |─────",
        value="\n".join(nomes) if nomes else "Ninguém entrou ainda.",
        inline=False,
    )
    embed.set_footer(text="Feito por " + bot.user.name, icon_url=bot.user.display_avatar.url)
    return embed, file

#Embed da partida em andamento, após confirmar o início
def partida_em_andamento(bot, lista_time_azul, lista_time_vermelho, inicio_unix):
    file = _image_file(MATCH_ICON_FILENAME)
    embed = discord.Embed(
        title="Partida em andamento",
        description=f"{jk.choice_joke()}",
        color=0xFEE581,
    )

    embed.set_author(name=bot.user.name, icon_url=bot.user.display_avatar.url)
    embed.set_thumbnail(url=f"attachment://{MATCH_ICON_FILENAME}")
    embed.add_field(name="─────| TIME AZUL |─────", value="\n".join(lista_time_azul))
    embed.add_field(name="─────| TIME VERMELHO |─────", value="\n".join(lista_time_vermelho), inline=False)
    embed.add_field(name="Início", value=f"<t:{inicio_unix}:R>", inline=False)
    embed.set_footer(text="Feito por " + bot.user.name, icon_url=bot.user.display_avatar.url)
    return embed, file

#Embed do resultado final da partida (vitória, cancelamento ou expiração)
def partida_resultado(bot, resultado, lista_time_azul, lista_time_vermelho):
    titulo, cor, icon_filename = _RESULTADOS[resultado]
    file = _image_file(icon_filename)
    
    embed = discord.Embed(
        title=titulo,
        description="Ninguém registrou o resultado a tempo." if resultado == "expirada" else f"{jk.choice_joke()}",
        color=cor,
    )

    embed.set_author(name=bot.user.name, icon_url=bot.user.display_avatar.url)
    embed.set_thumbnail(url=f"attachment://{icon_filename}")
    if resultado == "azul":
        embed.add_field(name="─────| TIME AZUL |─────", value="\n".join(lista_time_azul), inline=False)
    
    elif resultado == "vermelho":
        embed.add_field(name="─────| TIME VERMELHO |─────", value="\n".join(lista_time_vermelho), inline=False)
    
    else:
        embed.add_field(name="─────| TIME AZUL |─────", value="\n".join(lista_time_azul))
        embed.add_field(name="─────| TIME VERMELHO |─────", value="\n".join(lista_time_vermelho), inline=False)
    
    embed.set_footer(text="Feito por " + bot.user.name, icon_url=bot.user.display_avatar.url)
    return embed, file