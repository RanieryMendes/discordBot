import discord
import dotenv
import os
import datetime

from discord.ext import commands 

dotenv.load_dotenv()

token = os.getenv("ACCESS_TOKEN")

bot = commands.Bot(command_prefix="$",
 description="O DJ millionery esta aqui para agitar seu servidor e oferecer experiencias incriveis que so um rei do camarote milionario pode oferecer!", 
case_insensitive=True)

bot.embed_color = discord.Colour.purple()
bot.footer= "Investe comigo"
bot.footer_image= "https://png.pngtree.com/png-clipart/20190612/original/pngtree-a-wad-of-dollar-bills-png-image_3326543.jpg"
@bot.event

async def on_ready():
    print("I'm connected to Discord")

    game = discord.Game(name="!milhoes")
    await bot.change_presence(activity=game)

    embed= discord.Embed(
        title=f"{bot.user.name} Online!",
        color= bot.embed_color,
        timestamp= datetime.datetime.now(datetime.timezone.utc)
        )
    
    embed.set_footer(
        text=bot.footer,
        icon_url=bot.footer_image
    )

    bot.log_channel = bot.get_channel(670030020621762610)
    await bot.log_channel.send(embed=embed)
    print(f"Message sent on Discord channel. My ID is {bot.user.id}")

@bot.command(
    name="restart",
    aliases=["r"],
    help="Restarts the bot"
) 

async def restart(ctx):

    embed = discord.Embed(
        title=f"{bot.user.name} Restarting!",
        color= bot.embed_color,
        timestamp= datetime.datetime.now(datetime.timezone.utc)
    )
    embed.set_author(
        name=ctx.author.name,
        icon_url=ctx.author.avatar_url

    )
    embed.set_footer(

        text=bot.footer,
        icon_url=bot.footer_image
    )

    await bot.log_channel.send(embed=embed)

    await ctx.message.add_reaction('☑️')

    await bot.close()

bot.run(token, bot=True, reconnect=True)


# 670030020621762610