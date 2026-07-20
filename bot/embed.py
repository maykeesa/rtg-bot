import os
import discord
import bot.jokes as jk

# Icone do LoL
LOL_ICON_PATH = os.path.join(os.path.dirname(__file__), "..", "imgs", "lolIcon.png")
LOL_ICON_FILENAME = "lolIcon.png"

def _lol_icon_file():
    return discord.File(LOL_ICON_PATH, filename=LOL_ICON_FILENAME)

#Embed do !registrarTimeLane
async def time_lane(ctx, lista_time_blue, lista_time_red, bot):
    icon_file = _lol_icon_file()
    embed = discord.Embed(
        title="Time e Lanes aleatórias",
        description=f"{jk.choice_joke()}",
        color=0xFEE581,
    )

    embed.set_author(name = bot.user.name, icon_url= bot.user.avatar)
    embed.set_thumbnail(url=f"attachment://{LOL_ICON_FILENAME}")
    embed.add_field(name="─────| TIME BLUE |─────", value= "\n".join(lista_time_blue))
    embed.add_field(name="─────| TIME RED  |─────", value="\n".join(lista_time_red), inline=False)
    embed.set_footer(text="Feito por " + bot.user.name, icon_url= bot.user.avatar)
    await ctx.send(file=icon_file, embed=embed)

#Embed do !registrarTime
async def time(ctx, lista_time_blue, lista_time_red, bot):
    icon_file = _lol_icon_file()
    embed = discord.Embed(
        title="Times aleatórios",
        description=f"{jk.choice_joke()}",
        color=0xFEE581,
    )

    embed.set_author(name = bot.user.name, icon_url= bot.user.avatar)
    embed.set_thumbnail(url=f"attachment://{LOL_ICON_FILENAME}")
    embed.add_field(name="─────| TIME BLUE |─────", value= "\n".join(lista_time_blue))
    embed.add_field(name="─────| TIME RED  |─────", value= "\n".join(lista_time_red), inline=False)
    embed.set_footer(text="Feito por " + bot.user.name, icon_url= bot.user.avatar)
    await ctx.send(file=icon_file, embed=embed)
