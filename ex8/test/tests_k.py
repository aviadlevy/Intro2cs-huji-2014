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

from kset import kset,sklist_to_list
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


def consistent(sklist,nlist,dlist,verbose=False):
    if not nlist:
        return sklist.head is None and sklist.tail is None

    nlist=nlist[:]
    i,cur = 0,sklist.head
    while cur and i<len(nlist):
        if nlist[i] and nlist[i] is not cur:
            return False
        nlist[i]=cur
        i,cur = i+1,cur.next

    return (all(nlist) and
            sklist.head is nlist[0] and 
            sklist.tail is nlist[-1] and 
            all(n.data is d for n,d in zip(nlist,dlist)) and
            all(nlist[i].skip_back is (nlist[i-2] if i>1 else None) for i,n in enumerate(nlist)) and
            all(nlist[i].next is (nlist[i+1] if i<len(nlist)-1 else None) for i,n in enumerate(nlist)))

def import_runner_class_sklist(modulename, fname, args=[], kwargs={},tname=''):
    nlist = kwargs.pop("_nlist",[])
    dlist = [n.data for n in nlist]
    func = kwargs.pop("_func",None)
    argseq = kwargs.pop("_argseq",None)
    retval,sklist = import_runner(modulename, fname, args, kwargs)
    if retval:
        return(retval,sklist)
    if nlist:
        sklist.head, sklist.tail = nlist[0], nlist[-1]
    if not consistent(sklist,nlist,dlist):
        return('ctorfail','construction failed')
    res = []
    if func is None:
        return None,None
    elif func=='add_first':
        for val in argseq:
            res.append(getattr(sklist, func)(val))
            nlist[:0]=[None]
            dlist[:0]=[val]
    elif func=='add_last':
        for val in argseq:
            res.append(getattr(sklist, func)(val))
            nlist.append(None)
            dlist.append(val)
    elif func=='remove_first':
        for i in argseq:
            res.append(getattr(sklist, func)())
            nlist.pop(0)
            dlist.pop(0)
    elif func=='remove_last':
        for i in argseq:
            res.append(getattr(sklist, func)())
            nlist.pop()
            dlist.pop()
    elif func=='remove_node':
        res.append(getattr(sklist, func)(nlist[argseq]))
        nlist.pop(argseq)
        dlist.pop(argseq)
    elif func=='getitem_g':
        res.append(sklist[argseq])
    elif func=='getitem_b':
        try:
            res.append(sklist[argseq])
        except IndexError:
            pass
    else:
        return('nofunction',"Couldn't find function to run")
    if not consistent(sklist,nlist,dlist):
        return('badlist','list is not in state it should be')
    return (None,res)

def test_skipi_list(modulename="skipi_list",timeout=3):
    for name,testlist in kset.items():
        test_set(name,testlist,modulename,timeout,runner=import_runner_class_sklist)
    #for name,testlist in mset.items():
    #    test_set(name,testlist,modulename,timeout,runner=import_runner_modified)

def test_set(name, testlist, modulename="skipi_list",timeout=3,
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
        test_skipi_list()
    else:
        test_skipi_list()
