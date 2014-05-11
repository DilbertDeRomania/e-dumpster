-- Problem 10: Run-length encoding of a list. Use the result of problem P09 to implement
-- the so-called run-length encoding data compression method. Consecutive duplicates of elements
-- are encoded as lists (N E) where N is the number of duplicates of the element E.

module Problem10 (myEncode) where

myEncode :: Eq a => [a] -> [(Int, a)]

myEncode = foldr e [] where
	e x [] = [(1, x)]
	e x (acc@(a:as)) =
		if x == snd a
		then (fst a + 1, snd a) : as
		else (1, x) : acc
