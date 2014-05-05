#-------------------------------------------------------------------------------
# Name:        problem48
# Purpose:
#
# Author:      adrian
#
# Created:     30/01/2013
# Copyright:   (c) adrian 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    s = 0
    for i in range(1, 1001) :
        s += (i ** i)

    ss = str(s)
    print ss[-10:]

if __name__ == '__main__':
    main()
