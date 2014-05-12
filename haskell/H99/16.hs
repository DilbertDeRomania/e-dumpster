-- Problem 16:  Drop every N'th element from a list.

module Problem16 (dropEvery) where

dropEvery :: [a] -> Int -> [a]

dropEvery xs n = dropEvery' xs n 1

{- dropEvery' is not tail recursive :-( -}
dropEvery' (x:xs) n i =
	if n == i then dropEvery' xs n 1
	else x : dropEvery' xs n (i + 1)

dropEvery' [] _ _ = []


{- inefficient because of new list created by zip and mod operator?

dropEvery xs n = [x | (x,i) <- zip xs [1..], i `mod` n /= 0]

-}


{- inefficient because of ++ 

dropEvery xs n = fst $ foldl f ([], 1) xs where
	f (ys, i) x = 
		if i == n then (ys, 1)
		else (ys ++ [x], i + 1)
-}
