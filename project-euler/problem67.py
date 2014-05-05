#-------------------------------------------------------------------------------
# Name:        problem67
# Purpose:
#
# Author:      Adrian
#
# Created:     25/01/2013
# Copyright:   (c) Adrian 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

class TMatrix :
    def __init__(self, fileName) :
        self.tm    = []
        self.lines = 0

        f = open(fileName,"r")
        inputString = f.read()
        f.close()

        self.lines = inputString.count('\n')
        self.tm    = [int(w) for w in inputString.split()]


    def getElemAt(self, line, col) :
        if col > line :
            raise Exception("invalid column")

        beginLine = (line * (line + 1)) / 2
        return self.tm[beginLine + col]

    def setElemAt(self, line, col, val) :
        if col > line :
            raise Exception("invalid column")

        beginLine = (line * (line + 1)) / 2
        self.tm[beginLine + col] = val

    def __getitem__(self, pos) :
        i, j = pos
        return self.getElemAt(i, j)

    def __setitem__(self, pos, val) :
        i, j = pos
        return self.setElemAt(i, j, val)


def main():
    tm = TMatrix("triangle.txt")

    crntLine = tm.lines - 2

    while True :
        for i in range(0, crntLine + 1) :
            newVal = max(tm[crntLine + 1, i], tm[crntLine + 1, i + 1])
            newVal += tm[crntLine, i]
            tm[crntLine, i] = newVal

        crntLine = crntLine - 1
        if crntLine < 0 :
            break

    print tm[0, 0]

if __name__ == '__main__':
    main()
