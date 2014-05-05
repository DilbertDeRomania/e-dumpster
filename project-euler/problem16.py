#-------------------------------------------------------------------------------
# Name:        problem16
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
    print 2**1000
    print sum(int(x) for x in str(2**1000))

if __name__ == '__main__':
    main()
