import sys


def main():
    option = input(
        "MENU: \n 1- Cadastrar Álbum \n 2- Pesquisar Álbum \n 3- Pesquisar Música \n 4- Gerar Playlist \n 5- Sair")

    if option == '1':
        print("Type the album information you want create:")
        #createAlbum(request) obs.: title, release, band
        print("Type the music information you want to add to the album:")
        #albuns.songs.append(request) obs.: title, duration, isFavorite

    elif option == '2':
        print("Type title, release or band to find an album:")
        #albuns.get(request) obs.: title, release or band

    elif option == '3':
        print("Type title, release or band to find a song:")
        #songs.get(request) obs.: title or band

    elif option == '4':
        print("Generating playlist...")
        #gerarPlaylist obs.: half favorite songs for Billie, half random

    elif option == '5':
        print("Closing...")
        sys.exit(0)

    else:
        print("Opcao invalida. Escolha novamente.")


