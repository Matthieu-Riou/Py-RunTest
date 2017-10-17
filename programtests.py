#! /usr/bin/python -u

import sys, doctest, string, StringIO, dis, os, time, select
from colors import colorString
import argparse as ap
import subprocess as sp



def check_usage(f, name):
    backup_stdout = sys.stdout
    fake_stdout = StringIO.StringIO()
    sys.stdout = fake_stdout
    dis.dis(f)
    sys.stdout = backup_stdout
    matchName = False
    lines = fake_stdout.getvalue().split("\n")
    lines = [l.split() for l in lines]
    for l in lines:
        i = l.index('LOAD_GLOBAL') if 'LOAD_GLOBAL' in l else -1 
        if i != -1:
            if l[i+2] == ('(%s)' % name):
                return True
    return False


def prompt_release_stdout(fakestdout):
    # Function that prompts the user to realease content of fakestdout, return True if the user decides to pass the current function
    while True:
        action = raw_input("Print failed tests? [F(irst)/a(ll)/o(ne by one)/n(one)/p(ass this function)] ")
        action = action.lower()
        if action.lower() == 'p':
            return True
        elif action == '' or action == 'f':
            print fakestdout.getvalue().split("*" * 70)[1]
            break
        elif action == 'a':
            print fakestdout.getvalue()
            break
        elif action == 'o':
            for s in fakestdout.getvalue().split("*" * 70)[1:-1]:
                print s                
                print
                action = raw_input("Next error? [Y(es)/n(o)] ")
                action = action.lower()
                if action == 'n':
                        break
            break
        elif action.lower() == 'n':
            break

    return False




def read_timeout(f, n):
    r, w, e = select.select([ f ], [], [], 0)
    time.sleep(0.5)
    if r:
        return os.read(f.fileno(), n)
    return ""



def write_timeout(f, content):
    while True:
        r, w, e = select.select([ f ], [], [], 0)
        time.sleep(0.5)
        if w:
            f.write(content)
            break


def exec_wrap(fileName, testcaseFile):

    p = sp.Popen(["unbuffer", "python", fileName], stdin=sp.PIPE, stdout=sp.PIPE, stderr=sp.PIPE, bufsize=-1)


    with open(testcaseFile) as f:
        out = ""
        while True:
            line = f.readline()
            if not line:
                break
            mode, content = line.split(";")[:2]
            if mode == "OUT-NONL":
                out += content
            elif mode == "OUT-NL":
                out += content + "\n"
            elif mode == "IN-NL":
                p.stdin.write(content + "\n")
                out += content + "\n"
        print out,


def test_ex1():
    '''
    >>> exec_wrap("ex1.py", "ex1.py.io")
    Input op: *
    Input lhs: 3
    Input rhs: 4
    12.0
    '''


if __name__ == '__main__':

    p = ap.ArgumentParser()
    p.add_argument("-f", "--function", default = '')
    p.add_argument("-a", "--all", action='store_true')
    p.add_argument("-l", "--list", action='store_true')
    p.add_argument("--program", default = "ex1.py")
    args = p.parse_args()

    fakestdout = StringIO.StringIO() # Fake file object for Stdout interception
    stdout = sys.stdout # Backup stdout


    targets = [
        ("test_ex1", test_ex1)
    ]


    # Override function name from cmd line argument
    if args.function != "":
        findtarget = [t for t in targets if t[0] == args.function]
        if len(findtarget) == 0:
            print "Error: Target function [%s] not found." % args.function
            sys.exit(1)
        else:
            print "Override: testing only [%s]" % args.function
            targets = findtarget


    print "=" * 79
    __test__ = {} # Functions mapped in __test__ are actually tested by doctest
    for fname, f in targets:
        __test__[fname] = f

        # Intercept Stdout
        sys.stdout = fakestdout
        res = doctest.testmod()
        # Restore Stdout
        sys.stdout = stdout
        test = string.ljust("{}".format(fname), 24, ' ') + " {}"

        if res.failed == 0:
            print colorString("green", test.format(res))
        else:
            if not args.all:
                print "=" * 79

            color = "yellow" if res.failed < res.attempted else "red"
            print colorString(color, test.format(res))

            if not args.all:
                print
                notPassing = prompt_release_stdout(fakestdout)
                if not notPassing and not args.list:
                    break

                if args.list and not notPassing:
                    print "=" * 79
                    action = raw_input("Continue? [Y(es)/n(o)] ")
                    action = action.lower()

                    if action == 'n':
                        break

        fakestdout.close()
        fakestdout = StringIO.StringIO()
        del __test__[fname]


    print "=" * 79


