#-------------------------------------------------------------------------------
# Name:        problem81
# Purpose:
#
# Author:      Adrian
#
# Created:     25/01/2013
# Copyright:   (c) Adrian 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

def readData(fileName) :
    f = open(fileName,"r")

    m = []
    for line in f.readlines() :
        m.append([int(w) for w in line.split(",")])

    f.close()
    return m


def update(m, i, j) :
    if i == 0 :
        if j > 0:
            m[i][j] += m[i][j - 1]
    else :
        if j == 0 :
            m[i][j] += m[i - 1][j]
        else :
            m[i][j] += min(m[i][j - 1], m[i - 1][j])


def main():
    m = readData("matrix81.txt")
    n = len(m)

    for i in range(0, n) :
        for j in range(0, i + 1) :
            update(m, i - j, j)

    for i in range(1, n) :
        for j in range(0, n - i) :
            update(m, i + j, n - j - 1)

    print m[n - 1][n - 1]


if __name__ == '__main__':
    main()
