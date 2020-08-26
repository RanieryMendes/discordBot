import discord
import dotenv
import os
import datetime
import random
import asyncio
import time
import youtube_dl
import traceback, json
from discord.utils import get
from youtube_dl import YoutubeDL
from discord.ext import commands, tasks
from youtube_search import YoutubeSearch 
import shutil

#get Token
dotenv.load_dotenv()
token = os.getenv("ACCESS_TOKEN")

#initating bot configuration
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

    #channel address to where message is going to be sent
    bot.log_channel = bot.get_channel(670030698308173824)
    await bot.log_channel.send(embed=embed)
    print(f"Message sent on Discord channel. My ID is {bot.user.id}")
    google.start()
   
    



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
    
    bot.log_channel = bot.get_channel(670030698308173824)
    await bot.log_channel.send(embed=embed)
 

#RESTART COMMAND
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

    
    await ctx.channel.send(embed=embed)

    #send a reaction to "register" the restart
    await ctx.message.add_reaction('☑️')

    #disconnect
    await bot.close()
    
    await time.sleep(10)

    bot.run(token)


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

    #create the invitation link 
    invitation = await ctx.channel.create_invite(max_uses=1,unique=True,max_age=120)

    
    await ctx.channel.send(embed=embed, content=invitation)

    await ctx.author.send(invitation)

#ON MESSAGE EVENT
@bot.event
async def on_message(message):

#photo that will be sent along with the word explained below
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
    
    name =  member.name#store the new guest's nick
   
    bot.log_channel = bot.get_channel(670030698308173824) #address of the channel the bot may send the message
    
    
    #if condition which chekes wheter the user is a new guest or not. NOT = was already on the server
    if(before.channel == None and member.id != 743902306306752522):
        #send welcome message
        await bot.log_channel.send(f"Oi,  {name}  , mama aqui!! GLUB GLUB", file= photoWelcome) 



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
    help="Toca um audio maneiro! É random e surpresa ;)"
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


#STOP Command
@bot.command(
    name="stop",
    aliases=["s"],
    help="  Retira o bot do canal de voz! Favor utilizar este comando quando acabar de tocar suas musicas"
) 

async def stop(ctx):

    #get the address of the voice channel the bot has to disconnect from
    channel = ctx.message.guild.voice_client
    list_songs.clear() #clear the list of songs to be played 
    name_songs.clear() #clear the list of songs name to be played 
    
    try:
        if channel.is_connected():
        
            await channel.disconnect()

    except AttributeError as e:
        print(e)
    



#BRTT COMMAND
@bot.command(
    name="brtt",
    aliases=["tt"],
    help="Lança a braba do BRTT"
) 

async def brtt(ctx):

    #set photo to be sent by the command 
    brtt_photo= discord.File('./images/brtt.jpeg')
    #get the address of the text channel the message is going to be sent
    channel = ctx.channel

    await channel.send("REXPEITA", file= brtt_photo)

@bot.command(
    name="tiasfofinhas",
    aliases=["ff"],
    help="Lança a braba das Tias Fofinhas"
) 

async def tiasfofinhas(ctx):


    #set audio to be played
    audio = "./audios/jeitoSexy.mp3"

    channel = ctx.author.voice.channel
    
    #connect to the voice channel
    player = await channel.connect()    

    #player.play(discord.FFmpegPCMAudio('audio.mp3'))
    player.play(discord.FFmpegPCMAudio(audio))

    #prevents the user from quitting the bot before it finishes playing the song
    while player.is_playing():
         time.sleep(5)

    await player.disconnect()


    


#list to store all the songs' url
list_songs = []
name_songs=[]
@bot.command(
    name="play",
    aliases=["p"],
    help="Bora rebolar essa raba?!"
) 

async def play (ctx):

    #setup for player 
    YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist':'True'}
    FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}

    #
    #function that will be used for recursion later
    def check_player():

        #print statements for tracking playlist 
        print("Im in check player")
        print("New length: "+ str(len(list_songs)))

        #delete song that has just played from the list 
        list_songs.pop(0)
        name_songs.pop(0)
        
        #print statement to check list
        print("New length 2: "+ str(len(list_songs)))

        #check if list of songs is zero. If player finishes and length of list_songs is Zero, no songs is played next
        if len(list_songs) == 0:
            route = ctx.channel
            
            
        else:
            
            time.sleep(2)
            #play song which is next in the queue
            voice.play(discord.FFmpegPCMAudio(list_songs[0], **FFMPEG_OPTIONS), after=  lambda  e:  check_player())

    #get voice channel info
    voice = get(bot.voice_clients, guild=ctx.guild)
    channel = ctx.author.voice.channel 

    #get song name written by the user
    song = ctx.message.content
    song = song[2:]
    print("Playing: " + song)

    ydl_opts = {
            'format': 'beataudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192'
            }]
        }
    yt = YoutubeSearch(song, max_results=1).to_json()
 
    yt_id = str(json.loads(yt)['videos'][0]['id'])
    print("yt id is: " + yt_id)
    yt_url = 'https://www.youtube.com/watch?v='+yt_id
    print(yt_url)

    try:
        if voice.is_playing():
            print("Ta tocando vou add na fila")

            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url=yt_url, download=False)
            URL = info['formats'][0]['url']
            a = info['title']
            name_songs.append(a)
            b = len(name_songs) - 1
            
            await ctx.channel.send(f"{bot.user.name} adicionou {name_songs[b]}. Queue position: {b}")
            list_songs.append(URL)
  
        
        else:
            print("Ta tocando")

            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url=yt_url, download=False)
            URL = info['formats'][0]['url']

            #get video name
            a = info['title']

            #add the song's url and name to lists
            name_songs.append(a)
            list_songs.append(URL)

            #inform the channel song which is currently playing
            await ctx.channel.send(f"{bot.user.name} tá tocando: {name_songs[0]}")
            voice.play(discord.FFmpegPCMAudio(list_songs[0], **FFMPEG_OPTIONS),  after=lambda  e: check_player())
    except commands.errors.CommandInvokeError:
            print("Ta tocando vou add na fila")

            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url=yt_url, download=False)
            URL = info['formats'][0]['url']
            a = info['title']
            name_songs.append(a)
            b = len(name_songs) - 1
            
            await ctx.channel.send(f"{bot.user.name} adicionou {name_songs[b]}. Queue position: {b}")
            list_songs.append(URL)

        

#backgound messages to be sent every 15 min
@tasks.loop(minutes=15)
async def google():

    randNum = random.randrange(3)

    if randNum == 0:
        embed = discord.Embed(
            title=f"{bot.user.name} tem uma super dica pra você! Betina who?? So clicar: http://letmegooglethat.com/?q=como+ganhar+dinheiro+rapido",
            color= bot.embed_color,
            timestamp= datetime.datetime.now(datetime.timezone.utc)
        )
    

        embed.set_footer(
            text=bot.footer,
            icon_url=bot.footer_image
        )

    elif randNum == 1:
        embed = discord.Embed(
            title=f" AHHH MAS SE ELEGER O BOLSONARO O DOLAR CAI!! PIPIPOPO! OLHA ESSA MERDA NAS ALTURAS! Vai ver o Mickey na PQP!! Se liga nisso https://economia.uol.com.br/cotacoes/cambio/",
            color= bot.embed_color,
            timestamp= datetime.datetime.now(datetime.timezone.utc)
        )
    

        embed.set_footer(
            text=bot.footer,
            icon_url=bot.footer_image
        )

    else:
         embed = discord.Embed(
            title=f"Vamos desisntalar esse LOL!! Ve se aprende aqui: https://playerlink.gg/network ",
            color= bot.embed_color,
            timestamp= datetime.datetime.now(datetime.timezone.utc)
        )
    

         embed.set_footer(
            text=bot.footer,
            icon_url=bot.footer_image)


    #
    bot.log_channel = bot.get_channel(670030698308173824)
    await bot.log_channel.send( embed=embed)
    print("Background loop just sent a message")
    

#JOIN COMMAND
@bot.command(pass_context=True, aliases=['j', 'joi'])
async def join(ctx):
    #getting in the voice channel and connect to it, so users can play songs
    global voice
    channel = ctx.message.author.voice.channel
    voice = get(bot.voice_clients, guild=ctx.guild)

    #check if bot is connected to another voice channel

    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()
        print(f"The bot has connected to {channel}\n")

    await ctx.send(f"Joined {channel}")


    
#run the bot 
bot.run(token, bot=True, reconnect=True)


