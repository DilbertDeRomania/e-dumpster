#-------------------------------------------------------------------------------
# Name:        problem25
# Purpose:
#
# Author:      adrian
#
# Created:     30/01/2013
# Copyright:   (c) adrian 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    f1 = 1
    f2 = 1
    i  = 3

    while True :
        f3    = f1 + f2
        f3s   = str(f3)
        f3len = len(f3s)

        if f3len == 1000:
            print i
            print f3
            break
        elif f3len > 1000 :
            print "Not found"
            break

        f1 = f2
        f2 = f3
        i  += 1

if __name__ == '__main__':
    main()
