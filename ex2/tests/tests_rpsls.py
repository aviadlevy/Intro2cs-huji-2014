#!/usr/bin/env python3

from autotest import sp_test,mp_test,res_code,long_sequence_compare
from sys import argv
from os import chdir
import sys

import gamelist
import setlist

def test_rpsls_game(script="ex2_rpsls_game_wrapper.py", timeout=3, name="RPSLSgame"):
    correct = 0
    for i in range(len(gamelist.l)):
        for w in (0,1):
            ans = gamelist.d[(i,w)]
            tname = name+"_"+str(i)+"_"+str(w)
            try:
                res, output = sp_test([sys.executable,script,str(i),str(w)],
                                      timeout=timeout,
                                      input=gamelist.game_input_str(i,1-w),
                                      universal_newlines=True)
                if res:
                    res_code(tname, res, output)
                    continue
                if isinstance(output,str):
                    output = output.encode()
                if output==ans: # correct result
                    correct+=1
                    continue
                else:
                    long_sequence_compare(tname, ans, output)
                    continue
            except Exception as e:
                res_code(tname, "testingFailed", e)
                continue
    res_code(name, str(correct))

def test_rpsls_illegal(script="ex2_rpsls_game_wrapper.py", timeout=3, name="RPSLSillegal"):
    ans = gamelist.ill
    try:
        res, output = sp_test([sys.executable,script]+gamelist.illargs,
                              timeout=timeout,
                              input="0\n-5\n6\n12345678901234567890\n-987654321\n-987654321\n1234567890\n6\n-5\n0\n2\n-987654321\n1234567890\n6\n-5\n0\n0\n-5\n6\n1234567890\n-9876543211234567890\n2\n",
                              universal_newlines=True)
        if res:
            res_code(name, res, output)
        else:
            if isinstance(output,str):
                output = output.encode()
            if output==ans: # correct result
                res_code(name, "correct")
            else:
                long_sequence_compare(name, ans, output)
    except Exception as e:
        res_code(tname, "testingFailed", e)

def test_rpsls_singleset(script="ex2_rpsls_wrapper.py", timeout=3, name="RPSLSsingleset"):
    correct = 0
    #d = {}
    for i in range(len(setlist.l)):
        ans = setlist.r[i]
        tname = name+"_"+str(i)
        try:
            res, output = sp_test([sys.executable,script,str(i)],
                                  timeout=timeout,
                                  input=setlist.ssetinput(i)+"\n1\n",
                                  universal_newlines=True)
            if res:
                res_code(tname, res, output)
                continue
            if isinstance(output,str):
                output = output.encode()
                #d[i] = output
                #continue
            if output==ans: # correct result
                correct+=1
                continue
            else:
                long_sequence_compare(tname, ans, output)
                continue
        except Exception as e:
            res_code(tname, "testingFailed", e)
            continue
    res_code(name, str(correct))
    #print("r =",d)

def test_rpsls_setseries(script="ex2_rpsls_wrapper.py", timeout=3, name="RPSLSsetseries"):
    correct = 0
    #d = {}
    for i in range(len(setlist.l2)):
        ans = setlist.r2[i]
        tname = name+"_"+str(i)
        try:
            res, output = sp_test([sys.executable,script,str(i+len(setlist.l))],
                                  timeout=timeout,
                                  input=setlist.msetinput(i)+"1\n",
                                  universal_newlines=True)
            if res:
                res_code(tname, res, output)
                continue
            if isinstance(output,str):
                output = output.encode()
                #d[i] = output
                #continue
            if output==ans: # correct result
                correct+=1
                continue
            else:
                long_sequence_compare(tname, ans, output)
                continue
        except Exception as e:
            res_code(tname, "testingFailed", e)
            continue
    res_code(name, str(correct))
    #print("r2 =",d)

def test_rpsls_setreset(script="ex2_rpsls_wrapper.py", timeout=3, name="RPSLSsetreset"):
    correct = 0
    #d = {}
    for i in range(len(setlist.l)):
        ans = setlist.r3[i]
        tname = name+"_"+str(i)
        try:
            res, output = sp_test([sys.executable,script,str(i+len(setlist.l)+len(setlist.l2))],
                                  timeout=timeout,
                                  input=setlist.rsetinput(i)+"1\n",
                                  universal_newlines=True)
            if res:
                res_code(tname, res, output)
                continue
            if isinstance(output,str):
                output = output.encode()
                #d[i] = output
                #continue
            if output==ans: # correct result
                correct+=1
                continue
            else:
                long_sequence_compare(tname, ans, output)
                continue
        except Exception as e:
            res_code(tname, "testingFailed", e)
            continue
    res_code(name, str(correct))
    #print("r3 =",d)

if __name__=="__main__":

    if len(argv) > 1:
        chdir(argv[1])

    test_rpsls_game()
    test_rpsls_illegal()
    test_rpsls_singleset()
    test_rpsls_setseries()
    test_rpsls_setreset()
