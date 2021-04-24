from datetime import time
import random

from models import Song

def createAlbum(albuns, album, songs, song):

    for album_x in albuns:
        if album_x.title == album.title:
            album_x.setSong(song)
            songs.append(song)
            return albuns, songs
    
    albuns.append(album)
    songs.append(song)

    return albuns, songs

def searchAlbum(albuns, request):
    found_albums = []

    for album in albuns:
        if album.title == request or album.band == request or album.release == request:
            found_albums.append(album)

    return found_albums

def searchSong(albuns, songs, song_band, request):
    if song_band == '1':
        for album in albuns:
            if album.band == request:
                return album.songs
    else:
        for song in songs:
            if song.title == request:
                return song

def get_song(songs):
    new_song_idx = random.choice(range(len(songs)))
    new_song = songs[new_song_idx]

    # deleta a musica escolhida da lista para evitar repeticao
    songs.pop(new_song_idx)
    
    return (new_song, songs)

def generatePlaylist(songs):
    duration_time = 0
    limit_time = 3600
    new_song:Song
    qt_fav_songs:int = 0
    qt_usual_songs:int = 0
    playlist = []

    favorite_songs = [song for song in songs if song.isFavorite]
    usual_songs = [song for song in songs if not song.isFavorite]
    
    for i in range(len(songs)):
        
        if qt_fav_songs == qt_usual_songs:
            if favorite_songs:
                new_song, favorite_songs = get_song(favorite_songs)
            else:
                new_song, usual_songs = get_song(usual_songs)
        elif qt_fav_songs < qt_usual_songs:
            if usual_songs:
                new_song, usual_songs = get_song(usual_songs)
            else:
                new_song, favorite_songs = get_song(favorite_songs)
        else:
            if favorite_songs:
                new_song, favorite_songs = get_song(favorite_songs)
            else:
                new_song, usual_songs = get_song(usual_songs)

        if duration_time + (new_song.duration.minute * 60 + new_song.duration.second)  > limit_time: 
            continue # pula para a proxima iteracao do loop
        else:
            duration_time += (new_song.duration.minute * 60 + new_song.duration.second)
        
        playlist.append(new_song)

        if new_song.isFavorite:
            qt_fav_songs += 1 
        else:
            qt_usual_songs += 1
        
        # Playlist entre tempo limite - 2 minutos até tempo limite
        if duration_time <= limit_time and duration_time > (limit_time - 120):
            break
    
    print(f"Playlist total length {duration_time} seconds ~ {duration_time / 60} minutes")
    for song in playlist:
        print(song.title)