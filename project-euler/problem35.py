#-------------------------------------------------------------------------------
# Name:        problem35
# Purpose:
#
# Author:      adrian
#
# Created:     01/03/2013
# Copyright:   (c) adrian 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import time


def computePrimes(lt) :
    def filterCircular(n) :
        if n < 100 : # 17 is circular
            return True

        for c in str(n) :
            if c in "24680" :
                return False

        return True

    z = range(lt + 1)
    z[0] = z[1] = False

    for val in z:
        if not val:
            continue

        for i in range(val * 2, lt + 1, val):
            z[i] = False

    primes=[x for x in z if x and filterCircular(x)]
    return primes


def main():
    primes = computePrimes(1000000)

    def isCircularPrime(p) :
        if p < 10 :
            return True # 2, 3, 5, 7 are circular

        s = str(p)

        for i in xrange(0, len(s)) :
            s = s[1:] + s[0]
            if not int(s) in primes :
                return False

        return True

    c = 0
    for p in primes :
        if isCircularPrime(p) :
            c += 1

    print c


if __name__ == '__main__':
    start_time = time.time()
    main()
    print time.time() - start_time, "seconds"
