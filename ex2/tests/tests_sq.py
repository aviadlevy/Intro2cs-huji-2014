#!/usr/bin/env python3

from autotest import sp_test,mp_test,res_code,long_sequence_compare
from sys import argv
from os import chdir
import sys

from sqset import get_sq,sqset

def test_squares(script="ex2_square_wrapper.py", timeout=3, name="Squares"):
    correct = 0
    for i in sqset:
        ans = get_sq(i)
        try:
            res, output = sp_test([sys.executable,script,str(i)], timeout=timeout, input=str(i),
                                  universal_newlines=True)
            if res:
                res_code(name+str(i), res, output)
                continue
            if isinstance(output,str):
                output = output.encode()
            if output==ans: # correct result
                correct+=1
                continue
            else:
                long_sequence_compare(name+str(i), ans, output)
                continue
        except Exception as e:
            res_code(name+str(i), "testingFailed", e)
            continue

    res_code(name, str(correct))

if __name__=="__main__":

    if len(argv) > 1:
        chdir(argv[1])

    test_squares()
