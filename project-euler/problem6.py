#-------------------------------------------------------------------------------
# Name:        problem6
# Purpose:
#
# Author:      Adrian
#
# Created:     25/01/2013
# Copyright:   (c) Adrian 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

def main():
    n = 100

    s1 = 0

    for i in range (1, n + 1) :
        s1 += i * i

    s2 = sum(range(1, n + 1)) ** 2

    print s2 - s1

if __name__ == '__main__':
    main()
