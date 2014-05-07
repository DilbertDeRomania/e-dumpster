-- Problem 3: Find the K'th element of a list. The first element in the list is number 1. 

module Problem3 (elemAt) where

elemAt :: (Num n, Ord n) => n -> [a] -> Maybe a

elemAt _ [] = Nothing
elemAt 1 (x:xs) = Just x
elemAt n (x:xs) =
    if n <= 0 
    then error "invalid index"
    else elemAt (n - 1) xs
