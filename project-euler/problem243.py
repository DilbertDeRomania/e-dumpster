#-------------------------------------------------------------------------------
# Name:        problem243
# Purpose:
#
# Author:      Adrian
#
# Created:     05/03/2013
# Copyright:   (c) Adrian 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

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

primes = computePrimes(100000)



def gcd(a, b) :
    while b != 0 :
        t = b
        b = a % t
        a = t

    return a


def resilience0(d) :
    if d in primes :
        return d - 1

    r = 1

    #for i in xrange(2, d) :
    i = 2
    while i < d :
        if gcd(i, d) == 1:
            r += 1
        i += 1

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


def resilience(d) :
    r = 1
    ps = []
    for p in primes :
        if p < d :
            ps.append(p)
        else : break

    ps

    return r


def main1() :
##    d = 3 * 5 * 7 * 11 * 13 * 17 * 19 * 23 * 29
##    r = resilience0(d)
##
##    print d, float(r) / (d - 1)
##    return

    d = 265060
    c = 0
    m = 1.0

    while True :
        r = resilience1(d)

        # compare r / (d - 1) to 15499 / 94744
        #if r != d - 1 and r * 94744 < (d - 1) * 15499 :
        #    break

        r = float(r) / (d - 1)
        if r < m :
            m = r
            print d, m

        d += 1
        c += 1

        if c % 1000 == 0:
            print "#", c

    print "Result=", d



def main() :
    d = 2*3*5*7*11*13*17*19*23*2
    print d

    r = resilience0(d)
    print float(r) / (d - 1)
    return

##    d = 2 * 3 * 5 * 7 * 13 * 17 * 43 * 47
##    r = float(resilience(d)) / (d - 1)
##    print d, r

    d = 1
    primes = computePrimes(100)
    for p in primes :
        d *= p
        print p, d
##        d = 2 * 3 * 5 * 7 * 11 * p
##        r = resilience(d)
##        r = float(r) / (d - 1)
##        print d, r


if __name__ == '__main__':
    main()

# just use euler's totient formula.
# http://en.wikipedia.org/wiki/Euler's_totient_function
