-- Problem 17:  Split a list into two parts; the length of the first part is given.

module Problem17 (mySplit) where

mySplit :: [a] -> Int -> ([a], [a])

{- hand made version -}
mySplit [] _ = ([], [])
mySplit xs 0 = ([], xs)

mySplit (x:xs) n
	| n >= 0 =
		let (lft,rght) = mySplit xs (n - 1)
		in (x:lft, rght)
	| otherwise = error "invalid argument"
