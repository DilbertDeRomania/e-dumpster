-- Problem 8: Eliminate consecutive duplicates of list elements.

module Problem8 (myCompress) where

myCompress :: Eq a => [a] -> [a]

myCompress (x:ys@(y:_)) =
	if x == y
	then myCompress ys
	else [x] ++ myCompress ys

myCompress xs = xs
