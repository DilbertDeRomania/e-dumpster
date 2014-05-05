#-------------------------------------------------------------------------------
# Name:        problem42
# Purpose:
#
# Author:      Adrian
#
# Created:     25/02/2013
# Copyright:   (c) Adrian 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

import math


def wordVal(w) :
    s = 0
    for c in w :
        s += ord(c) - ord('A') + 1

    return s


def isTriangleWord(w):
    v = wordVal(w)
    d = math.sqrt(1 + 8 * v)

    if int(d) != d :
        return False

    n = (d - 1) / 2
    return n == int(n)


def main():
    f = open("words_42.txt","r")
    inputString = f.read()
    f.close()

    words = [n.strip('"') for n in inputString.split(",")]

    c = 0
    for w in words:
        if isTriangleWord(w) :
            c += 1

    print c


if __name__ == '__main__':
    main()
