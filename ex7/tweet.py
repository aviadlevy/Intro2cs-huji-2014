from doctest import run_docstring_examples
import string
import re
from geo import Position

class Tweet:
    def __init__(self, text, time, lat, lon):
        self.__text = text
        self.__time = time
        self.__lat = lat
        self.__lon = lon

    def get_words(self):
        """Return the words in a tweet, not including punctuation.
        """
        #replace every none letter with a space and then create a string
        # with only lowercase words
        return re.sub("[^a-zA-Z]", " ",  self.__text).lower().split()

    def get_text(self):
        """Return the text of the tweet."""
        return self.__text

    def get_time(self):
        """Return the datetime that represents when the tweet was posted."""
        return self.__time

    def get_location(self):
        """Return a position (see geo.py) that represents the tweet's location."""
        return Position(self.__lat,self.__lon)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return (self.get_text() == other.get_text() and
                    self.get_location() == other.get_location() and
                    self.get_time() == other.get_time())
        else:
            return False

    def __str__(self):
        """Return a string representing the tweet."""
        return '"{0}" @ {1} : {2}'.format(self.get_text(), 
                                          self.get_location(), 
                                          self.get_time())

    def __repr__(self):
        """Return a string representing the tweet."""
        return 'Tweet({0}, {1}, {2}, {3})'.format(*map(repr,(self.get_text(),
                                                             self.get_time(),
                                                             self.get_location(
                                                             ).latitude(),
                                                             self.get_location(
                                                             ).longitude())))

    def get_sentiment(self,word_sentiments):
        """ Return a sentiment representing the degree of positive or negative
        sentiment in the given tweet, averaging over all the words in the tweet
        that have a sentiment value.
        """
        wordList = self.get_words()
        summarize = 0
        index = 0
        #serch for match word and if found, summarize to get average in the
        # end. if not found return None
        for word in wordList:
            if word in word_sentiments:
                summarize += word_sentiments[word]
                index += 1
        if index == 0:
            return
        return summarize / index


