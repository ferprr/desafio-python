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
    for album in albuns:
        if album.title == request or album.band == request:
            for song in album.songs:
                print(f'{album.title} {album.band} {album.release}')
                print(f'{song.title} {song.duration} {song.isFavorite}')

def searchSong(albuns, songs, request):
    for album in albuns:
        if album.band == request:
            for song in songs:
                if song.title == request:
                    print(f'{song.title} {song.duration} {song.isFavorite}')

# def generatePlaylist(songs):
#     print(sorted(songs))