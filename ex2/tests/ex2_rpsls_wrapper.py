#!/usr/bin/env python3

from collections import deque
import ex2_rpsls
import random

import setlist

def rep_game():
    if len(rep_game.future):
        res = rep_game.future.popleft()
    else:
        print("Unset future, returning random result")
        res = random.randrange(0,2)

    if res:
        print("Player wins fake game")
    else:
        print("Computer wins fake game")
    return res*2-1
rep_game.future = deque()


if __name__=="__main__":
    from sys import argv
    g = int(argv[1])

    rep_game.future.extend(setlist.getfuture(g))
    ex2_rpsls.rpsls_game = rep_game
    ex2_rpsls.rpsls_play()
