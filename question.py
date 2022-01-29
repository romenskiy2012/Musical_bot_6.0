#print("question подключен!")
import youtube_dl
import random
import time
Turn2 = []

DEBUG = False

def start(Question, user_id, id):
    if DEBUG:print("111")
    x = 0
    for id_user in Question[0]:
        if DEBUG:print(id_user)
        if id_user == user_id:
            if id == Question[1][x]:
                if DEBUG:print(user_id)
                Question[3].pop(x)
                Question[3].insert(x,'n')
                if DEBUG:print(Question)
                id_question = Question[2][x]
                if DEBUG:print("111")
                return id_question
        x = x + 1
    if DEBUG:print("111")
    return False

def q_download():
    global Turn2
    if DEBUG:print("IOIIFJJIGIJGF")
    if DEBUG:print(Turn2)
    i_2 = (random.randint(0, 10000000000000000000))
    #return Turn
    Turn2.append (i_2)
    print(Turn2)
    return i_2

def q_download_question(i_2):
    if DEBUG:print(Turn2)
    Cycle = True
    while Cycle == True:
        if Turn2[0] == i_2:
            Cycle = False

        time.sleep(1)# Остановка на 0.15 сек.

def q_download_del(i_2):
    global Turn2
    Turn2.remove(i_2)
    if DEBUG:print(Turn2)
