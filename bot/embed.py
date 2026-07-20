import os
import discord
import bot.jokes as jk

TEAM_ICON_FILENAME = "blitz_angry.png"
ERRO_IMAGE_FILENAME = "blitz_broken.png"

#Embed do !registrarTimeLane
async def time_lane(ctx, lista_time_blue, lista_time_red, bot):
    icon_file = _lol_icon_file()
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
    await ctx.send(file=icon_file, embed=embed)

#Embed do !registrarTime
async def time(ctx, lista_time_blue, lista_time_red, bot):
    icon_file = _lol_icon_file()
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
    await ctx.send(file=icon_file, embed=embed)

#Embed genérico de erro
async def erro(ctx, erro, bot):
    image_file = _erro_image_file()
    embed = discord.Embed(
        title=":x: " + erro.titulo,
        description=str(erro),
        color=0xE74C3C,
    )

    embed.set_author(name=bot.user.name, icon_url=bot.user.display_avatar.url)
    embed.set_thumbnail(url=f"attachment://{ERRO_IMAGE_FILENAME}")
    await ctx.send(file=image_file, embed=embed)

def _lol_icon_file():
    LOL_ICON_PATH = os.path.join(os.path.dirname(__file__), "..", "imgs", TEAM_ICON_FILENAME)
    return discord.File(LOL_ICON_PATH, filename=TEAM_ICON_FILENAME)

def _erro_image_file():
    ERRO_IMAGE_PATH = os.path.join(os.path.dirname(__file__), "..", "imgs", ERRO_IMAGE_FILENAME)
    return discord.File(ERRO_IMAGE_PATH, filename=ERRO_IMAGE_FILENAME)