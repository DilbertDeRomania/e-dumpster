#-------------------------------------------------------------------------------
# Name:        problem22
# Purpose:
#
# Author:      adrian
#
# Created:     31/01/2013
# Copyright:   (c) adrian 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    f = open("names.txt","r")
    inputString = f.read()
    f.close()

    names = [n.strip('"') for n in inputString.split(",")]
    names.sort()

    i = 1
    r = 0
    d = ord('A') - 1

    for n in names :
        s = sum(ord(ch) - d for ch in n)
        p = i * s
        r += p
        i += 1

    print r

if __name__ == '__main__':
    main()
