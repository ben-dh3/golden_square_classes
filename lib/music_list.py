# As a user
# So that I can keep track of my music listening
# I want to add tracks I've listened to and see a list of them.

class Music():
    def __init__(self):
        self.music_list = []

    def add_track(self,track):
        self.music_list.append(track)
        return self.music_list