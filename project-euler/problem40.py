#-------------------------------------------------------------------------------
# Name:        problem40
# Purpose:
#
# Author:      Adrian
#
# Created:     26/02/2013
# Copyright:   (c) Adrian 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python


# Brute stupid force.
def main():
    s = ""
    for i in range(0, 200000) :
        s += str(i)

    print s[1], s[10], s[100], s[1000], s[10000], s[100000], s[1000000]
    print int(s[1]) * int(s[10]) * int(s[100]) * int(s[1000]) * int(s[10000]) * int(s[100000]) * int(s[1000000])


if __name__ == '__main__':
    main()
