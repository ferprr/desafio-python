from datetime import datetime



class Song:


    def __init__(self, title:str, duration:datetime.time, isFavorite:bool):
        self.title:str = title
        self.duration:datetime.time = duration
        self.isFavorite:bool = isFavorite


class Album:


    def __init__(self, title:str, release:str, band:str):
        self.title:str = title
        self.release:str = release
        self.band:str = band

    def setSong(self, songs:list):
        self.songs:list.append(songs)


class Playlist:


    def __init__(self, name:str):
        self.title:str = name

    def setSong(self, songs:list):
        self.songs:list = songs
