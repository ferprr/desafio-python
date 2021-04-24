from datetime import datetime

class Song:

    def __init__(self, title:str, duration:datetime, isFavorite:bool):
        self.title:str = title
        self.duration:datetime = datetime.strptime(duration, "%M:%S")
        self.isFavorite:bool = isFavorite

    # def __eq__(self, other):
    #     return self.title == other.title and \
    #            self.duration == other.duration and \
    #            self.isFavorite == other.isFavorite

    def getSong(self):
        return self.song

class Album:

    def __init__(self, title:str, release:int, band:str, song:Song):
        self.title:str = title
        self.release:int = release
        self.band:str = band
        self.songs:set = set()
        self.songs.add(song)

    def setSong(self, song:Song):
        self.songs.add(song)

    def getSong(self):
        return self.songs


    # def __eq__(self, other):
    #     return self.title == other.title and \
    #            self.release == other.release and \
    #            self.band == other.band


class Playlist:

    def __init__(self, name:str, song:Song):
        self.title:str = name
        self.songs:set = set()
        self.songs.add(song)

    def setSong(self, song:Song):
        self.songs.add(song)
