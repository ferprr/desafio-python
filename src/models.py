from datetime import datetime

class Song:

    def __init__(self, title:str, duration:datetime, isFavorite:bool):
        self.title:str = title
        self.duration:datetime = datetime.strptime(duration, "%M:%S")
        self.isFavorite:bool = isFavorite

    def getSong(self):
        return self.song

class Album:

    def __init__(self, title:str, release:int, band:str, song:Song):
        self.title:str = title
        self.release:int = release
        self.band:str = band
        self.songs:list = []
        self.songs.append(song)

    def setSong(self, song:Song):
        self.songs.append(song)

    def getSong(self):
        return self.songs

class Playlist:

    def __init__(self, name:str, song:Song):
        self.title:str = name
        self.songs:list = []
        self.songs.append(song)

    def setSong(self, song:Song):
        self.songs.append(song)
