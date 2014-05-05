#-------------------------------------------------------------------------------
# Name:        problem2
# Purpose:
#
# Author:      Adrian
#
# Created:     20/01/2013
# Copyright:   (c) Adrian 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

def main():
    sumFib1()

def sumFib1():
    maxFib = 4000000

    f1  = 1
    f2  = 2
    sum = 0

    while True :
        if f2 > maxFib :
            break

        if f2 % 2 == 0 :
            sum += f2

        f3 = f1 + f2
        f1 = f2
        f2 = f3

    print sum

if __name__ == '__main__':
    main()
