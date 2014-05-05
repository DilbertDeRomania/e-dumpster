#-------------------------------------------------------------------------------
# Name:        problem205 second try
# Purpose:
#
# Author:      Adrian
#
# Created:     24/01/2013
# Copyright:   (c) Adrian 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python
import itertools
from collections import defaultdict
from decimal import Decimal


def computeProbabilities(diceNumber, diceFaces) :
    allcomb = list(itertools.product(*[range(1, diceFaces + 1) for d in range(1, diceNumber + 1)]))
    freqs   = defaultdict(float)

    for s in [sum(c) for c in allcomb] :
        freqs[s] += 1

    evtNumber = diceFaces ** diceNumber
    for k in freqs :
        freqs[k] /= float(evtNumber)

    return freqs


def main() :
    diceOneNumber = 9
    diceOneFaces  = 4
    diceTwoNumber = 6
    diceTwoFaces  = 6

    f1 = computeProbabilities(diceOneNumber, diceOneFaces)
    f2 = computeProbabilities(diceTwoNumber, diceTwoFaces)

    win = 0

    for k1, p1 in f1.iteritems():
        p = sum(p2 for k2, p2 in f2.iteritems() if k1 > k2)
        win += p * p1

    print round(win, 7)

##    tie = 0
##    for k1, p1 in f1.iteritems():
##        p = sum(p2 for k2, p2 in f2.iteritems() if k1 == k2)
##        tie += p * p1
##
##    loss = 0
##    for k1, p1 in f1.iteritems():
##        p = sum(p2 for k2, p2 in f2.iteritems() if k1 < k2)
##        loss += p * p1
##
##    print win, tie, loss, win + tie + loss

if __name__ == '__main__':
    main()
