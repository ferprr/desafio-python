from django.db.models.fields import BooleanField, CharField, DurationField


class Music:
    title = CharField(max_length=20, blank=True, null=True)
    duration = DurationField(blank=True, null=True)
    isFavorite = BooleanField(blank=True, null=True)


class Album:
    title = CharField(max_length=20, blank=True, null=True)
    release = CharField(max_length=20, blank=True, null=True)
    band = CharField(max_length=20, blank=True, null=True)
    musics = []


class Playlist:
    name = CharField(max_length=20, blank=True, null=True)
    musics = []
