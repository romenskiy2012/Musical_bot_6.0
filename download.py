import youtube_dl
import youtube
import question
import bd_module
import os
import os.path

import water_handler
print("youtube подключен!")   

def search(name):
    list = os.listdir("Music/")
    for list_2 in list:
        if list_2 == name:
            print("Такой фаел есть!")
            return False
    

def youtube_d(url,message):
    
    i_2 = question.q_download()# Занять место в очереди

    id = water_handler.youtube(url)
    print(f"id - {id}")
    id_name2 = f"{id}.opus"
    id_name = os.listdir("Music/")
    a = 0
    for sas in id_name:
        if sas == id_name2:
            a = a + 1
            
    if (a == 1):
        print(f"id2 - {id}")
        id, name_2, volume, time, views, estimation, date = bd_module.search_ID(id)# Получаем инфу из базы (По ключу из сылки имя)
        name = f"Music/{id}.opus"
        #bd_module.local(message, id)
        
    elif a == 0:
        video = youtube.yyy(url)
        ###### Фиксим имя файла
        name = video['title']
        name = name.replace(' ', '_')
        name = name.replace("'", '_')
        name = name.replace('"', '_')
        name = f"Music/{id}.opus"
        ######
        #url = f"http://youtu.be/{id}"
        youtube.don(url,id,message,name) # Скачивание
        volume = os.path.getsize(name)
        bd_module.search_ID_rid(id, video, volume)
        
    else:
        print("Выевлено сходство файлов!")
        
        

    
    
    
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

    question.q_download_question(i_2)# Наше место в очереди ?
    bd_module.adding_to_the_queue(message, id) # Добавить в бузу
    question.q_download_del(i_2)# Освободить место в очереди
    return id



