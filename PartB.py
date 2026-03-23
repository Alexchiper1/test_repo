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

    #not instance
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

unittest.main()