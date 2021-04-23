from datetime import time
from random import random

from models import Song

def createAlbum(albuns, album, songs, song):
    album.setSong(song)
    albuns.add(album)
    songs.add(song)

def searchAlbum(albuns, request):
    for album in albuns:
        if album.title == request or album.band == request:
            for song in album.songs:
                print(f'{album.title} {album.band} {album.release}')
                print(f'{song.title} {song.duration} {song.isFavorite}')

def searchSong(albuns, songs, request):
    for album in albuns:
        if album.band == request:
            for song in songs:
                if song.title == request:
                    print(f'{song.title} {song.duration} {song.isFavorite}')

def generatePlaylist(songs, playlist):
    duration_time = 0
    limit_time = 3600
    new_song:Song
    qt_fav_songs:int = 0
    qt_usual_songs:int = 0
    
    while duration_time < limit_time:

        if qt_fav_songs == qt_usual_songs:
            new_song = random.choice(tuple(songs))

        if duration_time + (new_song.duration.minute * 60 + new_song.duration.second)  > limit_time: 
            duration_time = limit_time
            continue # pula para a proxima iteracao do loop
        else:
            duration_time += (new_song.duration.minute * 60 + new_song.duration.second)
        
        playlist.add(new_song)

        if new_song.isFavorite == 0:
            qt_usual_songs += 1
        else:
            qt_fav_songs +=1 

    for song in playlist:
        print(song.title + " \n ")