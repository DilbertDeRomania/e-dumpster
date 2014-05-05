#-------------------------------------------------------------------------------
# Name:        problem34
# Purpose:
#
# Author:      Adrian
#
# Created:     27/02/2013
# Copyright:   (c) Adrian 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python
import scipy.misc
import time

facts = {}
def preCalcFact() :
    for i in range(0, 10) :
        facts[i] = scipy.misc.factorial(i, exact=1)


def factSum(x) :
    s = str(x)
    r = 0
    for c in s :
        r += facts[int(c)]

    return r


def main():
##    nineFact = scipy.misc.factorial(9, exact=1)
##    n = 1
##    while True :
##        f = nineFact * n
##        x = int("9" * n)
##        n += 1
##
##        if x > f :
##            print n - 1, x, f
##            break
## for n=7 9999999 > 7 * 9!

    preCalcFact()

    s = 0
    for n in range(10, 10000000) :
        if n == factSum(n) :
            s += n
            #print n

    print s


if __name__ == '__main__':
    start_time = time.time()
    main()
    print time.time() - start_time, "seconds"
