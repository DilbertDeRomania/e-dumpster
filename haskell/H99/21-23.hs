-- Problem 21: Insert an element at a given position into a list.

module Problem21_23 (myInsert1, myInsert2) where
import System.Random


-- Problem 21
myInsert1 :: [a] -> a -> Int -> [a]
myInsert1 xs x n = take (n - 1) xs ++ [x] ++ drop (n - 1) xs


myInsert2 :: [a] -> a -> Int -> [a]

myInsert2 [] y _ = [y]
myInsert2 xs y 1 = y:xs
myInsert2 (x:xs) y n = x:myInsert2 xs y (n - 1)


-- Problem 22: Create a list containing all integers within a given range.

myRange :: Int -> Int -> [Int]
myRange i j = [i..j]


-- Problem 23: Extract a given number of randomly selected elements from a list.
myRnd :: [a] -> Int -> IO [a]
myRnd xs n = do
	let len = length xs
	g <- newStdGen
	return (take n [xs !! k | k <- randomRs(0, len - 1) g])
