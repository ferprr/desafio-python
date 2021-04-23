from datetime import datetime

class Song:

    def __init__(self, title:str, duration:datetime, isFavorite:bool):
        self.title:str = title
        self.duration:datetime = datetime.strptime(duration, "%M:%S")
        self.isFavorite:bool = isFavorite


class Album:

    def __init__(self, title:str, release:int, band:str, song:Song):
        self.title:str = title
        self.release:int = release
        self.band:str = band
        self.songs:set = set()
        self.songs.add(song)

    def setSong(self, song:Song):
        self.songs.add(song)


class Playlist:

    def __init__(self, name:str, song:Song):
        self.title:str = name
        self.songs:set = set()
        self.songs.add(song)

    def setSong(self, song:Song):
        self.songs.add(song)
