#############################################################
# FILE: battleship.py
# WRITER:
# EXERCISE : intro2cs ex4 2013-2014
# Description
#new_board - creates a new board game for a Battleship game
#place_ship - Put a new ship on the board
#fire - implement a fire in battleship game
#############################################################

"""Implement the following function according the description in ex4"""


def new_board(width=10,height=None):
    """creates a new board game for a Battleship game.

    Args:
    -width: a positive int - the width of the board - default value 10
    -height: a positive int - the height of the board - if not spcified
    should be as width

    return: a NEW enpty board - each inner arrays is a list of 'None's.

    n case of bad input: values are out of range returns None

    You can assume that the types of the input arguments are correct."""
    #define height defult value
    if height == None: height = width
    #check for proper value
    if width < 1 or height < 1:
        return
    newBoard = []
    #create the board
    for indexHeight in range(height):
        newBoard.append([])
        for indexWidth in range(width):
            newBoard[indexHeight].append(None)
    return newBoard
    


def place_ship(board,ship_length,bow,ship_direction):
    """Put a new ship on the board

    put a new ship (with unique index) on the board.
    in case of successful placing edit the board according to the definitions
    in the ex description.

    Args:
    -board - battleshipe board - you can assume its legal
    -ship_length: a positive int the length of the ship
    -bow: a tuple of ints the index of the ship's bow
    -ship_direction: a tuple of ints representing the direction the ship
    is facing (dx,dy) - should be out of the 4 options(E,N,W,S):
    (1,0) -facing east, rest of ship is to west of bow,
    (0,-1) - facing north, rest of ship is to south of bow, and etc.

    return: the index of the placed ship, if the placement was successful,
    and 'None' otherwise.

    In case of bad input: values are out of range returns None

     You can assume the board is legal. You can assume the other inputs
     are of the right form. You need to check that they are legal."""
    #check for proper value    
    if ship_length < 1: return
    #define some varible we'll use
    indexPlace = 0
    shipIndexList = []
    shipLengthList = [ship_length]
    boardWidthLen = len(board[0])
    boardHeightLen = len(board)
    heightBow = bow[1]
    widthBow = bow[0]
    boardIsOk = False
    #check for proper values
    if widthBow < 0 or widthBow > boardWidthLen \
       or heightBow < 0 or heightBow > boardHeightLen \
       or ship_direction[0] < -1 or ship_direction[0] > 1 \
       or ship_direction[1] < -1 or ship_direction[1] > 1 \
       or (ship_direction[1] == 1 and ship_direction[0] == 1) \
       or (ship_direction[1] == 0 and ship_direction[0] == 0) \
       or (ship_direction[1] == -1 and ship_direction[0] == -1) \
       or (ship_direction[1] == -1 and ship_direction[0] == 1) \
       or (ship_direction[1] == 1 and ship_direction[0] == -1):
        return
    #find the index of our new ship
    #we create a list with all ships indexes on board and find the max
    for countHi in range(len(board)):
        for countRo in range(len(board[countHi])):
            if board[countHi][countRo] != None:
                shipIndexList.append(board[countHi][countRo][0])
    if len(shipIndexList) == 0:
        shipIndex = 1
    else:
        shipIndex = (max(shipIndexList)) + 1
    #check if we can place the ship (in board and no other ship blocking)
    #if so, board is ok to place a ship
    for counter in range(0,ship_length):
        if widthBow < 0 or widthBow >= boardWidthLen \
           or heightBow < 0 or heightBow >= boardHeightLen:
            return
        elif board[heightBow][widthBow] != None: return        
        else: boardIsOk = True
        #move to our next cell
        widthBow -= ship_direction[0]
        heightBow -= ship_direction[1]
    
    heightBow = bow[1]
    widthBow = bow[0]
    if boardIsOk:
        #lets place the ship!
        for counter in range(0,ship_length):
            SHIP_IS_HERE = (shipIndex,indexPlace,shipLengthList)
            board[heightBow][widthBow] = SHIP_IS_HERE
            widthBow -= ship_direction[0]
            heightBow -= ship_direction[1]
            indexPlace += 1
    return shipIndex
        


def fire(board,target):
    """implement a fire in battleship game

    Calling this function will try to destroy a part in one of the ships on the
    board. In case of successful fire destroy the relevant part
    in the damaged ship by deleting it from the board. deal also with the case
    of a ship which was completely destroyed

    -board - battleshipe board - you can assume its legal
    -target: a tuple of ints (x,y) indices on the board
    in case of illegal target return None

    returns: a tuple (hit,ship), where hit is True/False depending if the the
    shot hit, and ship is the index of the ship which was completely
    destroyed, or 0 if no ship was completely destroyed. or 0 if no ship
    was completely destroyed.

    Return None in case of bad input

    You can assume the board is legal. You can assume the other inputs
    are of the right form. You need to check that they are legal."""

    widthTar = target[0]
    heightTar = target[1]
    #check for proper value
    if widthTar < 0 or widthTar >= len(board[0]) or \
       heightTar < 0 or heightTar >= len(board):
        return
    #miss:
    if board[heightTar][widthTar] == None:
        indexShip1 = 0
        hitValue = False
    #hit:
    else:
        shipLen = board[heightTar][widthTar][2][0]
        #hit value is True anyway
        hitValue = True
        #if we destroyed the whole ship
        if board[heightTar][widthTar][2] == [1]:
            #get the index and delete the cell
            indexShip1 = board[heightTar][widthTar][0]
            board[heightTar][widthTar] = None
        #if we hit but not destroyed the whole ship
        else:
            #index ship is 0, and length decrease by 1
            indexShip1 = 0
            board[heightTar][widthTar][2][0] = shipLen - 1
            board[heightTar][widthTar] = None
    tupleToReturn = (hitValue,indexShip1)
    return tupleToReturn
