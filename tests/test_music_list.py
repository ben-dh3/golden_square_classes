from lib.music_list import *

def test_music_list():
    music_list = Music()
    result = music_list.add_track('Bakers Street')
    assert result == ['Bakers Street']

def test_long_music_list():
    music_list = Music()
    music_list.add_track('LOVE')
    result = music_list.add_track('Bakers Street')
    assert result == ['LOVE','Bakers Street']