import discord
import dotenv
import os
import datetime
import random

from discord.ext import commands 

dotenv.load_dotenv()

#get Token
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

    #game activity that will be displayed on the bot 
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



#MESSAGE FOR FIRST TIME JOINING THE SERVER
@bot.event
async def on_member_join(member):

  
    embed = discord.Embed(
        title=f"{member.display_name} chegou! Seja bem vindo nesssa grande pUtARiA",
        color= bot.embed_color,
        timestamp= datetime.datetime.now(datetime.timezone.utc)
    )

    embed.set_footer(

        text=bot.footer,
        icon_url=bot.footer_image
    )

    for channel in member.guild.channels:
            await channel.send_message(f"Welcome {member.display_name}")
    
    bot.log_channel = bot.get_channel(670030020621762610)
    await bot.log_channel.send(embed=embed)
 

#COMMAND RESTART 
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


#INVITATION COMMAND
@bot.command(
    name="invite",
    aliases=["i"],
    help="It creates a link invitation to the server"
) 

async def invite(ctx):

#message that will be sent along with the invitation
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

    #create the link 
    invitation = await ctx.channel.create_invite(max_uses=1,unique=True,max_age=120)

    
    await bot.log_channel.send(embed=embed, content=invitation)

    await ctx.author.send(invitation)

@bot.event
async def on_message(message):

  photoSimp = discord.File("./images/simpson.jpg")
#especial mute for users who type the word "grimes"        
  if message.content.startswith('grimes'):  
        channel = message.channel      
        await channel.send(f'Você falou aquela que nao pode ser nomeada', file=photoSimp )
        await message.author.edit(mute=True)

  #checks if the user has typed a bot command  
  await bot.process_commands(message)


#bot event to welcome users that come into the discord server
@bot.event
async def on_voice_state_update(member, before, after):

    #pic to be sent as a welcome gesture
    photoWelcome = discord.File("./images/adri.jpeg")
    
    name = member.nick #store the new guest's nick

    bot.log_channel = bot.get_channel(670030020621762610) #address of the channel the bot may send the message
    
    #if condition which chekes wheter the user is a new guest or not. NOT = was already on the server
    if(before.channel == None):
        #send welcome message
        await bot.log_channel.send("Oi, " + name + ", mama aqui!! GLUB GLUB", file= photoWelcome) 



#COMMAND $RONALDO
@bot.command(
    name="ronaldo",
    aliases=["ro"],
    help="It texts a random picture of someone who is doing Ronaldo's hang loose sign"
) 


async def ronaldo(ctx):

    #variables with pictures of Ronaldo's hang loose
    photoR = discord.File("./images/ronaldo.jpeg")
    photoN = discord.File("./images/neymar.jpeg")
    photoM = discord.File("./images/merkel.jpeg")
    photoP = discord.File("./images/alexandrePato.jpeg")
    photoG = discord.File("./images/GabiGol.jpeg")
    photoCV = discord.File("./images/cv.jpeg")
    photoAle = discord.File("./images/aleatorio.jpeg")
    

    #list with all possible pics 
    list_Photos= [photoR, photoN, photoM, photoP, photoG, photoCV, photoAle]

        
    #set a random number that will be the photo that will be posted on the chat channel whenever someone runs the command    
    randNum = random.randrange(7)


    channel = ctx.channel #channel to it the bot will send the message

    #run the command and publish a photo
    await channel.send(f'Faz o sinal do ronaldinho👍 , {ctx.author.name}', file=list_Photos[randNum])

    
#run the bot 
bot.run(token, bot=True, reconnect=True)

