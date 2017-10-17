#! /usr/bin/python -u


op = raw_input("Input op: ")
lhs = float(raw_input("Input lhs: "))
rhs = float(raw_input("Input rhs: "))

if op == "*":
    print lhs * rhs
elif op == "/":
    if rhs != 0:
        print lhs / rhs
    else:
        print "Error: Want to divide by zero"
else:
    print "Error: invalid operation"

