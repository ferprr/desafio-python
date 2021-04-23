from models import Album

#limit = 60:00

def createAlbum(albuns, selfAlbum, songs, selfSong):
    if selfAlbum in albuns:
        selfAlbum.setSong(selfSong)
        songs.append(selfSong)
    else:
        albuns.append(selfAlbum)
        songs.append(selfSong)

def searchAlbum(albuns, request, songs):
    for i in range(len(albuns)):
        for j in range(len(albuns[i].songs)):
            if albuns[i].title == request or albuns[i].band == request:
                print(f'{albuns[i].title} {albuns[i].band} {albuns[i].release}')
                print(f'{songs[j].title} {songs[j].duration} {songs[j].isFavorite}')

def searchSong(albuns, songs, request):
    for i in range(len(albuns)):
        for j in range(len(songs)):
            if songs[j].title == request or albuns[i].band == request:
                print(f'{songs[j].title} {songs[j].duration} {songs[j].isFavorite}')

def generatePlaylist(songs):
    print(songs.sort())