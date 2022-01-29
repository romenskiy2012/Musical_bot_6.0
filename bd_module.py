#print("bd подключен!")
Turn_queue = []
Turn_queue_local = []
Turn_queue_ID = []

DEBUG = False

import random
import time
import sqlite3
import os

put = os.path.dirname(os.path.realpath(__file__)) + "/"#Путь- (part-1)

from time import strftime, localtime, sleep #Для (Time)

import mariadb
import sys

IP = "127.0.0.1"
#IP = "192.168.1.40"
#bd = mariadb.connect(user="romenskiy2012",password="",host="127.0.0.1",port=3306)
pool = mariadb.ConnectionPool(user="Musical_bot",password="",host=IP,port=3306,pool_name="web-app",pool_size=1)
try:
    bd = pool.get_connection()
except mariadb.PoolError as e:
    print(f"Error opening connection from pool: {e}")

sql = bd.cursor()


sql.execute("CREATE TABLE IF NOT EXISTS Musical_bot_bd.B (server TEXT, id BIGINT, channel TEXT, channel_id BIGINT, txt_1 BIGINT, txt_2 BIGINT)")
sql.execute("CREATE TABLE IF NOT EXISTS Musical_bot_bd.ID (id TEXT, name TEXT, volume BIGINT, time BIGINT, views BIGINT, estimation DECIMAL, date TEXT, uploaded TEXT, upload_date TEXT, description TEXT, thumbnail TEXT)")
sql.execute("CREATE TABLE IF NOT EXISTS Musical_bot_bd.log (log TEXT)")
sql.execute("CREATE TABLE IF NOT EXISTS Musical_bot_bd.choice (channel_id BIGINT, txt_1 BIGINT, user_id BIGINT, id TEXT)")





sql.execute("ALTER TABLE Musical_bot_bd.B CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci") # Смена кодировки!
sql.execute("ALTER TABLE Musical_bot_bd.ID CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci") # Смена кодировки!
sql.execute("ALTER TABLE Musical_bot_bd.log CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci") #   Смена кодировки!
sql.execute("ALTER TABLE Musical_bot_bd.choice CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci") # Смена кодировки!
bd.commit()


def bd_reconect():
    bd = pool.get_connection()
    print("ОК")


# BEGIN redis
import redis
from datetime import timedelta
r = redis.StrictRedis(
    host='127.0.0.1',
    port=6379,
    password='',
    charset="utf-8",
    decode_responses=True
)


def creature_playlist(message,url,naim):
    r.rpush(f'queue:{message.author.guild.id}:playlist:{url}:1', user_id) # id
    r.rpush(f'queue:{message.author.guild.id}:playlist:{url}:2', user_id) # Имя
    r.rpush(f'queue:{message.author.guild.id}:playlist:{url}:3', user_id) # Статус


# BEGIN Проверка шкалы времени.
timeline = "timeline"
def delete_the_timeline(index:str):
    print(f"timeline:{index}")
    r.delete(f"timeline:{index}")

def checking_the_timeline(index:str):
    if r.get(f"timeline:{index}") != None:
        return True
    else:
        return False

def creature_the_timeline(index:str):
    r.setex(f"timeline:{index}", timedelta(minutes=60*24*5), value='1')

# END

def rewind_in_the_queue(guild_id, tame_L, command):
    r.lpush(f'queue:{guild_id}:queue', command)
    r.lpush(f'queue:{guild_id}:put_it_on', tame_L)
    r.lpush(f'queue:{guild_id}:name', "-")

def adding_to_the_top_of_the_queue(message, id, name, user_id):# добавление в очередь


    r.lpush(f'queue:{message.author.guild.id}:queue', id)
    r.lpush(f'queue:{message.author.guild.id}:put_it_on', user_id)
    r.lpush(f'queue:{message.author.guild.id}:name', name)

    print(id)

def adding_to_the_queue(message, id, name, user_id):# добавление в очередь


    r.rpush(f'queue:{message.author.guild.id}:queue', id)
    r.rpush(f'queue:{message.author.guild.id}:put_it_on', user_id)
    r.rpush(f'queue:{message.author.guild.id}:name', name)

    print(id)

def deleting_a_queue(message):# удаление очереди
    print("УДОЛИТЬ ВСЁ НАХУЙ!!!")
    print(r.lrange(f'queue:{message.author.guild.id}:name', 0, -1))
    r.lpop(f'queue:{message.author.guild.id}:queue', 1)
    r.lpop(f'queue:{message.author.guild.id}:put_it_on', 1)
    r.lpop(f'queue:{message.author.guild.id}:name', 1)

def reading_from_all_queue(message): # Рисуем очередь
    channel_id_l = (r.lrange(f'queue:{message.author.guild.id}:queue', 0, -1))
    put_it_on_l = (r.lrange(f'queue:{message.author.guild.id}:put_it_on', 0, -1))
    name_l = (r.lrange(f'queue:{message.author.guild.id}:name', 0, -1))
    print(channel_id_l)
    print("SAS")
    print(len(channel_id_l))

    if  len(channel_id_l) == 0:
        return "Пусто"
    else:
        A = 0
        result = ""
        while A != len(channel_id_l): # Маразм!!!
            if put_it_on_l[A] == "system":
                name = "🇸 🇾 🇸 🇹 🇪 🇲"
            else:
                name = f"<@{put_it_on_l[A]}>"
            if A == 0:
                result = result + f"(Сейчас): `{name_l[A]}`\nURL - `https://youtu.be/{channel_id_l[A]}`\nПоставил - {name}\n\n"
            else:
                result = result + f"{A}: `{name_l[A]}`\nURL - `https://youtu.be/{channel_id_l[A]}`\nПоставил - {name}\n\n"
            A = A + 1
    return result

def reading_from_a_queue(message): # чтение из очереди

    channel_id = (r.lrange(f'queue:{message.author.guild.id}:queue', 0, -1))
    put_it_on = (r.lrange(f'queue:{message.author.guild.id}:put_it_on', 0, -1))

    if  len(channel_id) == 0:
        return "001", "001"

    if put_it_on[0] == "playlist":
        print()



    return channel_id[0], put_it_on[0]



# END


def bd_scan():
    H = os.listdir(f"{put}Music")
    sql.execute(f"SELECT id FROM Musical_bot_bd.ID")
    channel_id = sql.fetchall()
    '''
    print("faels")
    for Q in H:
        Q = Q.replace('.opus', '')
        print(Q)
    print("BD")
    for Q in channel_id:
        print(Q[0])
    '''

    FALSE_BD = []
    FALSE_FEAL = []

    #print("BD")
    for Q in H:
        Q = Q.replace('.opus', '')
        OK = False
        for Q2 in channel_id:
            #print(f"{Q} - {Q2}")
            if Q2[0] == Q:
                #print("OK")
                OK = True
                exit
        if OK:
            #print("OK")
            pass
        else:
            #print("FALSE!!!!")
            #print(f"https://www.youtube.com/watch?v={Q}")
            FALSE_BD.append(Q)

    #print("FEAL")
    for Q in channel_id:
        OK = False
        for Q2 in H:
            Q2 = Q2.replace('.opus', '')
            #print(f"{Q} - {Q2}")
            if Q2 == Q[0]:
                #print("OK")
                OK = True
                exit
        if OK:
            #print("OK")
            pass
        else:
            #print("FALSE!!!!")
            #print(f"https://www.youtube.com/watch?v={Q[0]}")
            FALSE_FEAL.append(Q[0])

    print(f"Найдено ошибок в BD - {len(FALSE_BD)}")
    print(f"Найдено ошибок в FEAL - {len(FALSE_FEAL)}")

    print("BD")
    for Q in FALSE_BD:
        print(f"https://www.youtube.com/watch?v={Q}")
    print("FEAL")
    for Q in FALSE_FEAL:
        print(f"https://www.youtube.com/watch?v={Q}")

    return FALSE_BD, FALSE_FEAL





# BEGIN choice - qwestion  вопрос


def qwestion_bd(message, txt_id, id):

    sql.execute("INSERT INTO Musical_bot_bd.choice VALUES (?, ?, ?, ?)", (message.channel.id, txt_id, message.author.id, id))
    bd.commit()

def qwestion_bd_search(message):
    sql.execute("SELECT txt_1 FROM Musical_bot_bd.choice WHERE user_id = ? AND channel_id = ?", (message.author.id, message.channel.id))
    if sql.fetchone() is None:
        return False
    sql.execute("SELECT txt_1, id FROM Musical_bot_bd.choice WHERE user_id = ? AND channel_id = ?", (message.author.id, message.channel.id))
    AAA = sql.fetchall()[0]
    channel_id = AAA[0]
    id = AAA[1]
    return channel_id, id

def qwestion_bd_rm(message_id):
    #print(message_id)
    sql.execute(f"DELETE FROM Musical_bot_bd.choice WHERE txt_1 LIKE {message_id} LIMIT 1")
    bd.commit()
    #print("ДА!")
# END

def add(message,Turn,txt_1,txt_2,txt_3):


    sql.execute("SELECT server FROM Musical_bot_bd.B WHERE server = '?'", message.author.guild.name)
    if sql.fetchone() is None:
        sql.execute("INSERT INTO Musical_bot_bd.B VALUES (?, ?, ?, ?, ?, ?, ?)", (message.author.guild.name, message.author.guild.id, message.channel.name, message.channel.id, txt_1, txt_2, txt_3))
        bd.commit()


    else:
        print("Нет")
    sql.execute("SELECT server, server FROM Musical_bot_bd.B")

    channel_id = sql.fetchall()
    print(channel_id)
    jkofgdr = (len(channel_id))

    channel_id_2 = channel_id[jkofgdr - 1]
    channel_id_2 = channel_id_2[1]

    print(channel_id)
    print(channel_id_2)


    print(f"{message.author.guild.name} = {message.author.guild.id}")
    #sql.execute(f"CREATE TABLE IF NOT EXISTS Musical_bot_bd_queue.{message.author.guild.id} (queue TEXT, put_it_on TEXT, name TEXT)")
    #sql.execute(f"ALTER TABLE Musical_bot_bd_queue.{message.author.guild.id} CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci") # Смена кодировки!

    bd.commit()

# BEGIN queue  очередь
"""
def adding_to_the_queue(message, id, name, user_id):# добавление в очередь

    print(id)
    sql.execute(f"INSERT INTO Musical_bot_bd_queue.{message.author.guild.id} VALUES(?, ?, ?)", (id, user_id, name))
    bd.commit()




def deleting_a_queue_del(message):# Шиза

    sql.execute(f"SELECT * FROM Musical_bot_bd_queue.{message.author.guild.id} LIMIT 1")
    channel_id = sql.fetchall()
    print(channel_id)
    print(len(channel_id))
    if len(channel_id) != 0:
        channel_id = channel_id[0][0]
        print(channel_id)
        sql.execute(f"DELETE FROM Musical_bot_bd_queue.{message.author.guild.id} WHERE queue LIKE '{channel_id}' LIMIT 1")
        bd.commit()


def deleting_a_queue(message):# удаление очереди
    sql.execute(f"DELETE FROM Musical_bot_bd_queue.{message.author.guild.id} LIMIT 1")
    bd.commit()

"""
"""
1: `Научно-технический рэп -  Костыль и велосипед`
URL - `https://youtu.be/wjFgOckkVYM`
Поставил - <@198886008635260929>

2:`SQWOZ BAB, THE FIRST STATION — АУФ (Right Version) ♂️ Gachi Remix`
URL - `https://youtu.be/E5r-CbNs1uc`
Поставил - <@233962119106789376>
"""

"""
def reading_from_all_queue(message): # Рисуем очередь
    sql.execute(f"SELECT * FROM Musical_bot_bd_queue.{message.author.guild.id}")
    LOFT = sql.fetchall()
    if  len(LOFT) == 0:
        return "Пусто"
    else:
        A = 0
        result = ""
        while A != len(LOFT) + 1: # Маразм!!!
            LOFT_l = LOFT[A]
            if LOFT_l[1] == "system":
                name = "🇸 🇾 🇸 🇹 🇪 🇲"
            else:
                name = f"<@{LOFT_l[1]}>"
            if A == 0:
                result = result + f"(Сейчас): `{LOFT_l[2]}`\nURL - `https://youtu.be/{LOFT_l[0]}`\nПоставил - {name}\n\n"
            else:
                result = result + f"{A}: `{LOFT_l[2]}`\nURL - `https://youtu.be/{LOFT_l[0]}`\nПоставил - {name}\n\n"
            A = A + 1
    return result

def reading_from_a_queue(message): # чтение из очереди

    sql.execute(f"SELECT * FROM Musical_bot_bd_queue.{message.author.guild.id} LIMIT 1")
    LOFT = sql.fetchall()
    if  len(LOFT) == 0:
        return "001", "001"
    LOFT = LOFT[0]


    put_it_on = LOFT[1]
    channel_id = LOFT[0]

    return channel_id, put_it_on
"""
# END




def search_random_ID(): # поиск случайного ID
    sql.execute(f"SELECT id, name FROM Musical_bot_bd.ID")
    id_list = sql.fetchall()
    id_list_id = len(id_list) - 1

    random_id_lis = random.randint(0, id_list_id)

    return id_list[random_id_lis][0], id_list[random_id_lis][1]





def search_ID(id):
    print(f"id3 - {id}")

    
    sql.execute(f"SELECT id FROM Musical_bot_bd.ID WHERE id = '{id}'")
    if sql.fetchone() is None:
        print(f"Такой фаел не зарегестрирован в базе, доложите системнову адменестраторы или програмисту об этом\n Лог: id - {id}")
        
        return False

    else:

        sql.execute(f"SELECT name, volume, time, views, estimation, date, uploaded, upload_date, thumbnail FROM Musical_bot_bd.ID WHERE id = '{id}'")

        qm1 = sql.fetchall()[0]

        name_2 = qm1[0]
        volume = qm1[1]
        time = qm1[2]
        views = qm1[3]
        estimation = qm1[4]
        date = qm1[5]
        uploaded = qm1[6]
        upload_date = qm1[7]
        thumbnail = qm1[8]

        return name_2, volume, time, views, estimation, date, uploaded, upload_date, thumbnail
        
        
    
def search_ID_rid(id, video, volume, uploaded):
    
    description = video['description']#Игра
    thumbnail = video['thumbnail']
    
    name = video['title']
    if DEBUG:print(f"name - {name}")
    views = video['view_count']
    estimation = round(video['average_rating'], 1)
    
    video3 = []
    video3.extend (video['upload_date'])
    if DEBUG:print(video3)
    video3.insert(4, ":")
    video3.insert(7, ":")
    son = 0
    video4 = ("")
    while son != 10:
        video4 = video4 + str(video3[son])
        son = son + 1
    if DEBUG:print(video4)
    
    date = video4
    
    time = video['duration']
    
    #volume = "N/D"
    
    #uploaded = message.author.id
    upload_date = (strftime("%Y %m %d %X", localtime()))#Сколько часов ?
    
    
    if DEBUG:print(thumbnail)
    bd.commit() # mariadb.InterfaceError: Server has gone away ???
    sql.execute(f"SELECT id FROM Musical_bot_bd.ID WHERE id = '{id}'")
    if sql.fetchone() is None:
        sql.execute("INSERT INTO Musical_bot_bd.ID VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (id, name, volume, time, views, estimation, date, uploaded, upload_date, description, thumbnail))
        bd.commit()

    else:
        print("Нет")
    


    
    
    
def db_add_DEL(SQL_Q): # Код маразматика!

    SQL_Q = [[], [], [], [], [], []]

    naim = ["server","id","channel","channel_id","txt_1","txt_2","txt_3"]
    f = 0
    while f != 6:
        sql.execute(f"SELECT {naim[f]} FROM Musical_bot_bd.B")
        SQL_Q_L = sql.fetchall()
        x = 0
        for id_user in SQL_Q_L:
            SQL_Q[f].insert(x,id_user[0])
            x = x + 1
        f = f + 1

    #print("Даза")
    return SQL_Q


def db_add(): # Код почти здорового человека.
    SQL_Q = [[], [], [], [], [], [], []]
    sql.execute(f"SELECT * FROM Musical_bot_bd.B")
    SQL_Q_L = sql.fetchall()
    for S in SQL_Q_L:
        x = 0
        for S_2 in S:
            SQL_Q[x].append(S_2)
            x = x + 1
    return SQL_Q

def playlist(message, id):
    
    ### Подготовка

    a = True
    list = os.listdir()
    for list_2 in list:
        if list_2 == f"bd/{message.author.guild.id}":
            print("Такой фаел есть!")
            a = False
    if a == True:
        os.mkdir(f"bd/{message.author.guild.id}")


    
