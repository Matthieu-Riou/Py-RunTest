#! /usr/bin/env python

import sys, doctest, string, StringIO
from colors import colorString
import argparse as ap
from exam import *

def prompt_release_stdout(fakestdout):
    # Function that prompts the user to realease content of fakestdout
    while True:
        action = raw_input("Print failed tests? [F(irst)/a(ll)/n(one)] ")
        action = action.lower()
        if action == '' or action == 'f':
            print fakestdout.getvalue().split("*" * 70)[1]
            break
        elif action == 'a':
            print fakestdout.getvalue()
            break
        elif action.lower() == 'n':
            break






if __name__ == '__main__':

    p = ap.ArgumentParser()
    p.add_argument("-f", "--function", default = '')
    args = p.parse_args()

    fakestdout = StringIO.StringIO() # Fake file object for Stdout interception
    stdout = sys.stdout # Backup stdout


    targets = [
        ("add_ints", add_ints),
        ("f1", f1),
        ("f2", f2),
        ("mul", mul),
        ("sum_evens", sum_evens),
        ("surround", surround),
        ("center_in_field", center_in_field),
        ("comment_block", comment_block),
        ("is_nucleotide", is_nucleotide),
        ("is_valid_dna_sequence", is_valid_dna_sequence),
        ("get_complement", get_complement),
        ("get_complement_sequence", get_complement_sequence),
        ("get_number_from_letter", get_number_from_letter),
        ("get_letter_from_number", get_letter_from_number),
        ("shift_mod26", shift_mod26),
        ("encrypt_char", encrypt_char),
        ("encrypt_string", encrypt_string)
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
    __test__ = {}
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
            print "=" * 79
            print colorString("red", test.format(res))
            print
            prompt_release_stdout(fakestdout)
            break

        del __test__[fname]


    print "=" * 79



