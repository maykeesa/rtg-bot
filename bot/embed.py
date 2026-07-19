import discord
import bot.jokes as jk

# Icone do LoL
lol_icon = "https://cdn.discordapp.com/attachments/975993751455559680/976940532251127918/lolIcon.png"

#Embed do !registrarTimeLane
async def time_lane(ctx, lista_time_a, lista_time_b, bot):
    embed = discord.Embed(
        title="Time e Lanes aleatórias",
        description=f"{jk.choice_joke()}",
        color=0xFEE581,
    )

    embed.set_author(name = bot.user.name, icon_url= bot.user.avatar)
    embed.set_thumbnail(url=lol_icon)
    embed.add_field(name="─────| TIME BLUE |─────", value= "\n".join(lista_time_a))
    embed.add_field(name="─────| TIME RED  |─────", value="\n".join(lista_time_b), inline=False)
    embed.set_footer(text="Feito por " + bot.user.name, icon_url= bot.user.avatar)
    await ctx.send(embed=embed)

#Embed do !registrarTime
async def time(ctx, lista_time_a, lista_time_b, bot):
    embed = discord.Embed(
        title="Times aleatórios",
        description=f"{jk.choice_joke()}",
        color=0xFEE581,
    )

    embed.set_author(name = bot.user.name, icon_url= bot.user.avatar)
    embed.set_thumbnail(url=lol_icon)
    embed.add_field(name="─────| TIME BLUE |─────", value= "\n".join(lista_time_a))
    embed.add_field(name="─────| TIME RED  |─────", value= "\n".join(lista_time_b), inline=False)
    embed.set_footer(text="Feito por " + bot.user.name, icon_url= bot.user.avatar)
    await ctx.send(embed=embed)
