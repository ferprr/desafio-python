from datetime import datetime
import sys
import views
from models import Album, Song

albuns:list = []
songs:list = []

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
    
    new_albuns, new_songs = views.createAlbum(albuns, album, songs, song)
    for i in range(len(new_albuns)):
        albuns[i] = new_albuns[i]
    for i in range(len(new_songs)):
        songs[i] = new_songs[i]

def searchAlbum():
    request = input("Type a information to find the album: ")
    album_returned = views.searchAlbum(albuns, request)
    if album_returned == None:
        print("Album not found. Make sure it already exists.")
    elif len(album_returned.songs) > 1:
        print(f'{album_returned.title} {album_returned.release} {album_returned.band}')
        for song in album_returned.songs:
            print(f'{song.title} {song.duration.minute}:{song.duration.second} {song.isFavorite}')
    else: 
        print(f'{album_returned.title} {album_returned.release} {album_returned.band}')
        song = album_returned.songs[0]
        print(f'{song.title} {song.duration.minute}:{song.duration.second} {song.isFavorite}')

def searchSong():
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
    views.generatePlaylist(songs)

if __name__=="__main__":
        main()