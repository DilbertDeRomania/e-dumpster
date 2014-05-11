-- Problem 14: Duplicate the elements of a list.

module Problem14 (myDuplicate) where


myDuplicate :: [a] -> [a]
myDuplicate = foldr d [] where
	d x acc = [x, x] ++ acc

--myDuplicate (x:xs) = x:x:myDuplicate xs
--myDuplicate [] = []
