#-------------------------------------------------------------------------------
# Name:        problem12
# Purpose:
#
# Author:      Adrian
#
# Created:     16/02/2013
# Copyright:   (c) Adrian 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

from collections import defaultdict


def getPrimes(count) :
    z = range(count)
    z[0] = z[1] = False

    for val in z:
        if not val:
            continue
        for i in range(val * 2, count , val):
            z[i] = False

    primes = [x for x in z if x]
    return primes


def triangleNumber(n) :
    return (n * (n + 1)) / 2


primes = getPrimes(10000)


def getDivs(n) :
    divs = defaultdict(int)
    for p in primes :
        if p > n / 2:
            break

        while n % p == 0  :
            divs[p] += 1
            n = n / p

            if n == 1 :
                break
    if n != 1 :
        divs[n] += 1

    return divs


def main():
    i = 1
    while True :
        n = triangleNumber(i)
        d = getDivs(n)

        # compute the number of divisors (including 1 and n itself) based on prime divisors dictionary.
        c = 1
        for v in d.itervalues() :
            c *= (v + 1)

        if c > 500:
            print "i =", i, "n =", n
            print d
            break;

        i += 1


if __name__ == '__main__':
    main()
