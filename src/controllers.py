import sys
from turtle import title

import views

from models import Album, Song


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
        print("Type title, release or band to find a song: ")
        searchSong()
        main()

    elif option == '4':
        print("Generating playlist...")
        #generatePlaylist()
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
    album = Album(title, release, band)
    titleSong = input("Type a title to the song: ")
    duration = input("Type a duration to the song: ")
    isFavorite = input("Type if this is a favorite song: ")
    song = Song(titleSong, duration, isFavorite)
    views.createAlbum(album, song)

def searchAlbum():
    request = input("Type a information to find the album: ")
    views.searchAlbum(request)

def searchSong():
    request = input("Type a information to find the song: ")
    views.searchSong(request)

def generatePlaylist():
    generatePlaylist()

if __name__=="__main__":
        main()