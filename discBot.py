import discord
import dotenv
import os
import datetime
import random
import asyncio
import time
import youtube_dl
from discord.utils import get
from youtube_dl import YoutubeDL
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


    #COMMAND $MIREI
@bot.command(
    name="mirei",
    aliases=["m"],
    help="It plays RanyFollen's famous, controversial phrase"
) 

async def mirei(ctx):

    audio_1= './audios/audio.mp3'
    audio_2= './audios/vaamerda_1.mp3'
    audio_3='./audios/audio_3.mp3'
    audio_4='./audios/audio_4.mp3'
    audio_5='./audios/audio_5.mp3'

    list_Audios= [audio_1, audio_2, audio_3, audio_4, audio_5]

 #set a random number that will be the photo that will be posted on the chat channel whenever someone runs the command    
    randNum = random.randrange(5)

    channel = ctx.author.voice.channel
   
    player = await channel.connect()    
    #player.play(discord.FFmpegPCMAudio('audio.mp3'))
    player.play(discord.FFmpegPCMAudio(list_Audios[randNum]))

    while player.is_playing():
         time.sleep(5)
    await player.disconnect()



@bot.command(
    name="stop",
    aliases=["s"],
    help="It quits the bot from the voice channel"
) 

async def stop(ctx):

    channel = ctx.message.guild.voice_client
    await channel.disconnect()


# await voz.play(source="/Users/ranierymendes/Documents/DiscBot/audio.mpeg")

#MUSIC COMMMAND
@bot.command(
    name="play",
    aliases=["p"],
    help="O bot irá entrar no canal e tocar a musica selecionada pelo usuário"
)


async def play(ctx):
    try:
        channel = ctx.author.voice.channel
        await channel.connect()
    except discord.errors.InvalidArgument:
        await channel.send("O bot ta em outro canal porra! Ta cego?")
    except Exception as error:
        await channel.send("Ein Error: ```{error}```".format(error=error))

    try:
        yt_url = ctx.message.content
        print(yt_url)
        #remove the commander sign from the phrase
        yt_url = yt_url.strip('$p')
        print(yt_url)
        channel = ctx.author.voice.channel
        bot.log_channel = bot.get_channel(670030020621762610)
       
        try:
              ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
              with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                     ydl.download([yt_url])
                     for file in os.listdir("./"):
                         if file.endswith(".mp3"):
                            os.rename(file, 'song.mp3')
                     channel.play(discord.FFmpegPCMAudio("song.mp3"))
                     channel.volume = 100

                
                #player = await channel.create_ytdl_player(yt_url)

                #voice = ctx.message.guild.voice_client
               
               # player = await voice.create_ytdl_player('ytsearch: {}'.format(yt_url))
                
                #player.start()
              
       
        except Exception as e:
                 #await bot.log_channel.send("Error: [{error}]".format(error=e))
                 print(e)
    except Exception as e:
          # await bot.log_channel.send("Error: [{error}]".format(error=e))
           print(e)

@bot.command(
    name="brtt",
    aliases=["tt"],
    help="Lança a braba do BRTT"
) 

async def brtt(ctx):

    brtt_photo= discord.File('./images/brtt.jpeg')
    channel = ctx.channel

    await channel.send("REXPEITA", file= brtt_photo)

@bot.command(
    name="tiaFortinha",
    aliases=["ff"],
    help="Lança a braba das Tias Fortinhas"
) 

async def tiaFortinha(ctx):

    audio = "./audios/jeitoSexy.mp3"

    channel = ctx.author.voice.channel
    
    player = await channel.connect()    

    #player.play(discord.FFmpegPCMAudio('audio.mp3'))
    player.play(discord.FFmpegPCMAudio(audio))

    while player.is_playing():
         time.sleep(5)
    await player.disconnect()


def get_id(n):
    return n.id

@bot.command(
    name="teste",
    aliases=["te"],
    help="Sera que toca musica?"
) 

async def teste(ctx, video):
    YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist':'True'}
    FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
    voice = get(bot.voice_clients, guild=ctx.guild)
    channel = ctx.author.voice.channel 

    #store the list with the members online in the voice channel and their data
    list_users= ctx.author.voice.channel.members 
    #filters into a list that constains only their ids
    result= map(get_id, list_users)

    #checks whether the bot is already connected to the voice channel 
    #if not go ahead and connect to it

    if not 743902306306752522 in result: 
        
        player = await channel.connect()

   
     
    if player.is_connected():

        if not player.is_playing():

            with YoutubeDL(YDL_OPTIONS) as ydl:
                info = ydl.extract_info(url=video, download=False)
            URL = info['formats'][0]['url']

            player.play(discord.FFmpegPCMAudio(URL, **FFMPEG_OPTIONS), after=lambda  e: print('Chega dessa porra!', e))
          
        else:
            await ctx.channel.send("Ja ta tocando musica, mané!")

    else:
        await ctx.channel.send("Bot nao quer entrar pra voce! Tenta dps")
  

#run the bot 
bot.run(token, bot=True, reconnect=True)

    