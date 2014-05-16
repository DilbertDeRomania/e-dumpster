-- Problem 24: Lotto- draw N different random numbers from the set 1..M.
module Problem24_25 (myLotto, myPermutation) where
import System.Random

myLotto :: Int -> Int -> IO [Int]
myLotto n m = myRemoveNRandom [1..m] n

myRemoveNRandom :: [a] -> Int -> IO [a]
myRemoveNRandom xs 0 = return []

myRemoveNRandom xs n = do
	(x, ys) <- myRemoveRandomElem xs
	zs <- myRemoveNRandom ys (n - 1)
	return $ x : zs

myRemoveRandomElem :: [a] -> IO (a, [a])
myRemoveRandomElem xs = do
	k <- randomRIO (0, length xs - 1)
	return $ myRemoveElem xs k

myRemoveElem :: [a] -> Int -> (a, [a])
myRemoveElem xs k =
	let
		s = drop k xs
		r = (tail s)
		l = (take k xs)
	in (head s, l ++ r)

-- Problem 25: Generate a random permutation of the elements of a list.
myPermutation :: [a] -> IO [a]
myPermutation xs = myRemoveNRandom xs (length xs)
