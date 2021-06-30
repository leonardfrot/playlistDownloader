import pytube
from pytube import YouTube
from pytube import Playlist
import os
import moviepy.editor as mp
import re
from tqdm import tqdm

playlists = []
quit = False
types = ["metal", "rap", "electro", "divers"]

while quit == False:
    request = input("mettez les playlists, q pour télécharger")
    if request == "q":
        break

    typeNumber = input(
        "choisissez le genre du playlist \n 1 pour metal \n 2 pour rap \n 3 pour electro \n 4 pour divers")

    # controle de nombre
    try:
        val = int(typeNumber)
    except:
        print("le nombre est faux, mettez un bon nombre")

    if int(typeNumber) > 4 or int(typeNumber) < 1:
        print("le nombre est faux, mettez un bon nombre")

    type = types[int(typeNumber) - 1]

    objet = {"lien": request, "type": type}
    playlists.append(objet)

print(playlists)

for playlist in playlists:
    url = playlist.get("lien")
    filepath = 'C:/youtube/' + playlist.get("type")

    urls = Playlist(url)

    for url in urls:
        for i in tqdm(range(1), desc="Loading " + url):
            YouTube(url).streams.first().download(filepath)

    for file in os.listdir(filepath):
        if re.search('mp4', file):
            mp4_path = os.path.join(filepath, file)
            mp3_path = os.path.join(filepath, os.path.splitext(file)[0] + '.mp3')
            new_file = mp.AudioFileClip(mp4_path)
            new_file.write_audiofile(mp3_path)
            os.remove(mp4_path)





