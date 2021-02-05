import youtube_dl
import os
print("youtube подключен!")  

def start(url):
    if start_1(url):
        print("Это ютуб длинный.")
        return True
    if start_2(url):
        print("Это ютуб короткий.")
        return True
    print("Это не длинный и не короткий ютуб.")
    return False

def start_1(url):
    sas312 = ['y', 'o', 'u', 't', 'u', 'b', 'e', '.', 'c', 'o', 'm']
    f1 = (url)
    f2 = []
    f2.extend (f1)
    #print(f2)
    #if (f2[7) == "/":
    shit = False
    if shit == False:
        #print("/")
        f2.append ("001") #Конец текста "Замыкатель"
        Cycle01 = 0
        x = 0
        y = 0
        #print("Ок!1")
        while Cycle01 < 1:
            #print("Ок!2", x)
            #print("Ок!3")
            if (f2[x]) != (sas312[y]):
                y = 0
            if (f2[x]) == (sas312[y]):
                y = y + 1
            
            #print("Ок!4")
            x = x + 1
            #print("Ок!5")
            if y == (11):
                # Это ютуб!
                #print("Это ютуб!")
                Cycle01 = 10
                #TIN = True
                return True
                break #  !!!ВНИМАНИЕ!!!  ВЫХОД ИЗ ЦИКЛА!!!
            if "001" == (f2[x]):
                Cycle01 = 10
                #print("Это не ютуб!")
                #TIN = False
                return False
            elif x == (23):
                Cycle01 = 10
                #print("Это не ютуб!")
                #TIN = False
                return False
    #print(TIN)
    #return TIN
    print("Всё!")

def start_2(url):
    sas312 = ['y', 'o', 'u', 't', 'u', '.', 'b', 'e']
    f1 = (url)
    f2 = []
    f2.extend (f1)
    #print(f2)
    #if (f2[7) == "/":
    shit = False
    if shit == False:
        #print("/")
        f2.append ("001") #Конец текста "Замыкатель"
        Cycle01 = 0
        x = 0
        y = 0
        #print("Ок!1")
        while Cycle01 < 1:
            #print("Ок!2", x)
            #print("Ок!3")
            if (f2[x]) != (sas312[y]):
                y = 0
            if (f2[x]) == (sas312[y]):
                y = y + 1
            
            #print("Ок!4")
            x = x + 1
            #print("Ок!5")
            if y == (8):
                # Это ютуб!
                #print("Это ютуб!")
                Cycle01 = 7
                #TIN = True
                return True
                break #  !!!ВНИМАНИЕ!!!  ВЫХОД ИЗ ЦИКЛА!!!
            if "001" == (f2[x]):
                Cycle01 = 7
                #print("Это не ютуб!")
                #TIN = False
                return False
            elif x == (20):
                Cycle01 = 7
                #print("Это не ютуб!")
                #TIN = False
                return False
    #print(TIN)
    #return TIN
    print("Всё!")


def start_list(url):
    print("Это не плей лист")
    TIN = False
    #return TIN
    #return True
    return False


def start_IF(Question,guild_id,user_id):
    from time import strftime, localtime, sleep #Для (Time)
    print(Question)
    print(Question[0][0])
    a = True
    X = 0
    while a != 10:
        print(Question[1][X])
        print(Question[1][X])
        if user_id == Question[0][X] and guild_id == Question[1][X]:
        #if user_id == Question[X][0]:
            if Question[2][X] == "y":
                # Да это плейлист.
                print("Да это плейлист")
            elif Question[2][X] == "n":
                # Нет это не плейлист.
                print("Нет это не плейлист")
        
            else:
            #if "001" == Question[0][X]:
                # Ждать 10 сек.
                sleep(10)# Остановка на 1 сек.
                a = a + 1
                X = 0
        else:
            X = X + 1




        #Question[1,1]

def don(url,id,message, name):
    print(f"Качаем - {name}")
    fael = False
    '''
    #guild_name = message.author.guild.name
    for id_user in os.listdir():
        if guild_name == id_user:
            fael = True
    if fael == False:
        os.mkdir(guild_name)
'''

    #sasss = f"Music/{name}"
    sasss = name
    ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': sasss,
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'opus', #.opus
                #'output': '/home/romenskiy2012/',
                #'preferredquality': '192',
                'preferredquality': '192',
                
            }],
        }
    
    
    print("Скачивание аудио сейчас\n")
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])



def yyy(channel_id):
    ydl = youtube_dl.YoutubeDL({'outtmpl': '%(id)s%(ext)s'})
    #global video
    with ydl:
        result = ydl.extract_info(
            str(channel_id),
            download=False # We just want to extract the info
        )
        if 'entries' in result:
            # Can be a playlist or a list of videos
            video = result['entries'][0]
        else:
            # Just a video
            video = result


    
    #global GAMENAME, GAMENAME2
    GAMENAME = video['duration']#Игра
    print("Видео идёт - ",GAMENAME)
    return video
