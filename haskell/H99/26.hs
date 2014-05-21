-- Problem 26:  Generate the combinations of K distinct objects chosen from the N elements of a list.
module Problem26 (myCombinations) where


myCombinations :: Int -> [a] -> [[a]]
myCombinations n xs@(x:rs)
	| n == 1 = [[x] | x <- xs]
	| n == (length xs) = [xs]
	| n < 1 = error "Invalid n, it must be positive integer"
	| n > (length xs) = error "Invalid input: n > length of the list"
	| otherwise = 
		[x:cs | cs <- myCombinations (n - 1) rs] ++ myCombinations n rs
