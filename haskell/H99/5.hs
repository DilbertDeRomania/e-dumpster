-- Problem 5: Reverse a list. 

module Problem5 (myReverse) where

myReverse :: [a] -> [a]
myReverse x = myReverse' x []


myReverse' :: [a] -> [a] -> [a]
myReverse' [] a = a
myReverse' (x:xs) a = myReverse' xs (x:a)
