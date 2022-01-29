import yt_dlp
import os

DEBUG = True


url = os.environ["DOWNLOADER_URL"]
name = os.environ["DOWNLOADER_NAME"]

#def don(url,id, name):
if DEBUG:print(f"Качаем - {name}")


ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': name,
        'quiet': True,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'opus', #.opus
            #'output': '/home/romenskiy2012/',
            #'preferredquality': '192',
            'preferredquality': '192',

        }],
    }


if DEBUG:print("Скачивание аудио сейчас\n")
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])
