import random

class Artist():
    def __init__(self, name, doB, country):
        self.name = name
        self.doB = doB
        self.country = country
        self.albumlist = []
        self.songlist = []

    def add_album(self, album):
        self.albumlist.append(album)

    def add_song(self, song):
        self.songlist.append(song)

    def display_info(self):
        print(f"Name: {self.name} DoB: {self.doB} country: {self.country}")
        print("Albums:")
        for album in self.albumlist:
            print(f"{album.title}")
        print("Songs:")
        for song in self.songlist:
            print(f"{song.songtitle}")

class Song():
    def __init__(self, songtitle, artistname, year):
        self.songtitle = songtitle
        self.artistname = artistname
        self.year = year

    def display_info(self):
        print(f"Song Title: {self.songtitle} Artist: {self.artistname} Year: {self.year}")

class Album():
    def __init__(self, title, artist_name, year):
        self.title = title
        self.artist_name = artist_name
        self.year = year
        self.songs = []

    def add_song(self, title, year):
        song = Song(title, self.artist_name, year)
        self.songs.append(song)

    def display_info(self):
        print(f"Album title: {self.title} Artist Name: {self.artist_name} Year: {self.year}")
        print("Songs:")
        for s in self.songs:
            print(f"Song {s.songtitle}")

class Playlist:
    def __init__(self, title):
        self.title = title
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)

    def print_all_song(self):
        print(f"Playlist: {self.title}")
        for song in self.songs:
            print(f" {song.songtitle} - {song.artistname}")

    def sort_playlist(self, order='ASC'):
        reverse = True if order == 'DES' else False
        self.songs.sort(key=lambda s: s.songtitle, reverse=reverse)

    def shuffle_playlist(self):
        random.shuffle(self.songs)


a1 = Artist("Taylor Swift", "13-12-1989", "USA")
album = Album("FEARLESS", "Taylor Swift", 2008)

album.add_song("Fifteen", 2008)
album.add_song("Love Story", 2008)
album.add_song("Change", 2008)

a1.add_album(album)

for song in album.songs:
    a1.add_song(song)

playlist = Playlist("Taylor Playlist")

for song in album.songs:
    playlist.add_song(song)

a1.display_info()
album.display_info()
playlist.print_all_song()

print("Sorted descending:")
playlist.sort_playlist("DES")
playlist.print_all_song()

print("Shuffled:")
playlist.shuffle_playlist()
playlist.print_all_song()