import redis
import time

r = redis.StrictRedis(
    host='127.0.0.1',
    port=6379,
    password='',
    charset="utf-8",
    decode_responses=True
)

from datetime import timedelta
#r.setex('index',timedelta(minutes=1), value='1')

print(f"index: {r.get('index')}")





"""
import asyncio

async def SAS(A):
    while True:
        await asyncio.sleep(1)
        print(A)

async def SUS():
    task = asyncio.create_task(SAS("SAS"))
    print("SSSSSSSSSSSs")
    await asyncio.sleep(5)
    task.cancel()

asyncio.run(SUS())

"""




'''
ioloop = asyncio.get_event_loop()
wait_tasks = asyncio.wait(ioloop.create_task(SAS))
asyncio.sleep(10)
ioloop.close(SAS)
'''
'''
import youtube_dl

#url = "https://www.youtube.com/watch?v=6a08kXRkz-0&list=PLgb2J1R5MXUioTfGZFFvqru3gsVCWQlF7&index=1"
#url = "https://www.youtube.com/watch?v=hkZBskbkev8&list=PLgb2J1R5MXUioTfGZFFvqru3gsVCWQlF7&index=9"
#url = "https://www.youtube.com/watch?v=HDxLIBDU_ps"

ESC = b'\x1B' # Начинает ESC-последовательность
LF = b'\x0A' # \n Перевод на следующую строку
CR = b'\x0D' # \r Перевод в начало строки
CSI = b'[' # Ввод управляющей последовательности
EL = b'K' # Очистить строку. 2 - всю строку

import time
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
    print('progress: '+ '|'*i + ' '*(10-i) , i*10, '%', end='')
    # а потом обновляем прогресс-бар
    # end='' - значит остаемся в строке
    sys.stdout.flush()
    # для отрисовки недопечатанной строки
    i+=1

for text in ['один','два','три','ЧЕТЫРЕ','пять','шесть']:
    nprint(text)
    time.sleep(0.5)

print("\nВСЁ")

'''

'''
url = "https://www.youtube.com/watch?v=HDxLIBDU_ps&list=PLgb2J1R5MXUifC8JVqELYDGtP-0M31zBL&index=1"


ydl = youtube_dl.YoutubeDL({"start":4, "end":8})
video = ""



with ydl:
    result = ydl.extract_info \
    (url,
    download=False) #We just want to extract the info


    if 'entries' in result:
        # Can be a playlist or a list of videos
        video = result['entries']


        #loops entries to grab each video_url
        for i, item in enumerate(video):
            video = result['entries'][i]
            print(video['webpage_url'])

'''




"""

ydl = youtube_dl.YoutubeDL({'outtmpl': '%(id)s%(ext)s', 'playlist_index': True})
#global video
with ydl:
    result = ydl.extract_info(str(url), download=False # We just want to extract the info
    )
    if 'entries' in result:
        # Can be a playlist or a list of videos
        video = result['entries'][0]
    else:
        # Just a video
        video = result

print(int(result["width"]), int(result["height"]), float(result["fps"]))

"""

"""
ydl_opts = {
    'playlist_index': True,
    'ignoreerrors': True,
    'quiet': True
}



ydl = youtube_dl.YoutubeDL(ydl_opts)

playlist_dict = ydl.extract_info(url, download=False)

print(playlist_dict)
print(len(playlist_dict['entries']))
"""

'''
for video in playlist_dict['entries']:

    print()

    if not video:
        print('ERROR: Unable to get info. Continuing...')
        continue

    for prop in ['thumbnail', 'id', 'title', 'duration']:
        print(prop, '--', video.get(prop))
'''
