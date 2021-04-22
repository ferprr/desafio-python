from django.db.models.fields import BooleanField, CharField, DurationField


class Song:
    title = CharField(max_length=20, blank=True, null=True)
    duration = DurationField(blank=True, null=True)
    isFavorite = BooleanField(blank=True, null=True)
    
    def __init__(self, title, duration, isFavorite):
        self.title = title
        self.duration = duration
        self.isFavorite = isFavorite


class Album:
    title = CharField(max_length=20, blank=True, null=True)
    release = CharField(max_length=20, blank=True, null=True)
    band = CharField(max_length=20, blank=True, null=True)
    songs = []

    def __init__(self, title, release, band):
        self.title = title
        self.release = release
        self.band = band


class Playlist:
    name = CharField(max_length=20, blank=True, null=True)
    songs = []

    def __init__(self, name):
        self.title = name
