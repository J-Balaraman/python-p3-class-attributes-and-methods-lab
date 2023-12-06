class Song:
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        Song.add_song_to_count(self)
        Song.add_to_genres(self.genre)
        Song.add_to_artists(self.artist)
        Song.add_to_genre_count(self.genre)
        Song.add_to_artist_count(self.artist)

    @classmethod
    def add_song_to_count(cls, beans):
        cls.count += 1

    @classmethod
    def add_to_genres(cls, genre):
        if genre in cls.genres:
            pass
        else:
            cls.genres.append(genre)
            cls.genre_count.update({f"{genre}" : 0})

    @classmethod
    def add_to_artists(cls, artist):
        if artist in cls.artists:
            pass
        else:
            cls.artists.append(artist)
            cls.artist_count.update({f"{artist}" : 0})

    @classmethod
    def add_to_genre_count(cls, genre):
        x = cls.genre_count[f'{genre}']
        cls.genre_count.update({f"{genre}" : (x + 1)})

    @classmethod
    def add_to_artist_count(cls, artist):
        x = cls.artist_count[f'{artist}']
        cls.artist_count.update({f"{artist}" : (x + 1)})