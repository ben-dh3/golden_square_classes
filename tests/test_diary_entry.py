from lib.diary_entry import *

def test_diary_entry():
    diary_entry = DiaryEntry('title','contents')
    pass

def test_format_diary():
    diary_entry = DiaryEntry('14/11/23','Hello world!')
    result = diary_entry.format()
    assert result == '14/11/23: Hello world!'

def test_count_words():
    diary_entry = DiaryEntry('14/11/23','Hello world!')
    result = diary_entry.count_words()
    assert result == 2

def test_reading_time():
    # 50 words long
    diary_entry = DiaryEntry(' 14/11/23','Hello world! Here is an example post for this exercise Hello world! Here is an example post for this exercise Hello world! Here is an example post for this exercise Hello world! Here is an example post for this exercise Hello world! Here is an example post for this exercise')
    # 200 WPM
    result = diary_entry.reading_time(200)
    assert result == 0.25

def test_reading_chunk():
    diary_entry = DiaryEntry(' 14/11/23','Hello world! Here is an example post for this exercise hello world! here is an example post for this exercise Hello world! Here is an example post for this exercise Hello world! Here is an example post for this exercise Hello world! Here is an example post for this exercise')
    first_chunk = diary_entry.reading_chunk(10,1)
    assert first_chunk == 'Hello world! Here is an example post for this exercise'
    second_chunk = diary_entry.reading_chunk(10,1)
    assert second_chunk == 'hello world! here is an example post for this exercise'
    third_chunk = diary_entry.reading_chunk(10,1)
    fourth_chunk = diary_entry.reading_chunk(10,1)
    fifth_chunk = diary_entry.reading_chunk(10,1)
    restart_chunk = diary_entry.reading_chunk(10,1)
    assert restart_chunk == 'Hello world! Here is an example post for this exercise'

