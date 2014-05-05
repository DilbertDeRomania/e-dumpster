#-------------------------------------------------------------------------------
# Name:        problem208
# Purpose:
#
# Author:      adrian
#
# Created:     01/03/2013
# Copyright:   (c) adrian 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import scipy.misc


def main():

    s = 0
    for i in xrange(0, 15) :
        c = scipy.misc.comb(14, i, 1)
        s += c
        print i, c

    #s *= 2
    print s


if __name__ == '__main__':
    main()
