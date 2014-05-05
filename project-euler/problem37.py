#-------------------------------------------------------------------------------
# Name:        problem37
# Purpose:
#
# Author:      adrian
#
# Created:     28/02/2013
# Copyright:   (c) adrian 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import time


def computePrimes(lt) :
    def filterTruncable(n) :
        if n < 100 : #23 is truncable
            return True

        s = str(n)
        if s[-1:] == "1" :
            return False

        for c in s :
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

    primes=[x for x in z if x and filterTruncable(x)]
    return primes


def main():
    primes = computePrimes(1000000)

    def isTruncablePrime(p) :
        if p < 10 :
            return False # 2, 3, 5, 7 are not truncable

        s = str(p)

        while len(s) > 0 :
            if not int(s) in primes :
                return False
            s = s[1:]

        s = str(p)
        while len(s) > 0 :
            if not int(s) in primes :
                return False
            s = s[:-1]

        print p
        return True

    i = 0
    s = 0

    for p in primes :
        if isTruncablePrime(p) :
            i += 1
            s += p
            if i == 11 :
                break

    print i, s


if __name__ == '__main__':
    start_time = time.time()
    main()
    print time.time() - start_time, "seconds"
