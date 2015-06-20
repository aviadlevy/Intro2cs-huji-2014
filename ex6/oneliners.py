def is_two_palindrome(word) :
    '''The function tests if the given string is a “two palindrome” or not.
    in this function i used:
    slicing for string in order to get the two half and the reverse for each
    one and compare them.
    i used special condition for 1 length word so it match the expected result.
    '''
    
    return True if len(word) == 1 else word[:len(word)//2] == \
        word[len(word)//2-1::-1] and word[len(word)//2+len(word)%2:] == \
        word[:len(word)//2-(len(word)+1)%2:-1]

def uni_sort(firstList,secondList):
    '''The function combines two unsorted lists of integers into one sorted
     list.
    at first i merge both list, without sorting. then i used enumerate so i can
    scan the rest of the list to get rid of duplicates, and used 'sorted'
    on the result'''
    
    combindLists = firstList + secondList
    return sorted([cell for index,cell in enumerate(combindLists) \
                   if cell not in combindLists[:index]])

def dot_product(firstVector,secondVector):
    '''The function returns the dot product of two vectors.
    in this function i used:
    zip - make iterators from sequence. specificly it get the two values
    from each 'i' index in both lists to both variables.
    sum - summarize the whole values we get'''

    return sum(firstVectorValue*secondVectorValue for firstVectorValue,
                          secondVectorValue in zip(firstVector,secondVector))

def list_intersection(firstList,secondList):
    '''The function returns a new list sorted in ascending order. The
    output list contain those integers that appear in both input lists.
    in this function i used:
    set on the values from firstList if they appear on the second'''

    return sorted(list(set([cell for cell in firstList if cell in secondList])))

def list_difference(firstList,secondList):
    '''The function returns a list sorted in ascending order. The output
    list contain those integers that appear in just one of the input lists.
    in this function i used:
    set on the values from firstList if they not in the second and the
    value from the secondList if they not in the first'''

    return sorted(list(set( \
        [cell for cell in firstList if cell not in secondList] + \
        [cell for cell in secondList if cell not in firstList])))

import random , string
def random_string(numberOfChars):
    '''The function generates a random string of a given length.
    in this function i used:
    ''.join - add char that have been chosen from the random function
    random.choice - return a random element from given sequence  -
                    need to import random
    string.ascii_lowercase - all the lowercase letters  -
                             need to import string'''
    return ''.join(random.choice(string.ascii_lowercase) \
                   for index in range(numberOfChars))

import re
def word_mapper(string):
    '''The function returns a dictionary mapping from the words in the input
    text to their number appearances.
    in this function I used:
    re.sub - replace the given char in another char. (need to import 're').
    specificity, I used it to replace all none letters/numbers in white
    space. ([\W] mean that we replace all none [a-zA-Z0-9], and i add also '_')
    then I put it in list (using split()) and convert it to lowercase
    (using lower()).
    list.count - count the number of appearance in my list'''

    wordsList = re.sub("[\W_]", " ",  string).lower().split()
    return {item : wordsList.count(item) for item in wordsList}


def gimme_a_value(func,start):
    '''The function get a function and a starting point and returns a
    generator - on first call the starting point and then returns the value
    after pushing him to the function'''

    while True:
        yield start
        start = func(start)
