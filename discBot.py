import discord
import dotenv
import os
import datetime

from discord.ext import commands 

dotenv.load_dotenv()

token = os.getenv("ACCESS_TOKEN")

bot = commands.Bot(command_prefix="$",
 description="O DJ millionery está aqui para agitar seu servidor e oferecer experiências incríveis que só um rei do camarote milionario pode oferecer!", 
case_insensitive=True)


@bot.event

async def on_ready():
    print("I'm connected to Discord")

    game = discord.Game(name="!milhões")
    await bot.change_presence(activity=game)

    embed= discord.Embed(
        title=f"{bot.user.name} Online!",
        color= discord.Color.purple,
        timestamp= datetime.datetime.now(datetime.timezone.utc)
        )
    
    embed.set_footer(
        text="Investe comigo",

        icon_url="https://image.flaticon.com/icons/svg/409/409065.svg"
    )

    channel = bot.get_channel(670030020621762610)
    await channel.send(embed=embed)
    print(f"Message sent on Discord channel. My ID is {bot.user.id}")


bot.run(token, bot=True, reconnect=True)


# 670030020621762610