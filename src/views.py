from models import Album

#limit = 01:00:00

albuns = []
playlist = []

def createAlbum(selfAlbum, selfSong):
    albuns.append(selfAlbum)
    registerSongOnAlbum(selfSong, selfAlbum)

def registerSongOnAlbum(selfSong, selfAlbum):
    Album.insert(selfAlbum, selfSong)
    #Album.songs.append(selfSong)

def searchAlbum(request):
    filter_object = filter(lambda a: request in a, albuns)
    print(albuns(filter_object))

def searchSong(request):
    filter_object = filter(lambda a: request in a, albuns.songs)
    print(albuns.songs(filter_object))

#def generatePlaylist():
