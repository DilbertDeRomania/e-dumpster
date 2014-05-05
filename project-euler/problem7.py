#-------------------------------------------------------------------------------
# Name:        problem7
# Purpose:
#
# Author:      Adrian
#
# Created:     20/01/2013
# Copyright:   (c) Adrian 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python
import time

def main():
    startTime = time.time()

    lt=150000
    z=range(lt)
    z[0]=z[1]=False
    for val in z:
        if not val:
            continue
        for i in range(val*2,lt,val):
            z[i]=False

    primes=[x for x in z if x]

    print len(primes)
    print primes[10000]

    print time.time()-startTime, " seconds."


if __name__ == '__main__':
    main()
