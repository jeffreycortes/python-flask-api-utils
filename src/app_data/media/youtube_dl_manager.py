from __future__ import unicode_literals
import youtube_dl
import os
import sys

class MyLogger:
    def debug(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)

class YoutubeDLManager:
    media = None
    def __init__(self):
        self.__path_ffmpeg = 'src/app_data/media/ffmpeg/bin/'
        self.__path_download = 'src/app_infrastructure/persistence/media/downloads/'

        try:
            self.ydl_opts = {
                'format': 'bestaudio/best',
                'logger': MyLogger(),
                'download_archive': self.__path_download + 'downloads_log.txt',
                'ffmpeg_location': self.__path_ffmpeg,
                'progress_hooks': [self.progress_suscribe],
                'outtmpl': self.__path_download + '%(artist)s - %(title)s.%(ext)s',
                'postprocessors': [
                    {
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192'
                    }
                ],
                'verbose': 'true'
                }
            self.media = youtube_dl.YoutubeDL(self.ydl_opts)
        except:
            print('Error: The instance media object is not posible')

    def downloadBestAudio(self, url):
        print('downloadBestAudio', self.media)
        if self.media == None:
            return 'Media instance is None'

        with self.media as ydl:
            try:
                ydl.download([url])
            except:
                return 'Falló la extracción del audio'
        return 'File download succesfull ... ;)'

    def progress_suscribe(self, d):
        if d['status'] == 'finished':
            print('Done downloading, now converting ...')

    def version(self):
        return youtube_dl.version
