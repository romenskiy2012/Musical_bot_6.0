import youtube_dl
print("youtube подключен!")  


def start(url):
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

def don(url):
    sasss = "123.opus"
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