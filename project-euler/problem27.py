#-------------------------------------------------------------------------------
# Name:        problem27
# Purpose:
#
# Author:      Adrian
#
# Created:     04/03/2013
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


def main():
    primes = computePrimes(100000)
    primes1000 = computePrimes(999)

    resProduct = None
    maxCount   = 0

    for b in primes1000 :
        print b
        for a in xrange(-999, 1000) :
            n = 0

            # generate and count primes sequence length
            while True :
                x = n * n + a * n + b
                if x < 1 or not x in primes :
                    break
                n += 1

            if n > maxCount :
                maxCount = n
                resProduct = a * b

    print maxCount, resProduct


if __name__ == '__main__':
    main()
