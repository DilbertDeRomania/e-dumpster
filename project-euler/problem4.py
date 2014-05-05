#-------------------------------------------------------------------------------
# Name:        problem4
# Purpose:
#
# Author:      Adrian
#
# Created:     25/01/2013
# Copyright:   (c) Adrian 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

def nthDigit(n, d) :
    return (n % 10**(d+1)) / 10**d


def isPali(n) :
    if n > 999999 :
        raise Exception("number out of range " + str(n))

    if  n < 100000 :
        return (nthDigit(n, 0) == nthDigit(n, 4) and
                nthDigit(n, 1) == nthDigit(n, 3))
    else :
        return (nthDigit(n, 0) == nthDigit(n, 5) and
                nthDigit(n, 1) == nthDigit(n, 4) and
                nthDigit(n, 2) == nthDigit(n, 3))

def main():

    maxp = maxi = maxj = 0

    for i in reversed(range(100, 1000)) :
        for j in reversed(range(100, i + 1)) :
            p = i * j

            if isPali(p) :
                if maxp < p :
                    maxp = p
                    maxi = i
                    maxj = j

    print maxp, " = ", maxi, " * ", maxj

if __name__ == '__main__':
    main()
