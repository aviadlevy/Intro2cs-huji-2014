from collections import Counter
import bisect

'''
This module contains several function for compress and decompress data, using
the Huffman code algorithm.
'''

MAGIC = b"i2cshcfv1"


def symbol_count(data):
    """The function get data (some character)
    The function return dictionary with num of appearance for each char
    in data.
    """
    return Counter(data)


def make_huffman_tree(counter):
    """The function get dictionary with num of appearance for chars.
    The function return huffman tree. (will be present by tuples)"""

    if len(counter) == 0:
        return

    #insert counter items to list and sort by number of appearance,
    # less first. if appearance is similar sort by value, bigger first.
    listOfCounts = sorted(counter.items(), key=lambda x: (x[1], -x[0]))

    #make the huffman code
    while len(listOfCounts) > 1:
        firstCell = listOfCounts.pop(0)
        secondCell = listOfCounts.pop(0)
        newValue = (secondCell[0], firstCell[0])
        newCount = firstCell[1] + secondCell[1]
        newCellToList = [newValue, newCount]
        counts = [count[1] for count in listOfCounts]
        index = bisect.bisect(counts, newCount)
        listOfCounts.insert(index, newCellToList)
    return listOfCounts[0][0]


def build_codebook(huff_tree, prefix=""):
    """the function gets huffman tree (from make_huff_tree), and prefix (a
    variable used for the recursive process).
    the function return dict which take each val and set the key to be tuple:
    (length [of the binary number],code [the decimal val of the binary
    number])
    """

    table = {}
    #end of recursive
    if not huff_tree and len(prefix) == 0:
        return {}
        #if we get to the val inside the tree, insert the tuple to the dict
    if type(huff_tree) is int:
        if len(prefix) == 0:
            prefix = '0'
        table[huff_tree] = (len(prefix), int(prefix, 2))
    #if not send right and left branch
    else:
        if type(huff_tree[0]) is int or type(huff_tree[0]) is tuple:
            table.update(build_codebook(huff_tree[0], prefix + '0'))
        if type(huff_tree[1]) is int or type(huff_tree[1]) is tuple:
            table.update(build_codebook(huff_tree[1], prefix + '1'))

    return table


def build_canonical_codebook(codebook):
    """the function get codebook and return canonical codebook
    """

    canonical_codebook = {}
    #sort the codebook
    a = sorted(codebook.items())
    sll = sorted(a, key=lambda variable: variable[1][0])

    num = '0'
    #go over items in list and add new tuple to list
    for item in sll:
        num = num + '0' * (item[1][0] - len(num))
        canonical_codebook[item[0]] = (item[1][0], int(num, 2))
        #convert the next decimal val to decimal
        num = "{0:b}".format(int(num, 2) + 1)
        num = "0" * (item[1][0] - len(num)) + num

    return canonical_codebook


def build_decodebook(codebook):
    """the function get codebook and return dictionary that can help decode
    the codebook
    """

    newCodebook = {}
    for key, value in codebook.items():
        newCodebook[value] = key
    return newCodebook


def compress(corpus, codebook):
    """the function get values (inside corpus) and code book
    the function return iterator that return '0' or '1' case on the values
    and the codebook (match binary num for each value)
    """
    #go all over corpus values
    for corpusVal in corpus:
        #get the bin number
        codeValBin = "{0:b}".format(codebook[corpusVal][1])
        #check if the length is match. if not add '0' to the left side
        if len(codeValBin) != codebook[corpusVal][0]:
            for index in range(codebook[corpusVal][0] - len(codeValBin)):
                codeValBin = '0' + codeValBin

        codeValBin.split()
        index = 0
        while index != len(codeValBin):
            yield int(codeValBin[index])
            index += 1


def decompress(bits, decodebook):
    """the function get bits and decodebook. the function return
    iterator of the values with the original values from compressed
    codebook"""
    tempBin = ''
    for bit in bits:
        #create new temp binary number
        tempBin = tempBin + str(bit)
        for key, val in decodebook.items():
            #go through all decodebook and check if len and bin value is
            #matched. if so, enter to yield
            if len(tempBin) == key[0] and int(tempBin, 2) == key[1]:
                yield val
                tempBin = ''


def pad(bits):
    """
    The function get sequence of bits.
    The function adds '1' and '0'-s to the last byte.
    The function return iterator that iterate the decimal values for each
    byte.
    """

    BYTE_LENGTH = 8
    tempByte = ''

    #run on bits and add to temp str variable. if we get the byte length,
    # yield the decimal value
    for bit in bits:
        tempByte = tempByte + str(bit)
        if len(tempByte) == BYTE_LENGTH:
            yield int(tempByte, 2)
            tempByte = ''

    #last byte. add '1'
    tempByte = tempByte + '1'
    #adds '0'-s so we'll get the byte length
    if len(tempByte) % BYTE_LENGTH != 0:
        while len(tempByte) < BYTE_LENGTH:
            tempByte = tempByte + '0'

    #yeild last byte
    yield int(tempByte, 2)


def unpad(byteseq):
    """The function gets byte sequence (like the output of pad).
    The function remove '0'-s and '1' from last byte and return iterator
    that return the binary value fo the sequence"""

    BYTE_LENGTH = 8
    binSeq = ''

    #if the input is not list', convert so we can work more easily
    if type(byteseq) is not list:
        byteseq = list(byteseq)

    index = 0

    for number in byteseq:

        #convert current numebr to binary
        binSeq = ("{0:b}".format(number))

        #if the length is smaller than the byte length expected, add '0'-s
        while len(binSeq) < BYTE_LENGTH:
            binSeq = '0' + binSeq

        #if we not at the last byte, yield the binary number
        if index != len(byteseq) - 1:
            for bit in binSeq:
                yield int(bit)
            index += 1

        #if we at the last byte, remove the '0'-s and '1' from the end,
        # and yield
        else:
            while binSeq[-1] != '1':
                binSeq = binSeq[:-1]
            binSeq = binSeq[:-1]  #remove the '1'
            for bit in binSeq:
                yield int(bit)


def join(data, codebook):
    """the function gets list of numbers (data) and codebook
    the function check if one of the index in range of 0 - 255 (bits) is in
    code book. if so it yield the length value from the code book.
    otherwise, it yield 0. then it yield all the numbers in data"""

    NUM_OF_BITS = 256

    #run from 0 to 255 and check if we got a match.
    for index in range(NUM_OF_BITS):

        if index in codebook:
            yield codebook[index][0]  #the length value for the index

        else:
            yield 0

    #yield data numbers
    for dataVal in data:
        yield dataVal


def split(byteseq):
    """the function get one bytes sequence of bits and data.
    the function split the and return a tuple with both data and the canonical
    codebook for the bits sequence"""

    NUM_OF_BITS = 256
    codebook = {}
    #if the input is not list', convert so we can work more easily
    if type(byteseq) is not list:
        byteseq = list(byteseq)

    #get first 256 bits
    bitSeq = byteseq[:NUM_OF_BITS]
    #make data a generator
    data = (dataVal for dataVal in byteseq[NUM_OF_BITS:])

    #build the codebook
    for index in range(len(bitSeq)):
        if bitSeq[index] != 0:
            codebook[index] = (bitSeq[index], 0)

    #return the data and the canonical codebook (use build_canonical_codebook)
    return data, build_canonical_codebook(codebook)
