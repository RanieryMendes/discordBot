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



@bot.event
async def on_member_join(member):

    print("calling on join")
    embed = discord.Embed(
        title=f"{member.display_name} chegou! Ele ta aqui desde{member.joined_at()}",
        color= bot.embed_color,
        timestamp= datetime.datetime.now(datetime.timezone.utc)
    )

    embed.set_footer(

        text=bot.footer,
        icon_url=bot.footer_image
    )

   # mensagem = Message(
       # content=f"{member.display_name} chegou! Ele ta aqui desde{member.joined_at()}",
        #created_at=datetime.datetime.now(datetime.timezone.utc),
    #)
    for channel in member.guild.channels:
            await channel.send_message(f"Welcome {member.display_name}")
    
    print("calling on join2")
    bot.log_channel = bot.get_channel(670030020621762610)
    await bot.log_channel.send(embed=embed)
 


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


@bot.command(
    name="invite",
    aliases=["i"],
    help="It creates a link invitation to the server"
) 

async def invite(ctx):

    embed = discord.Embed(
        title=f" Toma aqui a porra do convite, {ctx.author.name}!",
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

    invitation = await ctx.channel.create_invite(max_uses=1,unique=True,max_age=120)


    
    
    await bot.log_channel.send(embed=embed, content=invitation)

    await ctx.author.send(invitation)





bot.run(token, bot=True, reconnect=True)


# 670030020621762610