#############################################################
# FILE: AlignDNA.py
# WRITER: Aviad Levy
# EXERCISE : intro2cs ex5 2013-2014
# Description
# get_alignment_score - takes two aligned DNA strands and
# returns the score of the alignment.
#############################################################
def get_alignment_score(strandOne, strandTwo, match=1, mismatch=-1, gap=-2):
    '''takes two aligned DNA strands (you may assume that they have the same
     length) and three optional scores value: match with default value of 1,
     mismatch with default value of -1 and gap with default value of -2.
     The function returns the score of the alignment.'''
    summarize = 0
    for index in range(min(len(strandOne), len(strandTwo))):
        if strandOne[index] == strandTwo[index]:
            if strandOne[index] != '-':
                summarize += match
        elif strandOne[index] != strandTwo[index] and \
                (strandOne[index] != '-' and strandTwo[index] != '-'):
            summarize += mismatch
        else:
            summarize += gap
    summarize += gap * (abs(len(strandTwo) - len(strandOne)))
    return summarize


def get_best_alignment_score(strandOne,strandTwo,match=1,mismatch=-1,gap=-2):
    '''takes two unaligned DNA strands (strings) and three optional scores
     value . The function calculates and returns a tuple of the highest score
      for the alignment of the two strands and the two aligned strands.'''
    #in case score is not defined yet
    if 'score' not in locals():
        score = 0
    #stop when both strands are empty
    if len(strandOne) == 0 and len(strandTwo) == 0:
        return 0 ,strandOne , strandTwo
    #stop when one strand is empty (if they not equal). if so complete the
    #difference with '-'
    elif len(strandOne) == 0 and len(strandTwo) != 0:
        return len(strandTwo) * gap, '-' * len(strandTwo), strandTwo
    elif len(strandTwo) == 0 and len(strandOne) != 0:
        return len(strandOne) * gap, strandOne, '-' * len(strandOne)
    #check the value for two letters
    bothLetters = get_best_alignment_score(strandOne[1:],strandTwo[1:],
                                             match,mismatch,gap)
    #check the value for one letter from each strand and the other is gap
    strandOneGap = get_best_alignment_score(strandOne,strandTwo[1:],
                                                 match,mismatch,gap)
    strandTwoGap = get_best_alignment_score(strandOne[1:],strandTwo,match,
                                            mismatch,gap)
    #remember the letters we check
    strandOneLetter = strandOne[0]
    strandTwoLetter = strandTwo[0]
    #check if we got a match
    if strandOne[0] == strandTwo[0]:
        score += match
    else:
        score += mismatch

    #make tuples with three option:
    #option 1 - we checked both letters.
    #option 2 - we checked for gap in strand 1
    #option 3 - we checked for gap in strand 2
    tupleOption1 = (bothLetters[0] + score,strandOneLetter+bothLetters[1],
                        strandTwoLetter+bothLetters[2])
    tupleOption2 = (strandOneGap[0]+gap , "-" + strandOneGap[1],
                          strandTwoLetter +strandOneGap[2])
    tupleOption3 = (strandTwoGap[0]+gap , strandOneLetter + strandTwoGap[1],
                    "-" + strandTwoGap[2])
    #check what option is the highest
    highestScore = (max(tupleOption1[0],tupleOption2[0],tupleOption3[0]))

    #reurn the tuple of the highest score
    tupleOfTuples = (tupleOption1,tupleOption2,tupleOption3)
    for index in range(3):
        if tupleOfTuples[index][0] == highestScore:
            return highestScore,tupleOfTuples[index][1],tupleOfTuples[index][2]
