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


dotenv.load_dotenv()

tocador = 2
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
    list_songs.clear()
    
    try:
        if channel.is_connected():
        
            await channel.disconnect()

    except AttributeError as e:
        print(e)
    


# await voz.play(source="/Users/ranierymendes/Documents/DiscBot/audio.mpeg")


#BRTT COMMAND
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

def store_player(player):

    tocador = player
    print(tocador)
    return
    

def get_id(n):
    return n.id

def release_player():
    return tocador


list_songs = []

@bot.command(
    name="play",
    aliases=["p"],
    help="Bora rebolar essa raba?!"
) 

async def play (ctx):

    YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist':'True'}
    FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}


    def check_player():
        print("Im in check player")
        
        
        
        print("New length: "+ str(len(list_songs)))
        list_songs.pop(0)
        asyncio.sleep
        print(list_songs)
        print("New length 2: "+ str(len(list_songs)))

        if len(list_songs) == 0:
            route = ctx.channel
            print("Lista ta vazia")
            
        else:
            print("vou tocar essa aqui")
            print(list_songs[0])
            time.sleep(2)
            voice.play(discord.FFmpegPCMAudio(list_songs[0], **FFMPEG_OPTIONS), after=lambda e: check_player())


    voice = get(bot.voice_clients, guild=ctx.guild)
    channel = ctx.author.voice.channel 


    #store the list with the members online in the voice channel and their data
    list_users= ctx.author.voice.channel.members 
    #filters into a list that constains only their ids
    new_list = []
    for n in list_users:
        new_list.append(get_id(n=n))
     
    print(new_list)
    #checks whether the bot is already connected to the voice channel 
    #if not go ahead and connect to it

    #if not 743902306306752522 in new_list: 
        
     #   player = await channel.connect()
      #  if player.is_connected():
       #     print("Player ligou")
        #    store_player(ctx.author.voice.channel)
            

    #if  743902306306752522 in new_list: 
    #    print("Ja ta no channel")
     #   player = release_player()


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

    if voice.is_playing():
        print("Ta tocando vou add na fila")

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url=yt_url, download=False)
        URL = info['formats'][0]['url']

        list_songs.append(URL)

    else:
        print("Ta tocando")

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url=yt_url, download=False)
        URL = info['formats'][0]['url']

        list_songs.append(URL)
        voice.play(discord.FFmpegPCMAudio(list_songs[0], **FFMPEG_OPTIONS), after=lambda  e:check_player())

    


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


    #https://playerlink.gg/network
    bot.log_channel = bot.get_channel(670030020621762610)
    await bot.log_channel.send( embed=embed)
    print("oi")
    

@bot.command(pass_context=True, aliases=['j', 'joi'])
async def join(ctx):
    global voice
    channel = ctx.message.author.voice.channel
    voice = get(bot.voice_clients, guild=ctx.guild)

    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()

    await voice.disconnect()

    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()
        print(f"The bot has connected to {channel}\n")

    await ctx.send(f"Joined {channel}")

queues = {}
@bot.command(pass_context=True,name= "koe", aliases=['k'])
async def koe(ctx, url: str):

    def check_queue():
        Queue_infile = os.path.isdir("./Queue")
        if Queue_infile is True:
            DIR = os.path.abspath(os.path.realpath("Queue"))
            length = len(os.listdir(DIR))
            still_q = length - 1
            try:
                first_file = os.listdir(DIR)[0]
            except:
                print("No more queued song(s)\n")
                queues.clear()
                return
            main_location = os.path.dirname(os.path.realpath(__file__))
            song_path = os.path.abspath(os.path.realpath("Queue") + "\\" + first_file)
            if length != 0:
                print("Song done, playing next queued\n")
                print(f"Songs still in queue: {still_q}")
                song_there = os.path.isfile("song.mp3")
                if song_there:
                    os.remove("song.mp3")
                shutil.move(song_path, main_location)
                for file in os.listdir("./"):
                    if file.endswith(".mp3"):
                        os.rename(file, 'song.mp3')

                voice.play(discord.FFmpegPCMAudio("song.mp3"), after=lambda e: check_queue())
                voice.source = discord.PCMVolumeTransformer(voice.source)
                voice.source.volume = 0.07

            else:
                queues.clear()
                return

        else:
            queues.clear()
            print("No songs were queued before the ending of the last song\n")



    song_there = os.path.isfile("song.mp3")
    try:
        if song_there:
            os.remove("song.mp3")
            queues.clear()
            print("Removed old song file")
    except PermissionError:
        print("Trying to delete song file, but it's being played")
        await ctx.send("ERROR: Music playing")
        return


    Queue_infile = os.path.isdir("./Queue")
    try:
        Queue_folder = "./Queue"
        if Queue_infile is True:
            print("Removed old Queue Folder")
            shutil.rmtree(Queue_folder)
    except:
        print("No old Queue folder")

    await ctx.send("Getting everything ready now")

    voice = get(bot.voice_clients, guild=ctx.guild)

    ydl_opts = {
        'format': 'bestaudio/best',
        'quiet': True,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        print("Downloading audio now\n")
        ydl.download([url])

    for file in os.listdir("./"):
        if file.endswith(".mp3"):
            name = file
            print(f"Renamed File: {file}\n")
            os.rename(file, "song.mp3")

    voice.play(discord.FFmpegPCMAudio("song.mp3"), after=lambda e: check_queue())
    voice.source = discord.PCMVolumeTransformer(voice.source)
    voice.source.volume = 0.07

    nname = name.rsplit("-", 2)
    await ctx.send(f"Playing: {nname[0]}")
    print("playing\n")


    
#run the bot 

bot.run(token, bot=True, reconnect=True)


