__author__ = 'win7'
import string

def get_words(text):
    wordList = []
    for word in text.split():
        for char in word:
            if char not in string.ascii_letters:
                break
        else:
            wordList.append(word.lower())
    return sorted(wordList)

print(get_words('abc ascka a$R#fv dsnl abc Abc'))


