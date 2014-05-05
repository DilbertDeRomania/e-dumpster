#-------------------------------------------------------------------------------
# Name:        problem10
# Purpose:
#
# Author:      Adrian
#
# Created:     20/01/2013
# Copyright:   (c) Adrian 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python
import math
import time

def secondTry() :
    pass


def firstTry() :
    # It took: 1316.87 seconds ~22 minutes
    bound = 2000000

    primes = [2 , 3]
    def isPrime (c) :
        sqrc = math.sqrt(c)
        firstFactor = next((pf for pf in primes if (pf <= sqrc) and (c % pf == 0)) , 0)
        return firstFactor == 0

    i = 5
    n = 5
    while n < bound :
        if isPrime(n) :
            primes.append(n)
        n += 2

        i += 1
        if i % 50000 == 0:
            print "*",

    print sum(primes)


def main() :
    firstTry()


if __name__ == '__main__':
    startTime = time.time()

    main()

    print "Time: ", (time.time() - startTime), " seconds"
