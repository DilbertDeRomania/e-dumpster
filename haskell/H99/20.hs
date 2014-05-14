-- Problem 20:  Remove the K'th element from a list.

module Problem19 (myRemove) where

myRemove ::  Int -> [a] -> (a, [a])

myRemove k xs = 
	(head right, left ++ (tail right))
	where
		left  = take (k - 1) xs
		right = drop (k - 1) xs
