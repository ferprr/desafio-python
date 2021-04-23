from models import Album

#limit = 00:01:00

def createAlbum(albuns, selfAlbum, songs, selfSong):
    albuns.append(selfAlbum)
    registerSongOnAlbum(songs,selfSong, selfAlbum)

def registerSongOnAlbum(songs, selfSong, selfAlbum):
    Album.setSong(selfAlbum, selfSong)
    songs.append(selfSong)

def searchAlbum(albuns, request):
    for i in range(len(albuns)):
        if albuns[i].title == request or albuns[i].band == request:
            print(f'{albuns[i].title} {albuns[i].band}')

def searchSong(songs, request):
    for i in range(len(songs)):
        if songs[i].title == request:
            print(f'{songs[i].title} {songs[i].duration}')

def generatePlaylist(songs):
    print(songs.sort())