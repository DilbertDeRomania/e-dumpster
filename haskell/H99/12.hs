-- Problem 12: Decode a run-length encoded list.
-- Given a run-length code list generated as specified in problem 11.
-- Construct its uncompressed version.

module Problem12 (myDecode) where

data EE a = M Int a | S a deriving Show

myDecode :: Eq a => [EE a] -> [a]

myDecode = foldr decodeElem [] where
	decodeElem (S x) acc = [x] ++ acc
	decodeElem (M n x) acc = (replicate n x) ++ acc

-- [M 4 'a',S 'b',M 2 'c', M 2 'a',S 'd',M 4 'e']
