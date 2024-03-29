"""Runs test(s) in process"""

import subprocess as sp
import multiprocessing as mp

import os
import signal
import tarfile
import fnmatch
from difflib import SequenceMatcher


def check_io(*popenargs, timeout=None, input=None, **kwargs):
    if 'stdin' in kwargs:
        raise ValueError('stdin argument not allowed, it will be overridden.')
    if 'stdout' in kwargs:
        raise ValueError('stdout argument not allowed, it will be overridden.')

    with sp.Popen(*popenargs, stdout=sp.PIPE, stdin=sp.PIPE, **kwargs) as process:
        try:
            output, unused_err = process.communicate(input=input, timeout=timeout)
        except sp.TimeoutExpired:
            process.kill()
            output, unused_err = process.communicate()
            raise sp.TimeoutExpired(process.args, timeout, output=output)
        except:
            process.kill()
            process.wait()
            raise
        retcode = process.poll()
        if retcode:
            raise sp.CalledProcessError(retcode, process.args, output=output)
        return output

def sp_test(args, timeout=None, input=None, universal_newlines=False):
    """runs test in subprocess"""
    
    try:
        output = check_io(args, timeout=timeout, input=input,
                          universal_newlines=universal_newlines)

    except sp.TimeoutExpired as e:
        return ("timeout",e)

    except sp.CalledProcessError as e:
        return ("retcode",e)

    except Exception as e:
        return ("exception",e)

    else:
        return (None,output)

def mp_test(target, args=(), kwargs={}, timeout=None):
    """runs test in multiprocess. (must be picklable)"""
        
    r, w = mp.Pipe(duplex=False)

    def wrap(target=None, args=(), kwargs={}):
        res=target(*args, **kwargs)
        try:
            w.send(res)
        except:
            os.kill(os.getpid(),signal.SIGTERM)
            
    p = mp.Process(target=wrap, args=[target, args, kwargs])
    p.start()
    p.join(timeout) # Can't timeout pipe recv, so risking block on send.
    if p.is_alive():
        p.terminate()
        return ("timeout","Timeout limit was "+str(timeout)+" seconds")
    if p.exitcode:
        return ("signaled","Exited following signal -"+str(p.exitcode))
    return (None,r.recv())

def res_code(name, res="", output=None, ratio=1):
    if output:
        print (output)
    print("\t".join(["result_code",name, res, str(ratio)]))

def filelist_test(filename, required=(), permitted=(), forbidden=()):
    tf = tarfile.open(name=filename)
    names = tf.getnames()
    tf.close()
    missing = [n for n in required if not n in names]
    tmpper = [n for n in names for pattern in permitted if fnmatch.fnmatch(n,pattern)]
    tmpfor = [n for n in names for pattern in forbidden if fnmatch.fnmatch(n,pattern)]
    extra = [n for n in names if n not in required and (n in tmpfor or n not in tmpper)]
    for n in missing:
        res_code("missing_file",n,"Missing required file: "+n)
    for n in extra:
        res_code("extra_file",n,"Extra file submitted: "+n)

def read_res_codes(file=None):
    res = []
    for line in file:
        rec = line.split("\t")
        if len(rec)==4 and rec[0]=="result_code":
            rec[3]=float(rec[3])
            res.append(rec)
    return res

def long_sequence_compare(name, expected, actual, contextpreview=20, res="wrong"):
    if expected==actual:
        return

    sm = SequenceMatcher(a=expected, b=actual)
    diffs = sm.get_opcodes()
    dstart = 0
    if diffs[0][0]=='equal':
        dstart = diffs[0][2] - contextpreview
        if dstart<0:
            dstart=0
    res_code(name, res, "\n".join(["Showing output from byte "+str(dstart),
                                   "expected: "+str(expected[dstart:]),
                                   "actual:   "+str(actual[dstart:])]))
   
