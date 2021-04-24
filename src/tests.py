from turtle import title
import unittest

import views

from models import Album, Song

albuns = [Album(title="album1", release=2000, band="band1", song=Song(title="song1", duration="2:55", isFavorite=True)),
    Album(title="album2", release=2010, band="band2", song=Song(title="song2", duration="3:10", isFavorite=False)),
    Album(title="album3", release=2017, band="band2", song=Song(title="song4", duration="2:47", isFavorite=True)),
    Album(title="album4", release=2020, band="band2", song=Song(title="song5", duration="4:03", isFavorite=True)),
    Album(title="album5", release=2012, band="band1", song=Song(title="song3", duration="4:24", isFavorite=False))]

songs = [Song(title="song1", duration="2:55", isFavorite=True), 
    Song(title="song2", duration="3:10", isFavorite=False), 
    Song(title="song3", duration="4:24", isFavorite=False),
    Song(title="song4", duration="2:47", isFavorite=True),
    Song(title="song5", duration="4:03", isFavorite=True)]

class Tests(unittest.TestCase):

    def setUp(self):
        self = unittest.TestCase()

    def test_create_new_album(self):

        print(len(songs))
        self.assertEqual(5, len(albuns))
        self.assertEqual(5, len(songs))

        song = Song(title="song7", duration="03:37", isFavorite=True)
        album = Album(title="album6", release=2016, band="band3", song=song)

        new_albuns, new_songs = views.createAlbum(albuns, album, songs, song)

        self.assertEqual(6, len(new_albuns))
        self.assertEqual(6, len(new_songs))

    def test_create_album_when_already_exists(self):

        print(len(songs))
        self.assertEqual(5, len(albuns))
        self.assertEqual(5, len(songs))

        song = Song(title="song7", duration="03:37", isFavorite=True)
        album = Album(title="album5", release=2012, band="band1", song=song)

        new_albuns, new_songs = views.createAlbum(albuns, album, songs, song)

        self.assertEqual(5, len(new_albuns))
        self.assertEqual(6, len(new_songs))

    def test_search_album_by_title_not_found(self):

        album = views.searchAlbum(albuns, "album6")

        self.assertEqual(album, None)

    # def test_search_album_by_title_found(self):

    #     album4 = Album(title="album4", release=2020, band="band2", song=Song(title="song5", duration="4:03", isFavorite=True))

    #     album = views.searchAlbum(albuns, "album4")

    #     self.assertEqual(album, album4)

    # def test_search_album_by_band_found(self):

    #     albuns_test = {Album(title="album2", release=2010, band="band2", song=Song(title="song2", duration="3:10", isFavorite=False)), Album(title="album3", release=2017, band="band2", song=Song(title="song4", duration="2:47", isFavorite=True)), Album(title="album4", release=2020, band="band2", song=Song(title="song5", duration="4:03", isFavorite=True))}

    #     album = views.searchAlbum(albuns, "band2")

    #     self.assertEqual(album, albuns_test)

    # def test_search_album_by_band_not_found(self):

    #     album = views.searchAlbum(albuns, "band3")

    #     self.assertEqual(album, None)

    # def test_search_album_by_release_found(self):

    #     album4 = Album(title="album4", release=2020, band="band2", song=Song(title="song4", duration="4:03", isFavorite=True))

    #     album = views.searchAlbum(albuns, 2020)

    #     self.assertEqual(album, album4)

    # def test_search_album_by_release_not_found(self):

    #     album = views.searchAlbum(albuns, 2017)

    #     self.assertEqual(album, None)

    # def test_search_song_by_title_found(self):

    #     song4 = Song(title="song4", duration="2:47", isFavorite=True)

    #     song = views.searchSong(albuns, songs, "song4")
    #     print(f'{song.title} {song.duration.minute}:{song.duration.second} {song.isFavorite}')

    #     self.assertEqual(song, song4)

    # def test_search_song_by_title_not_found(self):

    #     song = views.searchSong(albuns, songs, "song6")

    #     self.assertEqual(song, None)

    # def test_search_song_by_band_title_found(self):

    #     song4 = {Song(title="song2", duration="3:10", isFavorite=False),
    #     Song(title="song4", duration="2:47", isFavorite=True),
    #     Song(title="song5", duration="4:03", isFavorite=True)}

    #     song = views.searchSong(albuns, songs, '1', "band2")
    #     # for sing in song:
    #     #     print(f'{sing.title} {sing.duration.minute}:{sing.duration.second} {sing.isFavorite}')

    #     self.assertEqual(song, song4)

    # def test_search_song_by_band_title_not_found(self):

    #     song = views.searchSong(albuns, songs, "album5")

    #     self.assertEqual(song, None)

    # def test_search_song_by_song_title_found(self):

    #     song = views.searchSong(albuns, songs, "album5")

    #     self.assertEqual(song, None)

    # def test_search_song_by_song_title_not_found(self):

    #     song = views.searchSong(albuns, songs, "album5")

    #     self.assertEqual(song, None)


if __name__ == '__main__':
    unittest.main()