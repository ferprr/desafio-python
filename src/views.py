from datetime import time
import random

from models import Song

def createAlbum(albuns, album, songs, song):
    album.setSong(song)
    albuns.add(album)
    songs.add(song)

def searchAlbum(albuns, request):
    for album in albuns:
        if album.title == request or album.band == request or album.release == request:
            for song in album.songs:
                print(f'{album.title} {album.band} {album.release}')
                print(f'{song.title} {song.duration} {song.isFavorite}')

def searchSong(albuns, songs, request):
    for album in albuns:
        if album.band == request:
            for song in songs:
                if song.title == request:
                    print(f'{song.title} {song.duration} {song.isFavorite}')

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
    playlist = set()

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
            #print(f"Iteration {i} duration {duration_time} and song {new_song.title}")
        
        playlist.add(new_song)

        if new_song.isFavorite:
            qt_fav_songs += 1 
        else:
            qt_usual_songs += 1
        
        # Playlist entre tempo limite - 2 minutos até tempo limite
        if duration_time <= limit_time and duration_time > (limit_time - 120):
            break
    
    
    print(f"favorites {qt_fav_songs} and usuals {qt_usual_songs} and length favorites {len(favorite_songs)} and usuals {len(usual_songs)}")
    print(f"Playlist total length {duration_time} seconds ~ {duration_time / 60} minutes")
    for song in playlist:
        print(song.title)