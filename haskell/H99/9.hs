-- Problem 9: Pack consecutive duplicates of list elements into sublists.
-- If a list contains repeated elements they should be placed in separate sublists.

module Problem9 (myPack) where

myPack :: Eq a => [a] -> [[a]]

myPack [] = []
myPack x = 
	let (h, t) = packHead x
	in [h] ++ myPack t


packHead :: Eq a => [a] -> ([a], [a])
packHead (x:ys@(y:_)) =
	if x /= y
	then ([x], ys)
	else ([x] ++ hs, rs)
	where (hs, rs) = packHead ys

packHead [x] = ([x], [])
packHead [] = ([], [])
