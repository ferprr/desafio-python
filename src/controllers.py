from datetime import datetime
import sys
import views
from models import Album, Song

albuns:list = []
songs:list = []

def main():

    option = int(input(
            "MENU: \n 1- Cadastrar Álbum \n 2- Pesquisar Álbum \n 3- Pesquisar Música \n 4- Gerar Playlist \n 5- Sair \n"))

    while option != 5:

        if option == 1:
            print("Type the album information you want create: ")
            createAlbum()

        elif option == 2:
            print("Type title, release or band to find an album: ")
            searchAlbum()

        elif option == 3:
            print("Type title or band to find a song: ")
            searchSong()

        elif option == 4:
            print("Generating playlist...")
            generatePlaylist()
            
        else:
            print("Opcao invalida. Escolha novamente.")

        option = int(input(
            "MENU: \n 1- Cadastrar Álbum \n 2- Pesquisar Álbum \n 3- Pesquisar Música \n 4- Gerar Playlist \n 5- Sair \n"))

    print("Closing...")
    sys.exit(0)


def createAlbum():
    global albuns 
    global songs

    title = input("Type a title to the album: ")
    release = input("Type a release to the album: ")
    band = input("Type a band to the album: ")
    print("Type the songs information you want add to the album: ")
    titleSong = input("Type a title to the song: ")
    duration = input("Type a duration to the song (specify time in MM:SS format): ")
    isFavorite = input("Type if this is a favorite song: ")
    song = Song(titleSong, duration, isFavorite)
    album = Album(title, release, band, song)
    
    albuns, songs = views.createAlbum(albuns, album, songs, song)


def searchAlbum():
    global albuns 
    global songs

    request = input("Type a information to find the album: ")
    album_returned = views.searchAlbum(albuns, request)
    if album_returned == None:
        print("Album not found. Make sure it already exists.")
    elif len(album_returned) > 1:
        for album in album_returned:
            print(f'\nAlbum {album.title}: \n')
            if len(album.songs) > 1:
                print(f'{album.title} {album.release} {album.band}')
                for song in album.songs:
                    print(f'{song.title} {song.duration.minute}:{song.duration.second} {song.isFavorite}')
            else: 
                print(f'{album.title} {album.release} {album.band}')
                song = album.songs[0]
                print(f'{song.title} {song.duration.minute}:{song.duration.second} {song.isFavorite}')
    else:
        album_returned = album_returned[0]
        if len(album_returned.songs) > 1:
            print(f'{album_returned.title} {album_returned.release} {album_returned.band}')
            for song in album_returned.songs:
                print(f'{song.title} {song.duration.minute}:{song.duration.second} {song.isFavorite}')
        else: 
            print(f'{album_returned.title} {album_returned.release} {album_returned.band}')
            song = album_returned.songs[0]
            print(f'{song.title} {song.duration.minute}:{song.duration.second} {song.isFavorite}')

def searchSong():
    global albuns 
    global songs

    song_band = input('''
        Do you want to search by band name or song name?
        1 - Band
        2 - Song
        ''')
    request = input("Type a information to find the song: ")
    song_returned = views.searchSong(albuns, songs, song_band, request)
    if song_returned == None:
        print("Song not found. Make sure it already exists. ")
    elif type(song_returned) is list:
        for song in songs:
            print(f'{song.title} {song.duration.minute}:{song.duration.second} {song.isFavorite}')
    else:
        print(f'{song_returned.title} {song_returned.duration.minute}:{song_returned.duration.second} {song_returned.isFavorite}')

def generatePlaylist():
    global albuns 
    global songs

    views.generatePlaylist(songs)

if __name__=="__main__":
        main()