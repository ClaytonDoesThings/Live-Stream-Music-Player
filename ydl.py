from __future__ import unicode_literals
import youtube_dl

def ydl (args):
    ydl_opts = {
        'outtmpl': args['file_name']+'.%(ext)s',
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': args['codec'],
            'preferredquality': '192',
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
       ydl.download([args['url']])