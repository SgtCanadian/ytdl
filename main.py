from yt_dlp import YoutubeDL

url = 'https://www.youtube.com/shorts/vhd3u9RemT4'
ydl_opts = {'format': 'mp4'}
ydl_audio = {'format': 'mp3'}
#with YoutubeDL(ydl_opts) as ydl:
#    ydl.download(url)


print()
with YoutubeDL(ydl_audio) as ydl:
    ydl.download(url)