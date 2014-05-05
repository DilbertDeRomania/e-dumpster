#-------------------------------------------------------------------------------
# Name:        problem54
# Purpose:
#
# Author:      Adrian
#
# Created:     12/02/2013
# Copyright:   (c) Adrian 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python
from collections import defaultdict

CARD_VALUES = {
    'A' : 14, # Ace is only high for this problem. It can't be 1 for wheel straight Ace -> 5
    'K' : 13,
    'Q' : 12,
    'J' : 11,
    'T' : 10
}


STRAIGHT_FLUSH = 8
FOUR_OFAKIND   = 7
FULL_HOUSE     = 6
FLUSH          = 5
STRAIGHT       = 4
THREE_OFAKIND  = 3
TWO_PAIR       = 2
ONE_PAIR       = 1
HIGH_CARD      = 0


def getCardVal(c) :
    if '2' <= c <= '9' :
        return ord(c) - ord('0')
    else :
        return CARD_VALUES[c]


def evalHand(h) :
    cardMap  = defaultdict(int)
    suitMap = {}

    for c in h :
        cardVal = getCardVal(c[0])
        cardMap[cardVal] += 1

        suitMap[c[1]] = True

    mapLen   = len(cardMap)
    handType = HIGH_CARD

    if 5  == mapLen :
        handType = HIGH_CARD
    elif 4 == mapLen :
        handType = ONE_PAIR
    elif 3 == mapLen :
        if max(cardMap) == 3 :
            handType = THREE_OFAKIND
        else :
            handType = TWO_PAIR
    elif 2 == mapLen :
        if max(cardMap) == 4 :
            handType = FOUR_OFAKIND
        else :
            handType = FULL_HOUSE

    if handType == HIGH_CARD :
        # at this point we have high card, straigts, flush, straight/royal flush
        flush    = (len(suitMap) == 1)
        straight = ((max(cardMap) - min(cardMap)) == 4)

        if flush :
            if straight :
                handType = STRAIGHT_FLUSH
            else :
                handType = FLUSH
        elif straight :
            handType = STRAIGHT

    handValue = []
    for k, v in cardMap.iteritems() :
        handValue.append((v, k))

    handValue.sort(reverse=True)
    res = []
    res.append(handType)
    res = res  + handValue

    return res


def main():
    fileName = "poker.txt"
    f = open(fileName,"r")

    res = 0

    for line in f.readlines() :
        hands = line.split()
        h1 = hands[:5]
        h2 = hands[5:]

        v1 = evalHand(h1)
        v2 = evalHand(h2)

        if v1 > v2 :
            res += 1

    f.close()

    print res

if __name__ == '__main__':
    main()
