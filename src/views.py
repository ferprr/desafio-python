from models import Album

albuns = []
playlist = []

def createAlbum(selfAlbum, selfSong):
    albuns.append(selfAlbum)
    registerSongOnAlbum(selfSong)

def registerSongOnAlbum(selfSong):
    Album.songs.append(selfSong)

def searchAlbum(request):
    filter_object = filter(lambda a: request in a, albuns)
    print(albuns(filter_object))

def searchSong(request):
    filter_object = filter(lambda a: request in a, Album.songs)
    print(Album.songs(filter_object))

#def generatePlaylist():
