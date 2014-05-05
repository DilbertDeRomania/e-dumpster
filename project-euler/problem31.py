#-------------------------------------------------------------------------------
# Name:        problem31
# Purpose:
#
# Author:      Adrian
#
# Created:     14/03/2013
# Copyright:   (c) Adrian 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python



def main():
    coins = [200, 100, 50, 20, 10, 5, 2, 1]

    def calcComb(r, c) :
        n = 0
        for i in range(c, 8) :
            d = r - coins[i]
            if d == 0 :
                n += 1
            elif d > 0 :
                n += calcComb(d, i)

        return n

    res = calcComb(200, 0)
    print res

if __name__ == '__main__':
    main()
