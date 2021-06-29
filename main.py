from pytube import YouTube
from pytube import Playlist
import os
import moviepy.editor as mp
import re
from tqdm import tqdm

filepath = 'C:/youtube'

playlist = Playlist("https://www.youtube.com/playlist?list=PLpJy8H-uB3U1SpHNzDlBJWrt7Vgr9XgGx")

for url in playlist:
    for i in tqdm (range (1), desc="Loading " + url):
        YouTube(url).streams.first().download(filepath)

for file in os.listdir(filepath):
  if re.search('mp4', file):
    mp4_path = os.path.join(filepath,file)
    mp3_path = os.path.join(filepath,os.path.splitext(file)[0]+'.mp3')
    new_file = mp.AudioFileClip(mp4_path)
    new_file.write_audiofile(mp3_path)
    os.remove(mp4_path)


