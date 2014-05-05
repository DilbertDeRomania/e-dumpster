#-------------------------------------------------------------------------------
# Name:        problem17
# Purpose:
#
# Author:      Adrian
#
# Created:     06/02/2013
# Copyright:   (c) Adrian 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

numbersDict = {
    0 : "zero",
    1 : "one",
    2 : "two",
    3 : "three",
    4 : "four",
    5 : "five",
    6 : "six",
    7 : "seven",
    8 : "eight",
    9 : "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
    20: "twenty",
    30: "thirty",
    40: "forty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety"
}


def spellNumber(n) :
    if n < 0 :
        raise Exception("negative number")

    if n == 0 :
        return "zero"

    t = n / 1000
    n %= 1000

    if t > 10 :
        raise Exception("number bigger than 10k")

    res = ""

    if t > 0 :
        res += numbersDict[t] + "thousand"

    h = n / 100
    n %= 100

    if h > 0 :
        res += numbersDict[h] + "hundred"

        if n > 0 :
            res += "and"

    d = n / 10

    if d > 0 :
        if d > 1 :
            res += numbersDict[d * 10]
            n %= 10

            if n > 0 :
                res += numbersDict[n]
        else :
            res += numbersDict[n]
    elif n > 0 :
        res += numbersDict[n]

    return res

def main():
    r = ""

    for n in range (1, 1001) :
        w = spellNumber(n)
        r += w

    print len(r)

if __name__ == '__main__':
    main()
