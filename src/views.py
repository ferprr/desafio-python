from datetime import time
from random import random

def createAlbum(albuns, album, songs, favorite_songs, song):
    album.setSong(song)
    albuns.add(album)
    if song.isFavorite:
        favorite_songs.add(song)
    else:
        songs.add(song)

def searchAlbum(albuns, request, songs):
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

def generatePlaylist(favorite_songs, songs, playlist):
    duration_time:time = time()
    limit_time = time(1, 0, 0)
    while duration_time < limit_time:
        for i in range(len(songs)):
            if i % 2 == 0:
                new_song = random.choice(favorite_songs)
                playlist.add(new_song)
                duration_time= duration_time + new_song.duration
            else:
                new_song = random.choice(songs)
                playlist.add(new_song)

    for song in playlist:
        print(song.title + " \n ")