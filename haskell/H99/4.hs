-- Problem 4: Find the number of elements of a list.

module Problem4 (myLength) where

myLength :: Num n => [a] -> n
myLength x = myLength' x 0

myLength' :: Num n => [a] -> n -> n
myLength' [] n = n
myLength' (x:xs) n = myLength' xs (n + 1)
