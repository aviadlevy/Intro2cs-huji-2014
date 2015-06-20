from ex4 import *
from battleship import *
from copy import deepcopy
import pprint
_names = ("h2","h4","h6","h8","h1","h3","h5","h7","h9")
_boards_src = { (1,1) : [[None]],
            (1,10) : [[None],[None],[None],[None],[None],[None],[None],[None],[None],[None]],
            (10,1) : [[None,None,None,None,None,None,None,None,None,None]],
            (4,5) : [[None,None,None,None],
                     [None,None,None,None],
                     [None,None,None,None],
                     [None,None,None,None],
                     [None,None,None,None]],
            (6,6) : [[None,None,None,None,None,None],
                     [None,None,None,None,None,None],
                     [None,None,None,None,None,None],
                     [None,None,None,None,None,None],
                     [None,None,None,None,None,None],
                     [None,None,None,None,None,None]],
            (5,7) : [[None,None,None,None,None],
                     [None,None,None,None,None],
                     [None,None,None,None,None],
                     [None,None,None,None,None],
                     [None,None,None,None,None],
                     [None,None,None,None,None],
                     [None,None,None,None,None]],
            (7,5) : [[None,None,None,None,None,None,None],
                     [None,None,None,None,None,None,None],
                     [None,None,None,None,None,None,None],
                     [None,None,None,None,None,None,None],
                     [None,None,None,None,None,None,None]],
            (10,10) : [[None,None,None,None,None,None,None,None,None,None],
                       [None,None,None,None,None,None,None,None,None,None],
                       [None,None,None,None,None,None,None,None,None,None],
                       [None,None,None,None,None,None,None,None,None,None],
                       [None,None,None,None,None,None,None,None,None,None],
                       [None,None,None,None,None,None,None,None,None,None],
                       [None,None,None,None,None,None,None,None,None,None],
                       [None,None,None,None,None,None,None,None,None,None],
                       [None,None,None,None,None,None,None,None,None,None],
                       [None,None,None,None,None,None,None,None,None,None]]
            }
            
def get_board(name):
    return deepcopy(_boards_src[name])

def prepare_board(board,segments):
    for seg in segments:
        board[seg[1]][seg[0]] = seg[2]
    return board

def fix_board(board):
    d = {}
    for row in board:
        for i,cell in enumerate(row):
            if cell:
                if cell[0] not in d:
                    d[cell[0]] = [0][:]
                d[cell[0]][0]+=1
                row[i] = (cell[0],cell[1],d[cell[0]])
    return board

def recount_board(board):
    for row in board:
        for cell in row:
            if cell:
                cell[2][0]=0
    for row in board:
        for cell in row:
            if cell:
                cell[2][0]+=1
    return board


binst1 = [(1,2,(1,0)),(2,4,(2,0)),(3,6,(3,0)),(4,8,(4,0)),(6,0,(5,0)),(6,4,(6,0)),(8,8,(7,0)),(9,0,(8,0))]
bl1 = [(a[0],a[1]) for a in binst1]
binst2 = [(1,2,(1,0)),(1,3,(1,1)),(3,6,(3,0)),(3,8,(3,2)),(6,0,(5,4)),(6,4,(5,0)),(7,8,(7,3)),(9,8,(7,1))]
bl2 = [(a[0],a[1]) for a in binst2]


_vals = (0,1,5,10,50,100,500,1000,10000,1000000)

_inputs = list(zip(("h"+str(i) for i in range(20)),_vals+tuple(float(v) for v in _vals),_vals+_vals[::-1]))


def f0(home):
    return home[1]+1

def f1(home):
    return home[1]+home[2]

def f2(home):
    return home[1]+home[2]**2/2

def f3(home):
    return home[1]+home[2]**3/6

def op_homes(seed,opps):
    r = random.Random()
    r.seed(seed)
    opps=list(opps)
    r.shuffle(opps)
    res = list(zip(_names,range(100,1000,100),opps))
    r.shuffle(res)
    return res










#x = bubble_sort_2nd_value(list(zip(_names,(1, 15, 16, 45, 32, 8, 54, 49, 185))))
x=live_like_a_king(1000, 25, [1,2,3,4,5,6,7], [8,9],-10**-5)
#x=choosing_retirement_home(100,[],[("h1",100),("h2",900)])
#x=new_board(2)
#x=place_ship(fix_board(prepare_board(get_board((10,10)),binst2)),5, (9,3) , (0, 1))
#x=fire(fix_board(prepare_board(get_board((10,10)),binst2)), (1, 2) , )
#x=get_value_key(0)
#x=choose_retirement_home_opponents(1000,f2,[("h1",100,80),("h2",900,20)])

print(x)
#pprint.pprint(x)
