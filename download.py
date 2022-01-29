import youtube_dl
import youtube
import question
import bd_module
import os
import os.path

import asyncio
import sys


DEBUG = False

import water_handler
put = os.path.dirname(os.path.realpath(__file__)) + "/"#Путь- (part-1)
#print("youtube подключен!")

def search(name):
    list = os.listdir("Music/")
    for list_2 in list:
        if list_2 == name:
            if DEBUG:print("Такой фаел есть!")
            return False
    

async def youtube_d(url,message):
    
    i_2 = question.q_download()# Занять место в очереди

    id = water_handler.youtube(url)
    if DEBUG:print(f"id - {id}")
    id_name2 = f"{id}.opus"
    id_name = os.listdir(f"{put}Music/")
    a = 0
    for sas in id_name:
        if sas == id_name2:
            a = a + 1
            
    if (a == 1):
        if DEBUG:print(f"id2 - {id}")
        name_2, volume, time, views, estimation, date, uploaded, upload_date, thumbnail = bd_module.search_ID(id)# Получаем инфу из базы (По ключу из сылки имя) # TypeError: cannot unpack non-iterable bool object
        name = f"{put}Music/{id}.opus"
        #bd_module.local(message, id)
        
    elif a == 0:
        video = youtube.yyy(url)
        ###### Фиксим имя файла
        if video['is_live']:
            return False, False
        name = video['title']
        name = name.replace(' ', '_')
        name = name.replace("'", '_')
        name = name.replace('"', '_')
        name = f"{put}Music/{id}.opus"
        ######
        #url = f"http://youtu.be/{id}"
        #youtube.don(url,id,name) # Скачивание

        env = os.environ.copy()
        env["DOWNLOADER_URL"] = url
        env["DOWNLOADER_NAME"] = name
        proc = await asyncio.create_subprocess_exec(sys.executable, "SAS.py", env=env)
        await proc.wait()
        if proc.returncode == 0:
            print("ok")
        else:
            print("error")

        volume = os.path.getsize(name)
        bd_module.search_ID_rid(id, video, volume, message.author.id)
        name_2 = video['title']
        
    else:
        if DEBUG:print("Выевлено сходство файлов!")
        
        

    
    
    
    '''
    

    # Открываем второй поток для инфы (video = youtube.yyy(url) # Получения информации)

    # Если трека нет качаем его

    # Синфронизируем потоки.
    
    video = youtube.yyy(url)
    ###### Фиксим имя файла
    name = video['title']
    name = name.replace(' ', '_')
    name = name.replace("'", '_')
    name = name.replace('"', '_')
    name = f"{name}.opus"
    ######

    if search(name):
        youtube.don(url,id,message) # Скачивание
    '''

    #question.q_download_question(i_2)# Наше место в очереди ?
    #bd_module.adding_to_the_queue(message, id, name_2, message.author.id) # Добавить в бузу
    #question.q_download_del(i_2)# Освободить место в очереди
    return id, name_2



