#-------------------------------------------------------------------------------
# Name:        problem28
# Purpose:
#
# Author:      Adrian
#
# Created:     10/02/2013
# Copyright:   (c) Adrian 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python


def main():
    n  = 1
    u  = 1
    d1 = 1
    d2 = 1
    nMax = 1001

    while True :
        rd = u + n + 1
        ld = u + 2 * n + 2
        lt = u + 3 * n + 3
        rt = u + 4 * n + 4

        d1 += rd
        d2 += ld
        d1 += lt
        d2 += rt
        u = rt

        #print "----- ", n
        #print rd, ld, lt, rt

        n += 2
        if n == nMax :
            break

    print d1 + d2 - 1 # the middle 1 is added only once!!!

if __name__ == '__main__':
    main()
