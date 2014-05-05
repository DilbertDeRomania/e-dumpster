#-------------------------------------------------------------------------------
# Name:        problem205
# Purpose:
#
# Author:      Adrian
#
# Created:     21/01/2013
# Copyright:   (c) Adrian 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python
import random
import threading
from decimal import Decimal


# This monte carlo simulation does not work in decent timeout because we need
# 7 digit preciosion. Try other method.
# It seems to give 3 digit precision: 0.573...

class MonteCarloThread(threading.Thread) :
    def __init__(self, noIter) :
              threading.Thread.__init__(self)
              self.noIter = noIter
              self.p      = 0

    def run(self):
        it      = self.noIter
        self.p  = 0

        while it > 0 :
            s1 = sum(random.randint(1, 4) for r in range(1, 10))
            s2 = sum(random.randint(1, 6) for r in range(1, 7))

            if s1 > s2 :
                self.p += 1

            it -= 1


def main():
    numberOfIterations = 15000000
    t1 = MonteCarloThread(numberOfIterations)
    t2 = MonteCarloThread(numberOfIterations)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    p = t1.p + t2.p
    print p, 2 * numberOfIterations, Decimal(p) / Decimal(2 * numberOfIterations)

#################################################################################

if __name__ == '__main__':
    main()
