#############################################################
# FILE: GetToTheZero.py
# WRITER: Aviad Levy
# EXERCISE : intro2cs ex5 2013-2014
# Description
# is_solvable - check if the puzzle given is solvable
#############################################################
def is_solvable(start, board):
    '''takes a starting position of the agent, and a puzzle board (list).
    We can "bounce" specific steps between cells according to the value in it.
    The function will return true if it is possible to solve the puzzle
    from the configuration specified in the parameters (get to the end),
    and should return false if it is impossible.'''
    newBoard = board[:]
    #check start index is on board
    if start < 0 or start >= len(newBoard):
        return False
    #check if we not visited this cell
    elif newBoard[start] == None:
        return False
    #check if we go to the end of the line
    elif start == len(newBoard) -1:
        return True

    else:
        step = newBoard[start]
        #None mean we visited this cell
        newBoard[start] = None
        #go right the num of step in cell
        right = is_solvable(start + step,newBoard)
        #go left the num of step in cell
        left = is_solvable(start - step,newBoard)
        #if either left or right get me to the end,
        #that's great! we solved this!
        if right or left: return True
        else:
            return False