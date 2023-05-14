class Song(object):

    def __init__(self, lyrics) -> None:
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"])

bulls_on_parade = Song(["They rally around tha family",
                        "With pockets full of shells"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()


# Drills
class Song_comprehension(object):
    
    def __init__(self, lyrics) -> None:
        self.lyrics = lyrics
    
    def sing_it(self):
        [print(line) for line in self.lyrics]

new_song = ["We will",
            "We will",
            "Rock you"]

my_song = Song_comprehension(new_song)
my_song.sing_it()