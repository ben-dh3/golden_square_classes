class DiaryEntry:
    def __init__(self, title, contents):
        self.title = title
        self.contents = contents
        self.words_per_chunk=0
        self.iterator=0

    def format(self):
        return f"{self.title}: {self.contents}"

    def count_words(self):
        return len(self.contents.split(' '))

    def reading_time(self, wpm):
        string_length = len(self.contents.split(' '))
        return string_length/wpm

    def reading_chunk(self, wpm, minutes):
        # split contents into words
        split_string = self.contents.split(' ')
        # calculate no. words per chunk
        self.words_per_chunk = wpm * minutes
        # calculate no. chunks (words in content / words per chunk)
        number_of_chunks = int(len(split_string)/self.words_per_chunk)
        current_chunk = self.iterator * self.words_per_chunk
        # if all the content has been returned by previous calls, restart
        if self.iterator >= number_of_chunks:
            self.iterator = 0
            current_chunk = self.iterator * self.words_per_chunk
        # return the corresponding chunk   
        for i in range(self.iterator,number_of_chunks):
            # increment
            self.iterator+=1
            # print(self.iterator)
            return ' '.join(split_string[current_chunk:current_chunk+self.words_per_chunk])
        
        
        
        

# diary_entry=DiaryEntry(' 14/11/23','Hello world! Here is an example post for this exercise hello world! Here is an example post for this exercise Hello world! Here is an example post for this exercise Hello world! Here is an example post for this exercise Hello world! Here is an example post for this exercise')
# print(diary_entry.reading_chunk(10,1))
# print(diary_entry.reading_chunk(10,1))
# print(diary_entry.reading_chunk(10,1))
# print(diary_entry.reading_chunk(10,1))
# print(diary_entry.reading_chunk(10,1))
# print(diary_entry.reading_chunk(10,1))
        # Parameters
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   string: a chunk of the contents that the user could read in the
        #           given number of minutes
        #
        # If called again, `reading_chunk` should return the next chunk,
        # skipping what has already been read, until the contents is fully read.
        # The next call after that should restart from the beginning.
        