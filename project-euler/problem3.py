#-------------------------------------------------------------------------------
# Name:        problem3
# Purpose:
#
# Author:      Adrian
#
# Created:     20/01/2013
# Copyright:   (c) Adrian 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

def thirdTry() :
    #largeNumber = 600851475143
    largeNumber = 999999

    primes = [2 , 3]
    def isPrime (c) :
        firstFactor = next((pf for pf in primes if (pf <= c / 2) and (c % pf == 0)) , 0)
        return firstFactor == 0

    def findFirstPrimeFactor(c) :
        p = 4
        while p <= c / 2:
            if isPrime(p) :
                primes.append(p)

            if (n % p == 0) :
                return p

            p += 1
        return c

    factors = []
    n       = largeNumber

    while True :
        ff = findFirstPrimeFactor(n)
        factors.append(ff)
        print ff

        n = n / ff
        if (1 == n) :
            break;

    print "Largest primes factors = ", factors[-1]


def firstTry():
    #p = 600851475143
    p = 1000000
    primeFactors = findPrimes(p / 2)
    print primeFactors


def findPrimes (n) :
    primes = [2 , 3]

    def isPrime (c) :
        firstFactor = next((pf for pf in primes if (pf <= c / 2) and (c % pf == 0)) , 0)
        return firstFactor == 0

    p = 4
    while p <= n:
        if isPrime(p) :
            primes.append(p)
        p += 1

    return primes
#########################################################################
def findLargetFactor(n) :
    fact = n / 2
    id = 0
    while (fact > 0) and (n % fact != 0) :
        fact -= 1
        id += 1

        if id % 1000000 == 0 :
            print('*'),

    return fact

def secondTry() :
    p = 600851475143
    print findLargetFactor(p)


def main() :
    thirdTry()
    print "End"

if __name__ == '__main__':
    main()
