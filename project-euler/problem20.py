#-------------------------------------------------------------------------------
# Name:        problem20
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
    fact = 1
    for i in range (1, 101) :
        fact *= i

    print sum(int(x) for x in str(fact))


if __name__ == '__main__':
    main()
