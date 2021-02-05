print("bd подключен!")   
Turn_queue = []
Turn_queue_local = []
Turn_queue_ID = []


import random
import time
import sqlite3

def Turn_queue_U_ID():
    global Turn_queue_ID
    print(Turn_queue_ID)
    i_2 = (random.randint(0, 10000000000000000000))
    #return Turn
    Turn_queue_ID.append (i_2)

    Cycle = True
    while Cycle == True:
        if Turn_queue_ID[0] == i_2:
            Cycle == False
            # Начало редоктирование БД.
            #Turn.remove(i_2)
            print(Turn_queue_ID)
            return i_2
        time.sleep(0.05)# Остановка на 0.15 сек.

def Turn_queue_U_local():
    global Turn_queue_local
    print(Turn_queue_local)
    i_2 = (random.randint(0, 10000000000000000000))
    #return Turn
    Turn_queue_local.append (i_2)

    Cycle = True
    while Cycle == True:
        if Turn_queue_local[0] == i_2:
            Cycle == False
            # Начало редоктирование БД.
            #Turn.remove(i_2)
            print(Turn_queue_local)
            return i_2
        time.sleep(0.05)# Остановка на 0.15 сек.


def Turn_queue_U():
    global Turn_queue
    print(Turn_queue)
    i_2 = (random.randint(0, 10000000000000000000))
    #return Turn
    Turn_queue.append (i_2)

    Cycle = True
    while Cycle == True:
        if Turn_queue[0] == i_2:
            Cycle == False
            # Начало редоктирование БД.
            #Turn.remove(i_2)
            print(Turn_queue)
            return i_2
        time.sleep(0.05)# Остановка на 0.15 сек.


def id2(Turn):
    i_2 = (random.randint(0, 10000000000000000000))
    #return Turn
    Turn.append (i_2)

    Cycle = True
    while Cycle == True:
        if Turn[0] == i_2:
            Cycle == False
            # Начало редоктирование БД.
            #Turn.remove(i_2)
            return i_2
        time.sleep(0.05)# Остановка на 0.15 сек.


def add(message,Turn,txt_1,txt_2,SQL_Q):
    i_2 = id2(Turn)

    bd = sqlite3.connect("bd/B.bd")
    sql = bd.cursor()

    sql.execute("CREATE TABLE IF NOT EXISTS fiel (server TEXT, id TEXT, channel TEXT, channel_id TEXT, txt_1 TEXT, txt_2 TEXT)")
    bd.commit()
    sql.execute(f"SELECT server FROM fiel WHERE server = '{message.author.guild.name}'")
    if sql.fetchone() is None:
        sql.execute(f"INSERT INTO fiel VALUES ('{message.author.guild.name}', '{message.author.guild.id}', '{message.channel.name}', '{message.channel.id}', '{txt_1}', '{txt_2}')")
        bd.commit()
        x = 0 
        for id_user in SQL_Q:
            x = x + 1
        SQL_Q[0].insert(x,message.author.guild.name)
        SQL_Q[1].insert(x,message.author.guild.id)
        SQL_Q[2].insert(x,message.channel.name)
        SQL_Q[3].insert(x,message.channel.id)
        SQL_Q[4].insert(x,txt_1)
        SQL_Q[5].insert(x,txt_2)

    else:
        print("Нет")
    sql.execute("SELECT server, server FROM fiel")

    channel_id = sql.fetchall()
    print(channel_id)
    jkofgdr = (len(channel_id))

    channel_id_2 = channel_id[jkofgdr - 1]
    channel_id_2 = channel_id_2[1]

    print(channel_id)
    print(channel_id_2)

    bd_queue = sqlite3.connect("bd/queue.bd")
    sql_queue = bd_queue.cursor()
    print(message.author.guild.name)
    sql_queue.execute(f"CREATE TABLE IF NOT EXISTS '{message.author.guild.name}' (queue TEXT)")
    bd_queue.commit()
    bd_queue.close()

    Turn.remove(i_2)










'''


def id(id):
    global Turn_queue
    i_2 = id2(Turn_queue)

    bd = sqlite3.connect("bd/queue.bd")
    sql = bd.cursor()



    sql.execute("CREATE TABLE IF NOT EXISTS fiel (server TEXT, id TEXT, channel TEXT, channel_id TEXT, txt_1 TEXT, txt_2 TEXT)")
    bd.commit()
    sql.execute(f"SELECT server FROM fiel WHERE id = '{id}'")
    if sql.fetchone() is None:
        print(f"ОТЦУУТВЕНТ КАНАЛ ДЛЯ МУЗЫКИ НА СЕРВЕРЕ ID = '{id}'")
    else:
        sql.execute(f"SELECT channel_id, id FROM fiel WHERE id = '{id}'")
        id = sql.fetchall()
        id = id[0][0]
        print(id)


        bd.close()
        Turn_queue.remove(i_2)
        return id


    bd.close()
    Turn_queue.remove(i_2)
    id = False
    return id

'''

    
def adding_to_the_queue(message, id):
    global Turn_queue
    i_2 = Turn_queue_U()
    print(Turn_queue)
    bd_queue = sqlite3.connect("bd/queue.bd")
    sql_queue = bd_queue.cursor()

    sql_queue.execute(f"SELECT queue FROM '{message.author.guild.name}' WHERE queue = '001'")
    if sql_queue.fetchone() is None:
        sql_queue.execute(f"INSERT INTO '{message.author.guild.name}' VALUES ('001')")
        bd_queue.commit()
    else:
        print("Нет")

    sql_queue.execute(f"SELECT queue, queue FROM '{message.author.guild.name}'")

    channel_id = sql_queue.fetchall()
    channel_id = channel_id[0]
    channel_id = channel_id[1]
    print(channel_id)

    sql_queue.fetchone()
    dfsdfsf = f"DELETE FROM '{message.author.guild.name}' WHERE queue = '001'"
    sql_queue.execute(dfsdfsf)
    bd_queue.commit()

    sql_queue.execute(f"INSERT INTO '{message.author.guild.name}' VALUES ('{id}')")
    #channel_id = channel_id + 1
    sql_queue.execute(f"INSERT INTO '{message.author.guild.name}' VALUES ('001')")
    bd_queue.commit()
    sql_queue.execute(f"SELECT queue, queue FROM '{message.author.guild.name}'")
    channel_id = sql_queue.fetchall()
    channel_id = channel_id[0]
    channel_id = channel_id[1]
    print(channel_id)
    bd_queue.close()

    print(Turn_queue)
    Turn_queue.remove(i_2)
    print(Turn_queue)





def deleting_a_queue(message):
    global Turn_queue
    i_2 = Turn_queue_U()

    bd_queue = sqlite3.connect("bd/queue.bd")
    sql_queue = bd_queue.cursor()
    sql_queue.execute(f"SELECT * FROM '{message.author.guild.name}' ORDER BY ROWID ASC LIMIT 1")
    channel_id = sql_queue.fetchall()
    channel_id = channel_id[0]
    channel_id = channel_id[0]
    print(channel_id)
    sql_queue.execute(f"DELETE FROM '{message.author.guild.name}' WHERE queue LIKE '{channel_id}'")
    bd_queue.commit()
    print("САС")
    bd_queue.close()

    Turn_queue.remove(i_2)


def reading_from_a_queue(message):
    global Turn_queue
    i_2 = Turn_queue_U()

    bd_queue = sqlite3.connect("bd/queue.bd")
    sql_queue = bd_queue.cursor()
    sql_queue.execute(f"SELECT queue, queue FROM '{message.author.guild.name}'")
    channel_id = sql_queue.fetchall()
    channel_id = channel_id[0]
    channel_id = channel_id[1]
    print(channel_id)
    bd_queue.close()

    Turn_queue.remove(i_2)

    #return f"Music/{channel_id}.opus"
    return channel_id
    #return f"Music/{channel_id}"






def local(message, id):
    global Turn_queue_local
    i_2 = Turn_queue_U_local()
    print(Turn_queue_local)
    bd_queue = sqlite3.connect("bd/local.bd")
    sql_queue = bd_queue.cursor()

    sql_queue.execute(f"SELECT url FROM 'local' WHERE queue = '{id}'")
    if sql_queue.fetchone() is None:
        sql_queue.execute(f"SELECT queue, queue FROM '{message.author.guild.name}'")

        channel_id = sql_queue.fetchall()
        channel_id = channel_id[0]
        channel_id = channel_id[1]
        print(channel_id)
        
    else:
        print("Нету")

    print(channel_id)
    bd_queue.close()

    print(Turn_queue_U_local)
    Turn_queue_U_local.remove(i_2)
    print(Turn_queue_U_local)
    
    
    
    
def search_ID(id):
    print(f"id3 - {id}")
    global Turn_queue_ID
    i_2 = Turn_queue_U_ID()
    print(Turn_queue_ID)
    bd = sqlite3.connect("bd/ID.bd")
    sql = bd.cursor()
    
    sql.execute(f"SELECT id FROM fiel WHERE id = '{id}'")
    if sql.fetchone() is None:
        print(f"Такой фаел не зарегестрирован в базе, доложите системнову адменестраторы или програмисту об этом\n Лог: id - {id}")
        
        sql.close()
        
        print(Turn_queue_ID)
        Turn_queue_ID.remove(i_2)
        print(Turn_queue_ID)
        
        return False

    else:
        sql.execute(f"SELECT name, id FROM fiel WHERE id = '{id}'")
        qm1 = sql.fetchall()
        print(qm1)
        name_2 = qm1[0][0]
        print(name_2)
        
        sql.execute(f"SELECT volume, id FROM fiel WHERE id = '{id}'")
        channel_id = sql.fetchall()
        volume = channel_id[0][0]
        
        sql.execute(f"SELECT time, id FROM fiel WHERE id = '{id}'")
        channel_id = sql.fetchall()
        time = channel_id[0][0]
        
        sql.execute(f"SELECT views, id FROM fiel WHERE id = '{id}'")
        channel_id = sql.fetchall()
        views = channel_id[0][0]
        
        sql.execute(f"SELECT estimation, id FROM fiel WHERE id = '{id}'")
        channel_id = sql.fetchall()
        estimation = channel_id[0][0]
        
        sql.execute(f"SELECT date, id FROM fiel WHERE id = '{id}'")
        channel_id = sql.fetchall()
        date = channel_id[0][0]
        
        sql.close()
        
        print(Turn_queue_ID)
        Turn_queue_ID.remove(i_2)
        print(Turn_queue_ID)

        return id, name_2, volume, time, views, estimation, date
        
        
    
    
    
    
    
    
    
def search_ID_rid(id, video, volume):
    
    name = video['title']
    name = name.replace('{', '(')
    name = name.replace('}', ')')
    print(f"name - {name}")
    views = video['view_count']
    estimation = round(video['average_rating'], 1)
    
    video3 = []
    video3.extend (video['upload_date'])
    print(video3)
    video3.insert(4, ":")
    video3.insert(7, ":")
    son = 0
    video4 = ("")
    while son != 10:
        video4 = video4 + str(video3[son])
        son = son + 1
    print(video4)
    
    date = video4
    
    time = video['duration']
    
    #volume = "N/D"
    
    
    
    i_2 = Turn_queue_U_ID()

    bd = sqlite3.connect("bd/ID.bd")
    sql = bd.cursor()

    #sql.execute("CREATE TABLE IF NOT EXISTS fiel (id TEXT, id TEXT, channel TEXT, channel_id TEXT, txt_1 TEXT, txt_2 TEXT)")
    #bd.commit()
    sql.execute(f"SELECT id FROM fiel WHERE id = '{id}'")
    if sql.fetchone() is None:
        sql.execute(f"INSERT INTO fiel VALUES ('{id}', '{name}', '{volume}', '{time}', '{views}', '{estimation}', '{date}')") # Есть проблемы при добовление этого "https://www.youtube.com/watch?v=hJOiQo2ulyw&feature=youtu.be" sqlite3.OperationalError: near "s": syntax error

        bd.commit()

    else:
        print("Нет")
    #sql.execute("SELECT server, server FROM fiel")
    
    sql.close()

    '''
    channel_id = sql.fetchall()
    print(channel_id)
    jkofgdr = (len(channel_id))

    channel_id_2 = channel_id[jkofgdr - 1]
    channel_id_2 = channel_id_2[1]

    print(channel_id)
    print(channel_id_2)
    '''

    Turn_queue_ID.remove(i_2)
    
    
    
    
    
    
    
