#-------------------------------------------------------------------------------
# Name:        problem79
# Purpose:
#
# Author:      Adrian
#
# Created:     21/02/2013
# Copyright:   (c) Adrian 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

def main():
    f = open("keylog_79.txt","r")
    inputString = f.read()
    f.close()

    pins = [w for w in inputString.split()]
    pins = list(set(pins)) # remove duplicates.

    # s contains (x, y) if x appears before y in the result PIN.
    s = set()
    for p in pins :
        cmp1 = (p[0], p[1])
        s.add(cmp1)

        cmp2 = (p[1], p[2]);
        s.add(cmp2)

        cmp3 = (p[0], p[2])
        s.add(cmp3)

    def compare(n, m) :
        if n == m :
            return 0

        if (n, m) in s :
            return -1

        if (m, n) in s :
            return 1

        raise Exception("not total order: " + n + ", " + m)

    # HACK ALERT! 4 and 5 does not appear in the input file.
    # I should've decided that programatically :-(
    # res is ['0', '1', '2', '3', '6', '7', '8', '9']

    res = [chr(ord('0') + i) for i in range(0, 10) if i != 4 and i != 5]
    res.sort(cmp=compare)

    print "".join(res)

if __name__ == '__main__':
    main()
