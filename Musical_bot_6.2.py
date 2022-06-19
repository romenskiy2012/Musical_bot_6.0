#pip3 install discord.py
#pip3 install youtube-dl
#pip3 install PyNaCl
#sudo apt install ffmpeg
# on
#sudo pacman -S ffmpeg
#pip3 install PyYAML

DEBUG = True

# BEGIN Рисуем закгузку в кансоль.


ESC = b'\x1B' # Начинает ESC-последовательность
LF = b'\x0A' # \n Перевод на следующую строку
CR = b'\x0D' # \r Перевод в начало строки
CSI = b'[' # Ввод управляющей последовательности
EL = b'K' # Очистить строку. 2 - всю строку

import sys
import shutil




screen_size = shutil.get_terminal_size()
sys.stdout.buffer.write(LF*screen_size.lines)
# прокрутить экран в конец


i = 0 # счётчик

def nprint(text):
    global i
    sys.stdout.buffer.write(ESC+CSI+b'2'+EL+CR)
    # стирает строчку и переходит в начало
    print(text)
    # на свободной строчке пишем текст и переходим на новую
    print('progress: '+ '|'*i + '='*(10-i) , i*10, '%', end='')
    # а потом обновляем прогресс-бар
    # end='' - значит остаемся в строке
    sys.stdout.flush()
    # для отрисовки недопечатанной строки
    i+=1

def nprint2(text, i):
    j = int(i)
    i = int(i) / 10
    i = int(i)
    sys.stdout.buffer.write(ESC+CSI+b'2'+EL+CR)
    print(text)
    print('progress: '+ '|'*i + '='*(10-i) , j, '%', end='')
    sys.stdout.flush()


# END

########################### Дискорд
import discord
import asyncio
from discord.ext import commands, tasks
from discord.utils import get
############################

nprint("Подключения дискорд API")


############################

############################ Модули для сервисов
#import youtube_dl

############################

############################ Системные модули
import os
from threading import Thread
from subprocess import call
from time import strftime, localtime, sleep, time, gmtime#Для (Time)

#import time
import random
############################

nprint("Подключения системных модулей")


put = os.path.dirname(os.path.realpath(__file__)) + "/"#Путь- (part-1)

############################ json модуль
import json
with open(f"{put}sonf.json", "r") as read_file:
    X_Pars = json.load(read_file)
############################
nprint("Подключения json модуль")

#################################### Локальные модули

#import add

#import handler
import youtube
nprint("Подключения youtube")
import bd_module
nprint("Подключения bd_module")
import question
nprint("Подключения question")
import download
nprint("Подключения download")
import water_handler
nprint("Подключения water_handler")
import time_translation

import time_mark
import bot_gui
####################################


# BEGIN sql модуль
############################ sql модуль
SQL_Q = [[], [], [], [], [], [], []]


SQL_Q = bd_module.db_add(SQL_Q)

#print(SQL_Q[5][0])
'''
print("########################")
for id_user in SQL_Q[0]:
    print(id_user)
print("########################")
'''
############################
# END
nprint("Создания копии серверов")



### Подготовка

a = True
list = os.listdir()
for list_2 in list:
    if list_2 == "Music":
        #print("Такой фаел есть!")
        a = False
if a == True:
    os.mkdir("Music")
    nprint("Все папки на месте!")
else:
    nprint("Создания папок!")



#os.rmdir("Music")
#os.mkdir("Music")
#call(["rm", "-r", "Music"])
#call(["mkdir", "Music"])


#print(X_Pars)
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

volume1 = 0.2 # Громкость!



# BEGIN Редоктирование сообшения.

################################################################################# Редоктирование сообшения.

async def sing_ddd(message, voice): # Редоктирование сообшения.
    msg = bot.get_guild(message.guild.id)
    await voice.disconnect()
    r2 = X_Pars['preview']
    #r2 = "https://cdn.discordapp.com/attachments/587366302780358688/806924319422152744/BOT_V6.0.webp"

    a = 0
    for id_lin in SQL_Q[3]: # Узноём номер сообшений.
        if id_lin == message.channel.id:
            print(SQL_Q[5][a])
            qm2 = int(SQL_Q[5][a])
            qm = int(SQL_Q[4][a])
            channel_id = message.channel.id
        a = a + 1



    id_jgkihjkf = int(message.author.guild.id)
    msg_sa = await bot.get_guild(id_jgkihjkf).get_channel(channel_id).fetch_message(qm)
    bot.loop.create_task(msg_sa.edit(content=(r2)))




def checking_the_queue(message,voice, index): # Проверка на следуйший трек.
    bd_module.delete_the_timeline(index)
    id , time_L = bd_module.reading_from_a_queue(message)
    if id == "stop":
        bd_module.deleting_a_queue(message) # Удоления из очереди трека
        bot.loop.create_task(sing_ddd(message, voice))
    else:
        if id == "rewind":
            start_position = time_L
        else:
            start_position = 0
        bd_module.deleting_a_queue(message) # Удоления из очереди трека
        id , put_it_on = bd_module.reading_from_a_queue(message)
        if id == "001":
            id, name = bd_module.search_random_ID()
            bd_module.adding_to_the_queue(message, id, name, "system")
            sing(message,id, put_it_on, start_position)


            #bot.loop.create_task(sing_ddd(message))
            #bot.loop.create_task(voice.disconnect())
            #pass
        else:
            #bot.loop.create_task(sing(message,sasss))
            sing(message,id, put_it_on, start_position)

async def sing_k8ifg4(id, name_2, volume, time, views, estimation, date, message, uploaded, upload_date, put_it_on, thumbnail, start_position): # Редоктирование сообшения.



    r1 = thumbnail
    if thumbnail == "" or thumbnail == None:
        r1 = (f"https://i.ytimg.com/vi/{id}/hqdefault.jpg")



    a = 0
    for id_lin in SQL_Q[3]: # Узноём номер сообшений.
        if id_lin == message.channel.id:
            print(SQL_Q[5][a])
            qm3 = int(SQL_Q[6][a])
            qm2 = int(SQL_Q[5][a])
            qm = int(SQL_Q[4][a])
            channel_id = message.channel.id
        a = a + 1




    id_jgkihjkf = int(message.author.guild.id)
    msg_sa = await bot.get_guild(id_jgkihjkf).get_channel(channel_id).fetch_message(qm)
    bot.loop.create_task(msg_sa.edit(content=(r1)))

    msg_sa = await bot.get_guild(id_jgkihjkf).get_channel(channel_id).fetch_message(qm2)
    if uploaded != "N/D":
        uploaded = f"<@{uploaded}>"
    if put_it_on == "001" or put_it_on == "" or uploaded == None:
        put_it_on = "🇸 🇾 🇸 🇹 🇪 🇲"
    else:
        put_it_on = f"<@{put_it_on}>"

    lll = f"{name_2}\n👀 {views} 👍 {estimation} 🗓️ {date} \n💾 {uploaded} \n💾🗓️ {upload_date} \n✅ {put_it_on} \nТрек готов за {preparation_time3} Сек !\n{start_position} - {time}"





    bot.loop.create_task(msg_sa.edit(content=(lll)))

    """
    a = 0
    for id_lin in SQL_Q[3]: # Узноём номер сообшений.
        if id_lin == message.channel.id:
            qm3 = int(SQL_Q[6][a])
            channel_id = message.channel.id
        a = a + 1
    """
    queue = bd_module.reading_from_all_queue(message) # Очередь
    msg_sa = await bot.get_guild(id_jgkihjkf).get_channel(channel_id).fetch_message(qm3)
    bot.loop.create_task(msg_sa.edit(content=(queue)))


#################################################################################
# END


# BEGIN ПЕТЬ!
def convert_to_preferred_format(sec):
    sec = sec % (24 * 3600)
    hour = sec // 3600
    sec %= 3600
    min = sec // 60
    sec %= 60
    if hour == 0:
        return (f"{min}:{sec}")
    else:
        return (f"{hour}:{min}:{sec}")

theme = 2



async def timeline(message, time_SSS, lll, index, start_position, description):
    description_list = ""
    if description != None or description != "":
        hub_time, hub_name = time_mark.init_read(description)
    if len(hub_name) == len(hub_time):
        a = 0
        for hub_time_l in hub_time:
            description_list = description_list + f"{hub_time_l} - {hub_name[a]}\n"
            a = a + 1
    else:
        print(f"!!!КОНФЛИКТ!!!\n{len(hub_name)} != {len(hub_time)}")
    def description_list_target_ALL(hub_time, hub_name, target_id):
        description_list_target = ""
        if len(hub_name) == len(hub_time):
            a = 0
            for hub_time_l in hub_time:
                ty_res = gmtime(hub_time_l)
                res = strftime("%H:%M:%S",ty_res)
                #print(res)
                if a == target_id:
                    description_list_target = description_list_target + f"➡️ `{res}` - {hub_name[a]} ⬅️\n"
                else:
                    description_list_target = description_list_target + f"🔘 `{res}` - {hub_name[a]}\n"
                a = a + 1
        else:
            print(f"!!!КОНФЛИКТ!!!\n{len(hub_name)} != {len(hub_time)}")
        #print(description_list_target)
        return description_list_target
    def ALA(start_position, hub_time, hub_name):
        M = 0
        for L in hub_time:
            if L >= start_position:
                if len(hub_name) >= M:
                    return hub_name[M - 1], M - 1
            M = M + 1
        return None
    slips_l = 10
    L_1 = "```\n╔════════════════════════════════╗\n"
    L_3 = "\n╚════════════════════════════════╝```"
    id_jgkihjkf = int(message.author.guild.id)
    a = 0
    for id_lin in SQL_Q[3]: # Узноём номер сообшений.
        if id_lin == message.channel.id:
            qm2 = int(SQL_Q[5][a])
            channel_id = message.channel.id
        a = a + 1
    print("Жив ?")
    await asyncio.sleep(5)
    start_position = int(start_position) + 5
    print("Жив ?2")
    msg_sa = await bot.get_guild(id_jgkihjkf).get_channel(channel_id).fetch_message(qm2)
    while bd_module.checking_the_timeline(index):
        time_p = time_SSS/100
        time_pS = int(start_position/time_p)
        i = int(int(time_pS)*0.3)
        L_2 = f"║ {'█' * i}{' ' * (30 - i)} ║ "
        time_SSS_Q = convert_to_preferred_format(time_SSS)
        start_position_Q = convert_to_preferred_format(start_position)
        name, target_id = ALA(start_position, hub_time, hub_name)
        if theme == 0:
            bot.loop.create_task(msg_sa.edit(content=(f"{lll}{L_1+L_2+L_3}{start_position_Q} - {time_SSS_Q} {time_pS}%\n➡️ {name} ⬅️")))
        elif theme == 1:
            bot.loop.create_task(msg_sa.edit(content=(f"{lll}{L_1+L_2+L_3}{start_position_Q} - {time_SSS_Q} {time_pS}%\n{description_list}")))
        elif theme == 2:
            description_list_target = description_list_target_ALL(hub_time, hub_name, target_id)
            bot.loop.create_task(msg_sa.edit(content=(f"{lll}{L_1+L_2+L_3}{start_position_Q} - {time_SSS_Q} {time_pS}%\n{description_list_target}")))
        await asyncio.sleep(slips_l)
        start_position = int(start_position) + slips_l
"""
async def timeline(message, time_SSS, voice, lll, index):
    sor = ""
    GAMENAME = ""
    lll_2 = [
    f"```\n╔════════════════════════════════╗\n║                                ║ {sor}-{GAMENAME}\n╚════════════════════════════════╝```\n", f"```\n╔════════════════════════════════╗\n║ ███                            ║ {sor}-{GAMENAME}\n╚════════════════════════════════╝```\n", f"```\n╔════════════════════════════════╗\n║ ██████                         ║ {sor}-{GAMENAME}\n╚════════════════════════════════╝```\n", f"```\n╔════════════════════════════════╗\n║ █████████                      ║ {sor}-{GAMENAME}\n╚════════════════════════════════╝```\n", f"```\n╔════════════════════════════════╗\n║ ████████████                   ║ {sor}-{GAMENAME}\n╚════════════════════════════════╝```\n", f"```\n╔════════════════════════════════╗\n║ ███████████████                ║ {sor}-{GAMENAME}\n╚════════════════════════════════╝```\n", f"```\n╔════════════════════════════════╗\n║ ██████████████████             ║ {sor}-{GAMENAME}\n╚════════════════════════════════╝```\n", f"```\n╔════════════════════════════════╗\n║ █████████████████████          ║ {sor}-{GAMENAME}\n╚════════════════════════════════╝```\n", f"```\n╔════════════════════════════════╗\n║ ████████████████████████       ║ {sor}-{GAMENAME}\n╚════════════════════════════════╝```\n", f"```\n╔════════════════════════════════╗\n║ ██████████████████████████     ║ {sor}-{GAMENAME}\n╚════════════════════════════════╝```\n", f"```\n╔════════════════════════════════╗\n║ ██████████████████████████████ ║ {sor}-{GAMENAME}\n╚════════════════════════════════╝```\n"]


    print(voice.timestamp)
    id_jgkihjkf = int(message.author.guild.id)
    a = 0
    for id_lin in SQL_Q[3]: # Узноём номер сообшений.
        if id_lin == message.channel.id:
            qm2 = int(SQL_Q[5][a])
            channel_id = message.channel.id
        a = a + 1
    print("Жив ?")
    await asyncio.sleep(5)
    print("Жив ?2")
    msg_sa = await bot.get_guild(id_jgkihjkf).get_channel(channel_id).fetch_message(qm2)
"""
"""
    print("Жив ?3")
    while True:
        print("Жив ?4")
        await asyncio.sleep(10)
        print("Жив ?5")
        print(voice.timestamp/100000)
        print("Жив ?6")
        bot.loop.create_task(msg_sa.edit(content=(f"{lll}\n{int(voice.timestamp/100000)} - {time}")))
        print("Жив ?7")

"""
"""
    while bd_module.checking_the_timeline(index):
        bot.loop.create_task(msg_sa.edit(content=(f"{lll}\n{int(voice.timestamp/500000)} - {time} {int(voice.timestamp/500000*(time/100))}%")))
        await asyncio.sleep(10)
"""
#async def sing(message,sasss):

def sing(message,id, put_it_on, start_position):  ################## ПЕТЬ!
    print(id)

    name_2, volume, time, views, estimation, date, uploaded, upload_date, thumbnail, description = bd_module.search_ID(id)

    bot.loop.create_task(sing_k8ifg4(id, name_2, volume, time, views, estimation, date, message, uploaded, upload_date, put_it_on, thumbnail, start_position))
    #sing_k8ifg4(id, name_2, volume, time, views, estimation, date, message)

    sasss = f"{put}Music/{id}.opus"

    msg = bot.get_guild(message.author.guild.id)
    voice = get(bot.voice_clients, guild=msg)

    #voice.play(discord.FFmpegPCMAudio(sasss), after = lambda x: checking_the_queue(message,voice))

    #start_position = 30000 # - пусть надо начать с 5 сек (5000 мсек)
    #FFmpegPCMAudio(b.read(), pipe=True, options=f"-ss {start_point / 1000}") # - для BytesIO

    if uploaded != "N/D":
        uploaded = f"<@{uploaded}>"
    if put_it_on == "001" or put_it_on == "" or uploaded == None:
        put_it_on = "🇸 🇾 🇸 🇹 🇪 🇲"
    else:
        put_it_on = f"<@{put_it_on}>"

    lll = f"{name_2}\n👀 {views} 👍 {estimation} 🗓️ {date} \n💾 {uploaded} \n💾🗓️ {upload_date} \n✅ {put_it_on} \nТрек готов за {preparation_time3} Сек !"


    index = str(random.randint(0, 100000)) + str(random.randint(0, 100000))
    bd_module.creature_the_timeline(index)


    #task = asyncio.create_task(timeline(message, time, voice, lll))
    #voice.play(discord.FFmpegPCMAudio(sasss, options=f"-ss {start_position}"), after = lambda x: checking_the_queue(message,voice,task))
    sas = voice.play(discord.FFmpegPCMAudio(sasss, options=f"-ss {start_position}"), after = lambda x: checking_the_queue(message, voice, index))
    #print(after)
    print(sas)
    print(sas)
    print(sas)
    print(sas)
    print(sas)
    print(sas)

    voice.source = discord.PCMVolumeTransformer(voice.source)
    voice.source.volume = volume1
    
    #bot.loop.create_task(timeline(message, time, lll, index, start_position, description)) #
    bot.loop.create_task(bot_gui.timeline(bot, SQL_Q, message, time, lll, index, start_position, description))




    #client.voice_clients[0].play(discord.FFmpegPCMAudio('./source.mp3')) # - воспроизводим обрезанный файл


    #start_position = 5000 # - пусть надо начать с 5 сек (5000 мсек)
#FFmpegPCMAudio(b.read(), pipe=True, options=f"-ss {start_point / 1000}") # - для BytesIO

#FFmpegPCMAudio('my_song.mp3', options=f"-ss {start_point / 1000}")




#################################################################################

# END


async def qwestion(url, message):
    channel = message.channel
    await channel.send("Плейлист ?\ny/n")
    sleep(1)
    txt_id = (channel.last_message_id)
    bd_module.qwestion_bd(message, txt_id, url)

async def SSSS(message,url, id, put_it_on):
    #bot.loop.create_task(messenger_2(message,url, id, put_it_on))
    messenger_2(message,url, id, put_it_on).start()



# BEGIN Проверкак что это. и Подключение или добовления.

async def messenger(message,url): # №1  Проверкак что это.
    if DEBUG: print("222")
    if youtube.start(url):
        if DEBUG: print("222")
        if DEBUG: print("Это ютуб!")
        if youtube.start_list(url):# Очеридь ли ?
            if DEBUG: print("Заглушка")
            #qwestion(url, Turn, id, id_channel, message)
            id = water_handler.youtube(url) ### ВНИМАНИЕ!!! ЗАГЛУШКА!!!
            url = f"https://www.youtube.com/watch?v={id}" ### ВНИМАНИЕ!!! ЗАГЛУШКА!!!
            #bot.loop.create_task(qwestion(url, message)) # TODO Очередь не доделона, донако этот кусое её включит, (Перед этим закоментируйте заглушки рядом.)
            print("SAS111")
            #asyncio.run(qwestion(url, message))
            print("SAS222")
            await messenger(message,url) ### ВНИМАНИЕ!!! ЗАГЛУШКА!!!

            pass
        else:
            if DEBUG: print("2")
            id, name = await download.youtube_d(url,message)
            if id == False:
                channel = message.channel
                await channel.send("Стрим, нельзя!")
                sleep(2)
                txt_id = (channel.last_message_id)
                sleep(3)
                msg = await message.channel.fetch_message(txt_id)
                await msg.delete()

            #youtube.don(url)# Скачать
            if DEBUG: print("Готово")
            preparation_time2 = time()
            global preparation_time3
            preparation_time3 = (preparation_time2 - preparation_time)
            preparation_time3 = round(preparation_time3, 2)
            if DEBUG: print(preparation_time3)
            if DEBUG: print("3")
            put_it_on = message.author.id
            await messenger_2(message,url, id, put_it_on, name)

            # BEGIN Какойто кринж

            #bot.loop.create_task(messenger_2(message,url, id, put_it_on, name))
            #bot.loop.create_future(messenger_2(message,url, id, put_it_on))

            print("SAS")

            #asyncio.run(messenger_2(message,url, id, put_it_on))



            #tasks = [bot.loop.create_task(messenger_2(message,url, id, put_it_on))]
            #wait_tasks = asyncio.wait(tasks)
            #ioloop.run_until_complete(wait_tasks)
            #ioloop.close()

            #asyncio.run(messenger_2(message,url, id, put_it_on))
            #asyncio.run(messenger_2(message,url, id, put_it_on))
            #asyncio.run(SSSS(message,url, id, put_it_on))
            print("SAS121")

            #messenger_2(message,url, id)
            #task1 = asyncio.create_task(messenger_2(message,url, id))
            # END
    else:
        if DEBUG: print("Это не ютуб!")

# END

async def messenger_2(message,url, id, put_it_on, name): # №2     Подключение или добовления.
    if DEBUG: print("4")
    msg = bot.get_guild(message.author.guild.id)
    channel = message.author.voice.channel
    voice = get(bot.voice_clients, guild=msg)
    if DEBUG: print("5")
    if voice and voice.is_connected():
        # добавить в базу
        if DEBUG: print("добавить в базу")
        bd_module.adding_to_the_queue(message, id, name, message.author.id)

        # BEGIN Кринж с обновлением очереди.
        id_jgkihjkf = int(message.author.guild.id)
        a = 0
        for id_lin in SQL_Q[3]: # Узноём номер сообшений.
            if id_lin == message.channel.id:
                qm3 = int(SQL_Q[6][a])
                channel_id = message.channel.id
            a = a + 1

        queue = bd_module.reading_from_all_queue(message) # Очередь
        msg_sa = await bot.get_guild(id_jgkihjkf).get_channel(channel_id).fetch_message(qm3)
        bot.loop.create_task(msg_sa.edit(content=(queue)))
        if DEBUG: print(queue)
        # END



        await voice.move_to(channel)
    else:
        if DEBUG: print("6")
        bd_module.adding_to_the_top_of_the_queue(message, id, name, message.author.id)
        voice = await channel.connect()
        if DEBUG: print(f"Бот подключился к {channel}\n")
        #bot.loop.create_task(sing(message,sasss))
        start_position = 0
        sing(message,id, put_it_on, start_position)




### Выделяем отдельный канал для асинхронных вызовов.
### Если вы знаете как можно сделать асинохонную многопоточность.
### !Сообшите!
#################################################################################





################################################

async def http(url, Turn, id, id_channel, message):


    global Question
    url_index = []
    if DEBUG: print (url)

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
                    if DEBUG: print(Question)

                    # Что за сервис ?
                    #variable2 = Thread(target=messenger, args=(message,url))
                    #variable2.start()
                    if DEBUG: print("1")
                    #messenger(message,url)
                    #bot.loop.create_task(messenger(message,url))
                    #task2 = asyncio.create_task(messenger(message,url))

                    #variable2 = Thread(target=messenger, args=(message,url))
                    #variable2.start()

                    #await messenger(message,url)
                    #asyncio.create_task(messenger(message,url))
                    await messenger(message,url)

                    if DEBUG: print("SSS")





###############################################



preparation_time = ()
preparation_time3 = ()

# BEGIN Консольные команды.

################################################
def command(message): # Консольные команды.


    if message.content == "!add":
        bot.loop.create_task(add(message))
    if message.content == "!test":
        bot.loop.create_task(test(message))

async def test(message): # /test
    channel = message.channel
    await channel.send("Тут!")

async def add(message): # /add
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
    await channel.send("Привет3")
    sleep(1)
    txt_3 = (channel.last_message_id)
    print(channel.last_message_id)

    bd_module.add(message,Turn,txt_1,txt_2,txt_3)
    #bd_module.add(message,Turn,txt_1,txt_2,SQL_Q)
    print("САС!")
    global SQL_Q
    SQL_Q = bd_module.db_add(SQL_Q)


    print("########################")
    for id_user in SQL_Q[0]:
        print(id_user)
    print("########################")

# END

# BEGIN Консольные команды из консоли.

async def STOP():
    #await bot.logout() # Остановка бота
    await bot.close()


def tis():
    Q = True
    while Q == True:
        I = input()
        if I == "/stop":
            print("Завершение")
            bot.loop.create_task(STOP())
            Q = False
        if I == "/h" or I == "/help":
            print("/stop - Выключает всё.")
            print("/Restart_API - Переподключается к API Discord.")
            print("/Restart_BOT - Перезагружает всё.")
            print("/BD_info - Покозать информацию о BD.")
            print("/BD_reconect - Преподключение к BD.")
            print("/BD_scan - Просканировать базу треков на целосность.")
            print("/BD_rm_server <SERVER> - Удалить и обновить сервер из BD")
            print("/BD_updeite_server <SERVER> - Синхронизировать весь список серверов в BD с Local_BD")
            print("/updeite_jison - Обновить информацию о json файле.")
        if I == "/BD_reconect":
            bd_module.bd_reconect()
        if I == "/BD_scan":
            FALSE_BD, FALSE_FEAL = bd_module.bd_scan()
            if len(FALSE_BD) == 0 and len(FALSE_FEAL) == 0:
                print("База данных не имеет отклонений от файлов!")
            else:
                i = input("Имеются отклонения, попытатся дополнить \nнедостаюшие файлы или информацию ?\nY/N\n")
                if  i == "Y" or i == "y":
                    if len(FALSE_BD) != 0:
                        if len(FALSE_BD) <= 0:
                            JJJ = len(FALSE_BD) / 100
                        else:
                            JJJ = 100 / len(FALSE_BD)
                        i = 0
                        for id in FALSE_BD:
                            url = (f"https://www.youtube.com/watch?v={id}")
                            #nprint2(url, i)
                            nprint2(url, i)
                            name = f"{put}Music/{id}.opus"
                            video = youtube.yyy(url)
                            youtube.don(url,id,name) # Скачивание
                            volume = os.path.getsize(name)
                            bd_module.search_ID_rid(id, video, volume, "N/D")
                            i = i + JJJ
                        nprint2("Готово!", i)

                    #if len(FALSE_BD) != 0:
                        #for id in FALSE_FEAL:
                    print("\n")
                else:
                    print("Востоновление отменено!")

# END

### Старт бота.
@bot.event
async def on_ready():
    nprint("Бот онлайн!!!")
    print("\n#########Сервера#########")
    for id_user in SQL_Q[0]:
        print(id_user)
    print("#########################")
    variable = Thread(target=tis)
    variable.start()
    #print("Бот онлайн!!!")

numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]



@bot.event # Слушает.
async def on_message(message):
    chat = False
    if DEBUG: print("Да ?")
    if message.content.startswith(X_Pars['prefix']): # Команда ?
        command(message)
        pass

    else:
        for id_lin in SQL_Q[3]: # В том ли чате ?
            if id_lin == message.channel.id:
                chat = True

        if chat == True:
            if message.author.id != X_Pars['bot_id']:# Бот ?
                await message.delete()
                if DEBUG: print(message.author.id)

            if message.content == (''):# Это фаел ?
                pass
            for A in numbers:
                if message.content.startswith(A):# Это цифры для перемодки ?
                    print("SSSSSSSSSSSSSSS")
                    start_position = time_translation.timeL(message.content)
                    print(start_position)
                    bd_module.rewind_in_the_queue(message.guild.id, start_position, "rewind")
                    msg = bot.get_guild(message.guild.id)
                    voice = get(bot.voice_clients, guild=msg)
                    voice.stop()

            else:
                if message.content.startswith('y') or message.content.startswith('Y') or message.content.startswith('n') or message.content.startswith('N'):# Ответ ?
                    message_id, url = bd_module.qwestion_bd_search(message)
                    if message_id != False:
                        msg = await message.channel.fetch_message(message_id)
                        await msg.delete()
                        bd_module.qwestion_bd_rm(message_id)
                        if message.content.startswith('y') or message.content.startswith('Y'):
                            print("A ,,,")
                            #if DEBUG: print("Плейлист ?\ny/n")
                            url_S = youtube.playlist_pars(url)
                            env = os.environ.copy()
                            env["URL"] = f"https://www.youtube.com/playlist?list={url_S}"
                            proc = await asyncio.create_subprocess_exec(sys.executable, f"{put}run.py", env=env)
                            await proc.wait()
                            print(proc.returncode)

                        if message.content.startswith('n') or message.content.startswith('N'):
                            if DEBUG: print("Не плейлист")
                            id = water_handler.youtube(url)
                            url = f"https://www.youtube.com/watch?v={id}"
                            id = await download.youtube_d(url,message)
                            put_it_on = message.author.id
                            #await messenger_2(message,url, id, put_it_on, name) Имени нету!!!



                    pass





                elif message.content != (''):
                    global preparation_time
                    preparation_time = time()
                    id = message.author.guild.id
                    id_channel = message.channel.id
                    url = message.content

                    if DEBUG: print(url)

                    #variable = Thread(target=http, args=(url, Turn, id, id_channel, message))
                    #variable.start()

                    #asyncio.run(http(url, Turn, id, id_channel, message))
                    await http(url, Turn, id, id_channel, message)
                    print("Я 1 а ты ?")
                    #http(url, Turn, id, id_channel, message)
                    #await http(url, Turn, id, id_channel, message)
                    #await asyncio.bot.loop.create_task(http(url, Turn, id, id_channel, message))
                    #await bot.loop.create_task(await http(url, Turn, id, id_channel, message))
                    #print("Я 2 а ты ?")
                    #print("SSSSSSSSSSSSSSSSSSSSSSSSSs")
                    #task3 = asyncio.create_task(http(url, Turn, id, id_channel, message))







# BEGIN Кнопки

@bot.event
async def on_raw_reaction_add(reaction): # Сделать проверку на то, кто это
    global volume1, repeat
    if DEBUG: print(reaction.user_id)
    if reaction.user_id != X_Pars['bot_id']:# Бот ?
        if DEBUG: print(f"{reaction.member.display_name}#{reaction.member.discriminator}")


        #print(user.id)
        #msg_2 = bot.get_guild(int(X_Pars["guild_id"]))
        msg = bot.get_guild(reaction.member.guild.id)
        #if user.id != X_Pars["bot_id"]:
        #print(msg.author.id)
        user234id = True
        if DEBUG: print(reaction.user_id)
        admin_list = X_Pars['admin_list']
        admin_list.append("001")
        a = 0
        #while admin_list[a] != "001":
            #if reaction.user_id == admin_list[a]:

        if DEBUG: print("123")
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
        if DEBUG: print("1")
        if DEBUG: print(reaction.emoji)
        if (str(reaction.emoji) == "⏸️"):
            #print("2")
            voice.pause()
            if DEBUG: print("Пауза")

        if (str(reaction.emoji) == "⏯️"):
            if DEBUG: print("Сердце")

        if (str(reaction.emoji) == "▶️"):
            if DEBUG: print("Плей")
            voice.resume()
        if (str(reaction.emoji) == "⏩"):
            if DEBUG: print("Пропуск")
            voice.stop()
        if (str(reaction.emoji) == "⏭️"):
            if DEBUG: print("Пропуск плей листа.")
            print(voice.timestamp/100000)
            print(voice.sequence)
            print(voice._lite_nonce)
            print(voice._player.loops)
        if (str(reaction.emoji) == "⏹️"):
            if DEBUG: print(reaction.emoji)
            bd_module.rewind_in_the_queue(reaction.member.guild.id, "-", "stop")
            voice.stop()
        """
        if (str(reaction.emoji) == "🔄"):
            message = reaction.message
            id , put_it_on = bd_module.reading_from_a_queue(message)
            start_position = 30000
            sing(message,id, put_it_on, start_position)
            #if repeat == True:
                #repeat = False
            #else:
                #repeat = True
            if DEBUG: print(reaction.emoji)
            if DEBUG: print("🔂")
            if DEBUG: print("➡️")
        """
        if (str(reaction.emoji) == "🔊"):
            volume1 = volume1 + 0.1
            volume1 = round(volume1, 1)
            if DEBUG: print(volume1)
            if volume1 > 1:
                volume1 = volume1 - 0.1
            else:
                voice.source.volume = volume1
        if (str(reaction.emoji) == "🔉"):
            volume1 = volume1 - 0.1
            volume1 = round(volume1, 1)
            if DEBUG: print(volume1)
            if volume1 < 0.1:
                volume1 = volume1 + 0.1
            else:
                voice.source.volume = volume1
            if DEBUG: print("3")
# END

bot.run(TOKEN)

