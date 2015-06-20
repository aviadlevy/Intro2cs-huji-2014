#!/usr/bin/env python3

from autotest import sp_test,mp_test,res_code,long_sequence_compare
from sys import argv
from os import chdir
import sys
from importlib import import_module
from numbers import Number
from math import isnan
from collections import Sequence
import copy

from rtset import rtset

class FakeException(Exception):
    pass

def allclose(act, exp, rtol=1.e-5, atol=1.e-5, history=None):
    if id(act)==id(exp):
        return True
    if isinstance(exp,int):
        return exp==act
    elif isinstance(exp,Number):
        if exp==act or isnan(exp) and isnan(act):
            return True
        return abs(act-exp) <= atol + rtol * abs(exp) #based on numpy allclose
    elif isinstance(exp,(list,tuple)): #python recursive '==' doesn't work any better than this
        if type(exp) != type(act) or len(exp) != len(act):
            return False
        for l_act,l_exp in zip(act,exp):
            if not allclose(l_act,l_exp):
                return False
        return True
    else:
        return exp==act

def import_runner(modulename, fname, args=[], kwargs={}):
    module = import_module(modulename)
    func = getattr(module, fname)
    args2 = copy.deepcopy(args)
    kwargs2 = copy.deepcopy(kwargs)
    res = func(*args, **kwargs)
    if not (args==args2 and kwargs==kwargs2): #good enough for now
        return ("modified", res)
    return (None,res)

def test_ex3(modulename="ex3",timeout=3):
    for name,(testlist) in rtset.items():
        correct = 0
        #answers = []
        for i,(fname,args,kwargs,ans) in enumerate(testlist):
            tname = name + "_" + str(i)
            try:
                res, (lres,retval) = mp_test(import_runner,[modulename,fname,args,kwargs], timeout=timeout)
                #ans=retval
                #answers.append((fname,args,kwargs,ans))
                #continue
                if res:
                    res_code(tname, res, retval)
                    continue
                if lres:
                    res_code(tname, lres, retval)
                    continue
                #if retval==ans: # correct result    #with no floats
                if allclose(ans, retval): # correct result   #deep float compare?
                    correct+=1
                    continue
                else:
                    if isinstance(ans, Sequence):
                        long_sequence_compare(tname, ans, retval, contextpreview=3)
                    else:
                        res_code(tname, "wrong", "\n".join(
                                ["Wrong result:",
                                 "expected: "+str(ans),
                                 "actual:   "+str(retval)]))
                    continue
            except Exception as e:
                res_code(tname, "testingFailed", e)
                continue

        #print (name+'=',answers)
        res_code(name, str(correct))

if __name__=="__main__":
    if len(argv) > 1:
        chdir(argv[1])
    if len(argv)>2:
        test_ex3(argv[2])
    else:
        test_ex3()
