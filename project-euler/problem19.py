#-------------------------------------------------------------------------------
# Name:        problem19
# Purpose:
#
# Author:      Adrian
#
# Created:     31/01/2013
# Copyright:   (c) Adrian 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python
import datetime


def main():
    s = 0

    for y in range(1901, 2001) :
        for m in range(1, 13) :
            d = datetime.datetime(y, m, 1)
            if d.weekday() == 6 :
                s += 1

    print s

if __name__ == '__main__':
    main()
