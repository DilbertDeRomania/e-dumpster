-- Problem 6: Find out whether a list is a palindrome. A palindrome can be read forward or backward; e.g. (x a m a x).

module Problem6 (isPalindrome) where

isPalindrome :: Eq a => [a] -> Bool
isPalindrome x = x == myReverse x

myReverse :: [a] -> [a]
myReverse x = myReverse' x []


myReverse' :: [a] -> [a] -> [a]
myReverse' [] a = a
myReverse' (x:xs) a = myReverse' xs (x:a)
