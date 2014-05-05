#-------------------------------------------------------------------------------
# Name:        problem9
# Purpose:
#
# Author:      Adrian
#
# Created:     25/01/2013
# Copyright:   (c) Adrian 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python
import math

def main():
    for c in range(335, 998) :
        delta = 4 * c ** 2 + 8000 * c - 4000000
        if delta >= 0 :
            sq = math.sqrt(delta)
            t  = int(sq)
            if t == sq :

                b = int(500 - (2 * c - sq) / 4)
                a = 1000 - b - c

                print a, b, c, a + b + c
                print a**2, b**2, a**2 + b**2, c**2

                print a * b * c
                break

if __name__ == '__main__':
    main()
