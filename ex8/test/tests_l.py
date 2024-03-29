#!/usr/bin/env python3

from autotest import sp_test,mp_test,mp_test2,res_code,long_sequence_compare
import autotest as at
from sys import argv
from os import chdir
import sys
from importlib import import_module
from numbers import Number
from math import isnan
from collections import Sequence
import copy
import operator as op
from pprint import pprint
from types import GeneratorType
from itertools import islice
import re

from lset import lset,mset,sllist_to_list
import sllist

class FakeException(Exception):
    pass

def diff_str(intro,exp,act):
    return "\n".join([intro+":",
                      "expected: "+str(exp),
                      "actual:   "+str(act)])

def import_runner(modulename, fname, args=[], kwargs={}, check_input=True,tname=''):
    module = import_module(modulename)
    func = getattr(module, fname)
    if check_input:
        args2 = copy.deepcopy(args)
        kwargs2 = copy.deepcopy(kwargs)
    res = func(*args, **kwargs)
    if check_input:
        if not (args==args2 and kwargs==kwargs2): #good enough for now
            return ("modified", res)
    return (None,res)

def copy_convert(args):
    args2 = args[:]
    for i,sll in enumerate(args2):
        if isinstance(sll,sllist.List):
            args2[i] = sllist_to_list(sll)
    return args2


def import_runner_lstcmp(modulename, fname, args=[], kwargs={}, check_input=True,tname=''):
    if check_input:
        args2 = copy_convert(args)
    retval,res = import_runner(modulename, fname, args, kwargs, False,tname)
    if retval:
        return(retval,res)
    if check_input:
        if not (copy_convert(args)==args2): #good enough for now
            return ("modified", res)
    if isinstance(res,sllist.List):
        res = [n.data for n in sllist_to_list(res)]
    return (None,res)

def import_runner_modified(modulename, fname, args=[], kwargs={}, check_input=True,tname=''):
    ans = kwargs.pop("_ans",[])
    datalist = [n.data for n in ans]
    retval,res = import_runner(modulename, fname, args, kwargs, False,tname)
    if retval:
        return(retval,res)
    new_list = sllist_to_list(args[0])
    if new_list != ans:
        return ("wrong",diff_str("Wrong result, input: "+str(args),ans,retval))
    if ans and ans[-1].next is not None:
        return ("wrong","Result has cycle")
    datalist2 = [n.data for n in ans]
    for (d1,d2) in zip(datalist,datalist2):
        if d1 is not d2:
            return ("modified","node data was modified")
    return (None,res)

def import_runner_generator(modulename, fname, args=[], kwargs={},tname=''):
    outlen = kwargs.pop("_length",10)
    retval,res = import_runner(modulename, fname, args, kwargs)
    if retval:
        return(retval,res)
    if isinstance(res, Sequence):
        return ('notgenerator',type(res))
    return (None,list(islice(res,outlen)))

def import_runner_rand(modulename, fname, args=[], kwargs={},tname=''):
    retval,res = import_runner(modulename, fname, args, kwargs)
    if retval:
        return(retval,res)
    if not re.match(r'^[a-z]*$',res):
        return ('illegalchar','illegal character in '+str(res))
    if len(res)>500:
        missed = [c for c in 'abcdefghijklmnopqrstuvwxyz' if c not in res]
        if missed:
            return ('lettermissed','letters not in long random sequence: '+str(''.join(missed)))
    return (None,len(res))

def test_sllist_utils(modulename="sllist_utils",timeout=3):
    for name,testlist in lset.items():
        test_set(name,testlist,modulename,timeout,runner=import_runner_lstcmp)
    for name,testlist in mset.items():
        test_set(name,testlist,modulename,timeout,runner=import_runner_modified)

def test_set(name, testlist, modulename="oneliners",timeout=3,
             runner=import_runner, comparemethod=None):
    correct = 0
    #answers = []
    for i,(fname,args,kwargs,ans) in enumerate(testlist):
        tname = name + "_" + str(i)
        try:
            res, retval = mp_test2(runner,[modulename,fname,args,kwargs],{"tname":tname}, timeout=timeout)
            #ans=retval
            #answers.append((fname,args,kwargs,ans))
            #continue
            if res=="skip":
                continue
            if res:
                res_code(tname, res, retval)
                continue
            if retval==ans:
                correct+=1
                continue
            else:
                #if isinstance(ans, Sequence):
                #    long_sequence_compare(tname, ans, retval, contextpreview=3)
                #else:
                res_code(tname, "wrong",diff_str("Wrong result, input: "+str(args),ans,retval))
                continue
        except at.Error as e:
            res_code(tname, e.code, e.message)
        except Exception as e:
            res_code(tname, "testingFailed", e)
            continue

    #print (name+'=',answers)
    res_code(name, str(correct))

if __name__=="__main__":
    if len(argv)>1:
        #test_mystery(argv[1])
        test_sllist_utils()
    else:
        test_sllist_utils()
