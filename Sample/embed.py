import discord
import Sample.jokes as jk

# Icone do LoL
lolIcon = "https://cdn.discordapp.com/attachments/975993751455559680/976940532251127918/lolIcon.png"

#Embed do !registrarTimeLane
async def timeLane(ctx, listaTimeA, listaTimeB, bot):
    embed = discord.Embed(
        title="Time e Lanes aleatórias",
        description=f"{jk.choiceJoke()}",
        color=0xFEE581,
    )

    embed.set_author(name = bot.user.name, icon_url= bot.user.avatar)
    embed.set_thumbnail(url=lolIcon)
    embed.add_field(name="─────| TIME BLUE |─────", value= "\n".join(listaTimeA))
    embed.add_field(name="─────| TIME RED  |─────", value="\n".join(listaTimeB), inline=False)
    embed.set_footer(text="Feito por " + bot.user.name, icon_url= bot.user.avatar)
    await ctx.send(embed=embed)

#Embed do !registrarTime
async def time(ctx, listaTimeA, listaTimeB, bot):
    embed = discord.Embed(
        title="Times aleatórios",
        description=f"{jk.choiceJoke()}",
        color=0xFEE581,
    )

    embed.set_author(name = bot.user.name, icon_url= bot.user.avatar)
    embed.set_thumbnail(url=lolIcon)
    embed.add_field(name="─────| TIME BLUE |─────", value= "\n".join(listaTimeA))
    embed.add_field(name="─────| TIME RED  |─────", value= "\n".join(listaTimeB), inline=False)
    embed.set_footer(text="Feito por " + bot.user.name, icon_url= bot.user.avatar)
    await ctx.send(embed=embed)
