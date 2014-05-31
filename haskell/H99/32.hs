-- Problem 32: Determine the greatest common divisor of two positive integer numbers. Use Euclid's algorithm.
module Problem32 (mygcd) where

mygcd :: Int -> Int -> Int
mygcd n 1 = 1
mygcd 1 n = 1
mygcd m n = if m > n then gcd (m -n) m else gcd m (n - m)
