#-------------------------------------------------------------------------------
# Name:        problem36
# Purpose:
#
# Author:      adrian
#
# Created:     01/03/2013
# Copyright:   (c) adrian 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import time

def isPali(n, binary=False) :
    if binary :
        s = bin(n)[2:]
    else :
        s = str(n)

    return s == s[::-1]


def main():
    s = sum(n for n in xrange(1, 1000000) if isPali(n) and isPali(n, binary=True))
    print s


if __name__ == '__main__':
    start_time = time.time()
    main()
    print time.time() - start_time, "seconds"
