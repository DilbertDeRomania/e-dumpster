#-------------------------------------------------------------------------------
# Name:        problem14
# Purpose:
#
# Author:      Adrian
#
# Created:     05/02/2013
# Copyright:   (c) Adrian 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python


def colatzLen(n) :
    res = 1

    while True :
        if n == 1 :
            return res

        if n % 2 == 0 :
            n = n / 2
        else :
            n = 3 * n + 1

        res += 1

def main():
    maxLen = 0
    c = 0

    # I think we can skip even numbers
    for i in range(1, 1000001, 2) :
        m = colatzLen(i)
        if m > maxLen :
            maxLen = m
            c = i

    print c, maxLen

if __name__ == '__main__':
    main()
