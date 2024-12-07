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
        self.add_to_genres(genre)
        self.add_song_to_count()
        self.add_to_artist(artist)
        self.add_to_genre_count(genre)
        self.add_to_artist_count(artist)

    @classmethod
    def add_song_to_count(cls, increment = 1):
        cls.count += increment

    @classmethod
    def add_to_genres(cls, genre):
        cls.genres.append(genre)

    @classmethod
    def add_to_artist(cls, artist):
        cls.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls, genre):
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
            print(f"The genre '{genre}' is repeated.")

        else:
            cls.genre_count[genre] = 1

    @classmethod
    def add_to_artist_count(cls, artist):
        if artist in cls.artist_count:
            cls.artist_count[artist] +=1
            print(f"the artist '{artist}' is repeated")

        else:
            cls.artist_count[artist] = 1




song1 = Song("Sweet oblivion", "David kushner", "RnB")
song2 = Song("Solo", "Myles Smith", "Rpop")
song3 = Song("Shine Bright", "Alicia Keys", "Pop")
song4 = Song("Vibe", "Myles Smith", "RnB")
print(Song.genre_count)
