from models import Album

#limit = 00:01:00

albuns = []
playlist = []
songs = []

def createAlbum(selfAlbum, selfSong):
    albuns.append(selfAlbum)
    registerSongOnAlbum(selfSong, selfAlbum)

def registerSongOnAlbum(selfSong, selfAlbum):
    Album.setSong(selfAlbum, selfSong)
    songs.append(selfSong)
    #Album.songs.append(selfSong)

def searchAlbum(request):
    for i in range(len(albuns)):
        if albuns[i] == request:
            print(albuns[i])

def searchSong(request):
    for i in range(len(songs)):
        if songs[i] == request:
            print(songs[i])

def generatePlaylist():
    print(songs.sort())