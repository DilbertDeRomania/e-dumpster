#-------------------------------------------------------------------------------
# Name:        problem24
# Purpose:
#
# Author:      adrian
#
# Created:     31/01/2013
# Copyright:   (c) adrian 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import itertools


def main():
    perms = itertools.permutations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    i = 0

    for p in perms :
        i += 1

        if i == 1000000 :
            print p
            break


if __name__ == '__main__':
    main()
