-- Problem 15:  Replicate the elements of a list a given number of times.

module Problem15 (myReplicate) where

myReplicate :: Int -> [a] -> [a]

myReplicate n =	foldr (\x acc -> (replicate n x) ++ acc) []
