#!/usr/bin/env python3

from collections import deque
import random
import ex2_rpsls

def setseed(seed):
    random.seed(seed)


class FakeRandom(random.Random):
    """Fake random number generator which returns preset numbers for specific range."""

    def __init__(self):
        super().__init__()
        self.future = deque()

    def randrange(self, start, stop=None, step=1, int=int):
        if start==1 and stop==6 and step==1 and len(self.future):
            return self.future.popleft()
        return super().randrange(start, stop, step, int)

    def clear_future(self):
        self.future.clear()

    def set_future(self, seq):
        self.future.extend(seq)

    def replace_inst(self):
        random.seed = random._inst.seed
        random.randint = random._inst.randint
        random.randrange = random._inst.randrange
        

import gamelist

if __name__=="__main__":
    from sys import argv,stderr
    random._inst = FakeRandom()
    random._inst.replace_inst()
    g = int(argv[1])
    d = int(argv[2])
    random._inst.set_future(gamelist.l[g][1][d])
    for i in range(gamelist.l[g][0]):
        res=ex2_rpsls.rpsls_game()
        if res==1:
            retres = "Player won"
        elif res==-1:
            retres = "Computer won"
        else:
            retres = "Illegal return value"
        print("Return value indicates:",retres)

