from turtle import title
import unittest

import views

from models import Album, Song

albuns = {Album(title="album1", release=2000, band="band1", song=Song(title="song1", duration="2:55", isFavorite=True)),
    Album(title="album2", release=2010, band="band2", song=Song(title="song2", duration="3:10", isFavorite=False)),
    Album(title="album2", release=2012, band="band1", song=Song(title="song3", duration="4:24", isFavorite=False)),
    Album(title="album3", release=2017, band="band2", song=Song(title="song4", duration="2:47", isFavorite=True)),
    Album(title="album4", release=2020, band="band2", song=Song(title="song4", duration="4:03", isFavorite=True))}

songs = {Song(title="song1", duration="2:55", isFavorite=True), 
    Song(title="song2", duration="3:10", isFavorite=False), 
    Song(title="song3", duration="4:24", isFavorite=False),
    Song(title="song4", duration="2:47", isFavorite=True),
    Song(title="song4", duration="4:03", isFavorite=True)}

class Tests(unittest.TestCase):

    def test_create_album(self):

        self.assertEqual(5, len(albuns))

        song = Song(title="song7", duration="03:37", isFavorite=True)
        album = Album(title="album5", release=2019, band="band3", song=song)

        views.createAlbum(albuns, album, songs, song)

        self.assertNotEqual(5, len(albuns))
        self.assertNotEqual(6, len(songs))
        self.assertEqual(6, len(albuns))
        self.assertEqual(7, len(songs))

    def test_search_album_by_title_not_found(self):

        album = views.searchAlbum(albuns, "album5")

        self.assertEqual(album, None)

    def test_search_album_by_title_found(self):

        album4 = Album(title="album4", release=2020, band="band2", song=Song(title="song4", duration="4:03", isFavorite=True))

        album = views.searchAlbum(albuns, "album4")

        self.assertNotEqual(album, album4)

    def test_search_album_by_band_found(self):

        albuns_test = {Album(title="album2", release=2010, band="band2", song=Song(title="song2", duration="3:10", isFavorite=False)), Album(title="album3", release=2017, band="band2", song=Song(title="song4", duration="2:47", isFavorite=True)), Album(title="album4", release=2020, band="band2", song=Song(title="song4", duration="4:03", isFavorite=True))}

        album = views.searchAlbum(albuns, "band2")

        self.assertEqual(album, albuns_test)

    def test_search_album_by_band_not_found(self):

        album = views.searchAlbum(albuns, "band3")

        self.assertEqual(album, None)

    def test_search_album_by_release_found(self):

        album4 = Album(title="album4", release=2020, band="band2", song=Song(title="song4", duration="4:03", isFavorite=True))

        album = views.searchAlbum(albuns, 2020)

        self.assertEqual(album, album4)

    def test_search_album_by_release_not_found(self):

        album = views.searchAlbum(albuns, 2017)

        self.assertEqual(album, None)

    def test_search_song_by_title_found(self):

        song4 = Song(title="song4", duration="4:03", isFavorite=True)

        song = views.searchSong(albuns, songs, "song4")

        self.assertEqual(song, song4)

    def test_search_song_by_title_not_found(self):

        song = views.searchSong(albuns, songs, "song4")

        self.assertEqual(song, None)

    def test_search_song_by_band_found(self):

        song4 = Song(title="song4", duration="4:03", isFavorite=True)

        song = views.searchSong(albuns, songs, "band2")

        self.assertEqual(song, song4)

    def test_search_song_by_band_not_found(self):

        song = views.searchSong(albuns, songs, "album5")

        self.assertEqual(song, None)


if __name__ == '__main__':
    unittest.main()