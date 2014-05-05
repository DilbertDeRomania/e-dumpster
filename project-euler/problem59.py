#-------------------------------------------------------------------------------
# Name:        problem59
# Purpose:
#
# Author:      Adrian
#
# Created:     23/02/2013
# Copyright:   (c) Adrian 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

from collections import defaultdict


def isValidChar(ch) :
    if ch < 32 :
        return False

    return True


def uncrypt(inputNumbers, key) :
    numbers = inputNumbers[:]

    keys = [ord(key[0]), ord(key[1]), ord(key[2])]
    i = 0;

    for i in range(0, len(numbers)) :
        k = keys[i % 3]
        if k != 0 :
            numbers[i] = numbers[i] ^ k
            if not isValidChar(numbers[i]) :
                return ""
        else :
            numbers[i] = ord('_')


    return "".join([chr(n) for n in numbers])


def main():
    f = open("cipher_59.txt","r")
    inputString = f.read()
    f.close()

    numbers = [int(n) for n in inputString.split(",")]

    for k1 in range(ord('a'), ord('z') + 1) :
        for k2 in range(ord('a'), ord('z') + 1) :
            for k3 in range(ord('a'), ord('z') + 1) :
                key = chr(k1) + chr(k2) + chr(k3)
                s = uncrypt(numbers, key)

                if s.find(" the ") != -1 :
                    print key, ":\n", s, "\n"
                    print sum([ord(c) for c in s])
                    return

if __name__ == '__main__':
    main()
