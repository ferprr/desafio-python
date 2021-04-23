from models import Album

#limit = 60:00

def createAlbum(albuns, selfAlbum, songs, selfSong):
    # if selfAlbum in albuns:
    #     selfAlbum.setSong(selfSong)
    #     songs.append(selfSong)
    # else:
    selfAlbum.setSong(selfSong)
    albuns.add(selfAlbum)
    songs.add(selfSong)

def searchAlbum(albuns, request, songs):
    for i in range(len(albuns)):
        if albuns[i].title == request or albuns[i].band == request:
            for j in range(len(albuns[i].songs)):
                print(f'{albuns[i].title} {albuns[i].band} {albuns[i].release}')
                print(f'{songs[j].title} {songs[j].duration} {songs[j].isFavorite}')

def searchSong(albuns, songs, request):
    for i in range(len(albuns)):
        if albuns[i].band == request:
            for j in range(len(songs)):
                if songs[j].title == request:
                    print(f'{songs[j].title} {songs[j].duration} {songs[j].isFavorite}')

def generatePlaylist(songs):
    print(songs.sort())