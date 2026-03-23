import unittest
from PartA import *

class TestPartA(unittest.TestCase):

    def test_artist_is_instance_artist(self):
        a1 = Artist("Taylor Swift", "13-12-1989", "USA")
        self.assertIsInstance(a1, Artist)

    def test_song_is_instance_of_song(self):
        s1 = Song("Love Story", "Taylor Swift", 2008)
        self.assertIsInstance(s1, Song)

    def test_album_is_instance_of_album(self):
        al1 = Album("Fearless", "Taylor Swift", 2008)
        self.assertIsInstance(al1, Album)

    def test_playlist_is_instance_of_playlist(self):
        p1 = Playlist("My Playlist")
        self.assertIsInstance(p1, Playlist)

    # not instance
    def test_artist_is_not_instance_artist(self):
        a1 = Artist("Taylor Swift", "13-12-1989", "USA")
        self.assertNotIsInstance(a1, Song)

    def test_song_is_not_instance_of_song(self):
        s1 = Song("Love Story", "Taylor Swift", 2008)
        self.assertNotIsInstance(s1, Artist)

    def test_album_is_not_instance_of_album(self):
        al1 = Album("Fearless", "Taylor Swift", 2008)
        self.assertNotIsInstance(al1, Playlist)

    def test_playlist_is_not_instance_of_playlist(self):
        p1 = Playlist("My Playlist")
        self.assertNotIsInstance(p1, Album)

    # check 2 objects are identical
    def test_identical(self):
        s1 = Song("Love Story", "Taylor Swift", 2008)
        s2 = s1
        self.assertIs(s1, s2)

    # check if 2 objects are not identical
    def test_notidentical(self):
        s1 = Song("Love Story", "Taylor Swift", 2008)
        s2 = Song("Fearless", "Taylor Swift", 2008)
        self.assertIsNot(s1, s2)

    # test methods add_song and add_album
    def test_addsong_artist(self):
        artist = Artist("Taylor Swift", "13-12-1989", "USA")
        song = Song("Love Story", "Taylor Swift", 2008)
        artist.add_song(song)
        self.assertIn(song, artist.songlist)
        self.assertEqual(len(artist.songlist), 1)

    def test_addalbum_artist(self):
        artist = Artist("Taylor Swift", "13-12-1989", "USA")
        album = Album("Fearless", "Taylor Swift", 2008)
        artist.add_album(album)
        self.assertIn(album, artist.albumlist)
        self.assertEqual(len(artist.albumlist), 1)

    def test_addsong_album(self):
        album = Album("Fearless", "Taylor Swift", 2008)
        album.add_song("Love Story", 2008)
        self.assertEqual(len(album.songs), 1)
        self.assertEqual(album.songs[0].songtitle, "Love Story")
        self.assertEqual(album.songs[0].artistname, "Taylor Swift")
        self.assertEqual(album.songs[0].year, 2008)

    def test_addsong_playlist(self):
        playlist = Playlist("Taylor Playlist")
        song = Song("Love Story", "Taylor Swift", 2008)
        playlist.add_song(song)
        self.assertIn(song, playlist.songs)
        self.assertEqual(len(playlist.songs), 1)

    # test for sort playlist and shuffle playlist
    def test_sort_playlist_asc(self):
        playlist = Playlist("Taylor Playlist")
        s1 = Song("Love Story", "Taylor Swift", 2008)
        s2 = Song("Change", "Taylor Swift", 2008)
        s3 = Song("Fifteen", "Taylor Swift", 2008)

        playlist.add_song(s1)
        playlist.add_song(s2)
        playlist.add_song(s3)

        playlist.sort_playlist("ASC")
        titles = [song.songtitle for song in playlist.songs]
        self.assertEqual(titles, ["Change", "Fifteen", "Love Story"])

    def test_sort_playlist_des(self):
        playlist = Playlist("Taylor Playlist")
        s1 = Song("Love Story", "Taylor Swift", 2008)
        s2 = Song("Change", "Taylor Swift", 2008)
        s3 = Song("Fifteen", "Taylor Swift", 2008)

        playlist.add_song(s1)
        playlist.add_song(s2)
        playlist.add_song(s3)

        playlist.sort_playlist("DES")
        titles = [song.songtitle for song in playlist.songs]
        self.assertEqual(titles, ["Love Story", "Fifteen", "Change"])

    def test_shuffle_playlist(self):
        playlist = Playlist("Taylor Playlist")
        s1 = Song("Love Story", "Taylor Swift", 2008)
        s2 = Song("Change", "Taylor Swift", 2008)
        s3 = Song("Fifteen", "Taylor Swift", 2008)

        playlist.add_song(s1)
        playlist.add_song(s2)
        playlist.add_song(s3)

        before_shuffle = playlist.songs.copy()
        playlist.shuffle_playlist()
        after_shuffle = playlist.songs

        self.assertEqual(len(before_shuffle), len(after_shuffle))
        self.assertCountEqual(before_shuffle, after_shuffle)
unittest.main()