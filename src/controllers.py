from datetime import datetime
import sys
import views
from models import Album, Song

albuns = set()
songs = set()

def main():
    option = input(
        "MENU: \n 1- Cadastrar Álbum \n 2- Pesquisar Álbum \n 3- Pesquisar Música \n 4- Gerar Playlist \n 5- Sair \n")

    if option == '1':
        print("Type the album information you want create: ")
        createAlbum()
        main()

    elif option == '2':
        print("Type title, release or band to find an album: ")
        searchAlbum()
        main()

    elif option == '3':
        print("Type title or band to find a song: ")
        searchSong()
        main()

    elif option == '4':
        print("Generating playlist...")
        generatePlaylist()
        main()

    elif option == '5':
        print("Closing...")
        sys.exit(0)

    else:
        print("Opcao invalida. Escolha novamente.")
        main()


def createAlbum():
    title = input("Type a title to the album: ")
    release = input("Type a release to the album: ")
    band = input("Type a band to the album: ")
    print("Type the songs information you want add to the album: ")
    titleSong = input("Type a title to the song: ")
    duration = input("Type a duration to the song (specify time in MM:SS format): ")
    isFavorite = input("Type if this is a favorite song: ")
    song = Song(titleSong, duration, isFavorite)
    album = Album(title, release, band, song)
    
    views.createAlbum(albuns, album, songs, song)

def searchAlbum():
    request = input("Type a information to find the album: ")
    album_returned = views.searchAlbum(albuns, request)
    album_songs = album_returned.getSongs()
    if type(album_songs) is set:
        for song in album_songs:
            print(f'{song.title} {song.duration.minute}:{song.duration.second} {song.isFavorite}')
    else: 
        print(f'{album_returned.title} {album_returned.release} {album_returned.band}')
        print(f'{album_songs.title} {album_songs.duration.minute}:{album_songs.duration.second} {album_songs.isFavorite}')

def searchSong():
    request = input("Type a information to find the song: ")
    song_returned = views.searchSong(albuns, songs, request)
    if type(song_returned) is set:
        for song in songs:
            print(f'{song.title} {song.duration.minute}:{song.duration.second} {song.isFavorite}')
    else:
        print(f'{song_returned.title} {song_returned.duration.minute}:{song_returned.duration.second} {song_returned.isFavorite}')

def generatePlaylist():
    views.generatePlaylist(songs)

if __name__=="__main__":
        main()