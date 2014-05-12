-- Problem 11 + 13: Modified run-length encoding.
-- Modify the result of problem 10 in such a way that if an element
-- has no duplicates it is simply copied into the result list.
-- Only elements with duplicates are transferred as (N E) lists.

-- EE = Encoded Element
-- M = multiple, S = single
module Problem11 (myEncode2, EE) where

data EE a = M Int a | S a deriving Show

myEncode2 :: Eq a => [a] -> [EE a]

myEncode2 = foldr e [] where
	e x [] = [S x]

	e x (acc@((S a):as)) =
		if x == a
		then (M 2 a) : as
		else S x : acc

	e x (acc@((M n a):as)) =
		if x == a
		then (M (n + 1) a) : as
		else S x : acc
