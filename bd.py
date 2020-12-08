print("bd подключен!")   


import random
import time
import sqlite3


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


def id(id,Turn):
    i_2 = id2(Turn)

    bd = sqlite3.connect("bd/B.bd")
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
        Turn.remove(i_2)
        return id


    bd.close()
    Turn.remove(i_2)
    id = False
    return id

    
