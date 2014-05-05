#-------------------------------------------------------------------------------
# Name:        problem53
# Purpose:
#
# Author:      Adrian
#
# Created:     10/02/2013
# Copyright:   (c) Adrian 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python
import scipy.misc


def main():
    r = 0

    for n in range(23,101) :
        for k in range(0, n + 1) :
            c = scipy.misc.comb(n, k, 1)
            if c > 1000000 :
                r += 1

    print r

if __name__ == '__main__':
    main()
