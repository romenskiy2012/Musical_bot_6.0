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
import sqlite3



#################################### Локальные модули

#import add

#import handler
import youtube
import bd
import question
####################################



### Подготовка

call(["rm", "-r", "Music"])
call(["mkdir", "Music"])


print(X_Pars)
TOKEN = X_Pars['token']
bot = commands.Bot(command_prefix=X_Pars['prefix'])
client = discord.Client()
bot.remove_command("help")


###

Turn = [] # Очереди на базу данных.
sor = ()
video = ()
Question = [["001"], [], [], []] # Запросы.
#Question = [[233962119106789376,"001"], [769927691545215006], [785670323655016459], [False]] # Запросы.

volume1 = 0.2





async def sing(message):
    #sing "Music/" + message.author.guild.name + "/123.opus"
    sasss = "123.opus"
    msg = bot.get_guild(message.author.guild.id)
    voice = get(bot.voice_clients, guild=msg)


    

    #voice.play(discord.FFmpegPCMAudio(sasss), after = on_track_end)
    voice.play(discord.FFmpegPCMAudio(sasss))
    voice.source = discord.PCMVolumeTransformer(voice.source)
    voice.source.volume = volume1

    







async def messenger(message,url):
    msg = bot.get_guild(message.author.guild.id)
    channel = message.author.voice.channel
    voice = get(bot.voice_clients, guild=msg)
    if youtube.start(url):
        print("Это ютуб!")
        if youtube.start_list(url):# Очеридь ли ?
            pass
        else:
            youtube.don(url)# Скачать
            print("Готово")
            if voice and voice.is_connected():
                # добавить в базу
                print("добавить в базу")
                await voice.move_to(channel)
            else:
                voice = await channel.connect()
                print(f"Бот подключился к {channel}\n")
                bot.loop.create_task(sing(message))

    else:
        print("Это не ютуб!")




### Выделяем отдельный канал для асинхронных вызовов.
### Если вы знаете как можно сделать асинохонную многопоточность.
### !Сообшите!

async def asynchrony(message):
    await message.delete()





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
                    id2 = bd.id(id,Turn)
                    if int(id2) == id_channel: # В том лм канале ?
                        print("Да тут!")
                        bot.loop.create_task(asynchrony(message))
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
                    elif id2 == False:
                        # Убится!
                        pass
                    else:
                        print("Не тут!")


                    ### В том ли чате ?






#######################















### Старт бота.
@bot.event
async def on_ready():
    print("Бот онлайн!!!")


@bot.event # Слушает.
async def on_message(message):
    if message.content.startswith('/'): # Команда ?
        pass

    elif message.content.startswith('y') or message.content.startswith('Y') or message.content.startswith('n') or message.content.startswith('N'):# Ответ ?
        pass


    elif message.author.id == X_Pars['bot_id'] or message.content == (''):# Бот ?
        pass

    
    elif message.content != (''):
        id = message.author.guild.id
        id_channel = message.channel.id
        url = message.content
        
        print(url)
        variable = Thread(target=http, args=(url, Turn, id, id_channel, message))
        variable.start()



"""
    id = message.author.guild.id
    qm1 = bd.id(id,Turn)

    print(qm1)
    print(message.channel.id)
    if int(qm1) == message.channel.id:
        await message.delete()
    if message.author.id != bot_id and message.content != (''):
        print("Ты написал", message.content)
        rim = []
        rim.extend (message.content)

"""










bot.run(TOKEN)