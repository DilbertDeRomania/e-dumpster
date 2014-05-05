#-------------------------------------------------------------------------------
# Name:        problem29
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
    r = []

    for a in range(2, 101) :
        for b in range(2, 101) :
            r.append(a ** b)

    r = sorted(set(r))
    print len(r)

if __name__ == '__main__':
    main()
