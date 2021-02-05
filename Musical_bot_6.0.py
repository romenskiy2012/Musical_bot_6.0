#pip3 install discord.py
#pip3 install youtube-dl
#pip3 install PyNaCl
#sudo apt install ffmpeg 
# on
#sudo pacman -S ffmpeg 
#pip3 install PyYAML




########################### Дискорд
import discord
import asyncio
from discord.ext import commands
from discord.utils import get
############################

############################

############################ Модули для сервисов
#import youtube_dl

############################

############################ Системные модули
import os
from threading import Thread
from subprocess import call
from time import strftime, localtime, sleep #Для (Time)

import time
import random
############################

############################ json модуль
import json
with open("sonf.json", "r") as read_file:
    X_Pars = json.load(read_file) 
############################


############################ sql модуль
SQL_Q = [[], [], [], [], [], []]

import sqlite3

bd = sqlite3.connect("bd/B.bd")
sql = bd.cursor()

naim = ["server","id","channel","channel_id","txt_1","txt_2"]
f = 0
while f != 6:
    sql.execute(f"SELECT {naim[f]} FROM fiel")
    SQL_Q_L = sql.fetchall()
    x = 0 
    for id_user in SQL_Q_L:
        SQL_Q[f].insert(x,id_user[0])
        x = x + 1
    f = f + 1

bd.close()
print("Даза")
print(SQL_Q[1][3])
print(SQL_Q[5][0])
############################

#################################### Локальные модули

#import add

#import handler
import youtube
import bd_module
import question
import download
####################################



### Подготовка
a = True
list = os.listdir()
for list_2 in list:
    if list_2 == "Music":
        print("Такой фаел есть!")
        a = False
if a == True:
    os.mkdir("Music")

#os.rmdir("Music")
#os.mkdir("Music")
#call(["rm", "-r", "Music"])
#call(["mkdir", "Music"])


print(X_Pars)
TOKEN = X_Pars['token']
bot = commands.Bot(command_prefix=X_Pars['prefix'])
client = discord.Client()
bot.remove_command("help")


###

Turn = [] # Очереди на базу данных.
#Turn2 = [] # Очереди на базу данных.

sor = ()
video = ()
Question = [["001"], [], [], []] # Запросы.
#Question = [[233962119106789376,"001"], [769927691545215006], [785670323655016459], [False]] # Запросы.

volume1 = 0.2

async def sing_ddd(message):
    r2 = "https://cdn.discordapp.com/attachments/587366302780358688/806924319422152744/BOT_V6.0.webp"
    
    a = 0
    for id_lin in SQL_Q[3]: # В том ли чате ?
        if id_lin == message.channel.id:
            print(SQL_Q[5][a])
            qm2 = int(SQL_Q[5][a])
            qm = int(SQL_Q[4][a])
            channel_id = message.channel.id
        a = a + 1
        
        
            
    id_jgkihjkf = int(message.author.guild.id)
    msg_sa = await bot.get_guild(id_jgkihjkf).get_channel(channel_id).fetch_message(qm)
    bot.loop.create_task(msg_sa.edit(content=(r2)))
    
def checking_the_queue(message,voice):
    bd_module.deleting_a_queue(message) # Удоления из очереди трека
    id = bd_module.reading_from_a_queue(message)
    if id == "001":
        bot.loop.create_task(sing_ddd(message))
        bot.loop.create_task(voice.disconnect())
        #pass
    else:
        #bot.loop.create_task(sing(message,sasss))
        sing(message,id)

async def sing_k8ifg4(id, name_2, volume, time, views, estimation, date, message):
    r1 = (f"https://i.ytimg.com/vi/{id}/hqdefault.jpg")
    
    
    
    a = 0
    for id_lin in SQL_Q[3]: # В том ли чате ?
        if id_lin == message.channel.id:
            print(SQL_Q[5][a])
            qm2 = int(SQL_Q[5][a])
            qm = int(SQL_Q[4][a])
            channel_id = message.channel.id
        a = a + 1
        
        
            
    id_jgkihjkf = int(message.author.guild.id)
    msg_sa = await bot.get_guild(id_jgkihjkf).get_channel(channel_id).fetch_message(qm)
    bot.loop.create_task(msg_sa.edit(content=(r1)))
    
    msg_sa = await bot.get_guild(id_jgkihjkf).get_channel(channel_id).fetch_message(qm2)
    lll = f"{name_2}\n👀 {views} 👍 {estimation} 🗓️ {date}"
    bot.loop.create_task(msg_sa.edit(content=(lll)))
    
#async def sing(message,sasss):
def sing(message,id):
    print(id)

    id, name_2, volume, time, views, estimation, date = bd_module.search_ID(id)
    
    bot.loop.create_task(sing_k8ifg4(id, name_2, volume, time, views, estimation, date, message))
    #sing_k8ifg4(id, name_2, volume, time, views, estimation, date, message)
    
    sasss = f"Music/{id}.opus"

    msg = bot.get_guild(message.author.guild.id)
    voice = get(bot.voice_clients, guild=msg)

    voice.play(discord.FFmpegPCMAudio(sasss), after = lambda x: checking_the_queue(message,voice))
    voice.source = discord.PCMVolumeTransformer(voice.source)
    voice.source.volume = volume1

    







async def messenger(message,url):
    msg = bot.get_guild(message.author.guild.id)
    channel = message.author.voice.channel
    voice = get(bot.voice_clients, guild=msg)
    print("222")
    if youtube.start(url):
        print("222")
        print("Это ютуб!")
        if youtube.start_list(url):# Очеридь ли ?
            pass
        else:
            id = download.youtube_d(url,message)
            #youtube.don(url)# Скачать
            print("Готово")
            if voice and voice.is_connected():
                # добавить в базу
                print("добавить в базу")
                await voice.move_to(channel)
            else:
                voice = await channel.connect()
                print(f"Бот подключился к {channel}\n")
                #bot.loop.create_task(sing(message,sasss))
                sing(message,id)

    else:
        print("Это не ютуб!")




### Выделяем отдельный канал для асинхронных вызовов.
### Если вы знаете как можно сделать асинохонную многопоточность.
### !Сообшите!







########################

def http(url, Turn, id, id_channel, message):
    global Question
    url_index = []
    print (url)
    
    url_index.extend(url)
    url_index.append ("001")
    x = 0
    if url_index[x] == "h":
        if url_index[x + 1] == "t":
            if url_index[x + 2] == "t":
                if url_index[x + 3] == "p":
                    # Проверка на наличие вопроса
                    user_id = message.author.id
                    id_question = question.start(Question, user_id, id)
                    if id_question != False:
                        # Удолить id_question
                        #

                        #  Удолить сообшение с вопросом.
                        pass
                    print(Question)

                    # Что за сервис ?
                    bot.loop.create_task(messenger(message,url))






#######################





########################
def command(message):


    if message.content == "/add":
        bot.loop.create_task(add(message))
    if message.content == "/test":
        bot.loop.create_task(test(message))

async def test(message):
    channel = message.channel
    await channel.send("Тут!")

async def add(message):
    await message.delete()
    print(message.author.guild.name)# Имя 
    print(message.author.guild.id)# Айди
    print(message.channel.name)# Имя
    print(message.channel.id)# Айди
    msg = bot.get_guild(message.author.guild.id).get_channel(message.channel.id)
    channel = message.channel
    await channel.send("Привет")
    sleep(1)
    txt_1 = (channel.last_message_id)
    msg = await bot.get_guild(message.author.guild.id).get_channel(message.channel.id).fetch_message(txt_1)
    emoji = "⏸️"
    await msg.add_reaction(emoji)
    emoji = "▶️"
    await msg.add_reaction(emoji)
    emoji = "⏩"
    await msg.add_reaction(emoji)
    emoji = "⏭️"
    await msg.add_reaction(emoji)
    emoji = "⏹️"
    await msg.add_reaction(emoji)
    emoji = "🔄"#Повтор
    await msg.add_reaction(emoji)
    emoji = "🔊"
    await msg.add_reaction(emoji)
    emoji = "🔉"
    await msg.add_reaction(emoji)
    print(channel.last_message_id)
    



    await channel.send("Привет2")
    sleep(1)
    txt_2 = (channel.last_message_id)
    print(channel.last_message_id)

    bd_module.add(message,Turn,txt_1,txt_2,SQL_Q)
    print("САС!")



########################




### Старт бота.
@bot.event
async def on_ready():
    print("Бот онлайн!!!")


@bot.event # Слушает.
async def on_message(message):
    chat = False
    print("Да ?")
    if message.content.startswith('/'): # Команда ?
        command(message)
        pass

    else:
        for id_lin in SQL_Q[3]: # В том ли чате ?
            if id_lin == message.channel.id:
                chat = True

        if chat == True:
            await message.delete()
            if message.content == (''):# Это фаел ?
                pass

            if message.content == ('1'):# Это цифры для перемодки ?
                pass

            elif message.content.startswith('y') or message.content.startswith('Y') or message.content.startswith('n') or message.content.startswith('N'):# Ответ ?
                pass


            elif message.author.id == X_Pars['bot_id']:# Бот ?
                pass

            
            elif message.content != (''):
                id = message.author.guild.id
                id_channel = message.channel.id
                url = message.content
                
                print(url)
                variable = Thread(target=http, args=(url, Turn, id, id_channel, message))
                variable.start()




















@bot.event
async def on_raw_reaction_add(reaction):
    global volume1, repeat
    print(reaction.user_id)
    print(f"{reaction.member.display_name}#{reaction.member.discriminator}")
        
        
    #print(user.id)
    #msg_2 = bot.get_guild(int(X_Pars["guild_id"]))
    msg = bot.get_guild(reaction.member.guild.id)
    #if user.id != X_Pars["bot_id"]:
    #print(msg.author.id)
    user234id = True
    print(reaction.user_id)
    admin_list = X_Pars['admin_list']
    admin_list.append("001")
    a = 0
    #while admin_list[a] != "001":
        #if reaction.user_id == admin_list[a]:
    
    print("123")
    #ctx = ("pause")
    #await reaction.clear_reaction(reaction)
    #def on_track_end2(error):
    #    bot.loop.create_task(bot.send(":white_check_mark: Скачано!"))
    #await ctx.send(reaction) #отправляем обратно аргумент

    #await reaction.message.channel.send(reaction)
    #print(on_reaction_add)
    
    #voice = get(bot.voice_clients, guild=reaction.message.guild)
    voice = get(bot.voice_clients, guild=msg)
    #print(reaction)
    #await ('Say hello!')
    #on_track_end2
    #await reaction.message.send('Hello World!')
    print("1")
    print(reaction.emoji)
    if (str(reaction.emoji) == "⏸️"):
        #print("2")
        voice.pause()
        print("Пауза")
        
    if (str(reaction.emoji) == "⏯️"):
        print("Сердце")
    if (str(reaction.emoji) == "▶️"):
        print("Плей")
        voice.resume()
    if (str(reaction.emoji) == "⏩"):
        print("Пропуск")
        voice.stop()
    if (str(reaction.emoji) == "⏭️"):
        print("Пропуск плей листа.")
        global m11
        m11 = 1
        voice.stop()
    if (str(reaction.emoji) == "⏹️"):
        print(reaction.emoji)
        global f
        f = ["123", "001"]
        #voice.disconnect()
        voice.stop()
    if (str(reaction.emoji) == "🔄"):
        if repeat == True:
            repeat = False
        else:
            repeat = True
        print(reaction.emoji)
        print("🔂")
        print("➡️")
        
    if (str(reaction.emoji) == "🔊"):
        volume1 = volume1 + 0.1
        volume1 = round(volume1, 1)
        print(volume1)
        if volume1 > 1:
            volume1 = volume1 - 0.1
        else:
            voice.source.volume = volume1
    if (str(reaction.emoji) == "🔉"):
        volume1 = volume1 - 0.1
        volume1 = round(volume1, 1)
        print(volume1)
        if volume1 < 0.1:
            volume1 = volume1 + 0.1
        else:
            voice.source.volume = volume1
        print("3")

bot.run(TOKEN)
