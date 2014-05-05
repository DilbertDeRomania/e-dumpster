#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      adrian
#
# Created:     06/03/2013
# Copyright:   (c) adrian 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from operator import mul


def computePrimes(lt) :
    z = range(lt + 1)
    z[0] = z[1] = False

    for val in z:
        if not val:
            continue
        for i in range(val * 2, lt + 1, val):
            z[i] = False

    primes=[x for x in z if x]
    return primes


primes = computePrimes(100)


def gcd(a, b) :
    while b != 0 :
        t = b
        b = a % t
        a = t

    return a


def resilience(d) :
    if d in primes :
        return d - 1

    r = 1

    for i in xrange(2, d) :
        if gcd(i, d) == 1:
            r += 1

    return r

def resilience1(d) :
    z = range(0, d)
    r = 1
    z[0] = z[1] = False

    for val in z:
        if not val:
            continue

        if d % val == 0 :
            for i in range(val * 2, d, val):
                z[i] = False
        else : r += 1

    return r


def main() :
##    print primes
##
##    d = 2 * 3 * 5 * 7 * 11 * 13 * 17 * 19 * 97
##    r = resilience(d)
##
##    print d, r, float(r) / (d - 1)

    d = 1
    for p in primes :
        d *= p

        print "start computing", d, p
        #r = resilience(d)

        #print p, d, r, float(r) / (d - 1)

##    for i in range(2, 20) :
##        print i, resilience(i)

    #print primes

    #d = 2 * 3 * 5 * 7 * 11 * 97
    #print d
    #r = resilience1(d)

    #print d, float(r) / (d - 1)



def main0():
    #for i in range (3, 100) :
    #primes = computePrimes(5)
    d = reduce(mul, primes, 1)

    print primes, d
    r = 1

    for p in primes :
        r += (d - 1) / p

    print r

##        k = len(primes)
##
##        r = float(d - 2*k) / (d - 1)
##        print i, r

##        left = (d - 1 - 2**k) * 94744
##        right = (d -1) * 15499
##
##        #print left, right
##        if left < right :
##            print "####################"
##            break


if __name__ == '__main__':
    main()
