-- Problem 19:  Extract a slice from a list.

module Problem19 (myRotate) where

myRotate :: [a] -> Int -> [a]

myRotate xs n
	| abs n >= abs len = myRotate xs (n `mod` len)
	| n == 0 = xs
	| n > 0 = drop n xs ++ take n xs
	| otherwise = myRotate xs (len + n)
	where len = length xs
