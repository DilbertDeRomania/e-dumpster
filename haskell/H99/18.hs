-- Problem 18:  Extract a slice from a list.

module Problem18 (mySlice) where

mySlice :: [a] -> Int -> Int -> [a]
mySlice xs i j = myTake (j - i + 1) $ myDrop (i - 1) xs


myTake :: Int -> [a] -> [a]
myTake 0 xs = []
myTake _ [] = []
myTake n (x:xs) = x : myTake (n - 1) xs


{- myDrop shoudl be tail recrusive? -}
myDrop :: Int -> [a] -> [a]
myDrop 0 xs = xs
myDrop _ [] = []
myDrop n (x:xs) = myDrop (n - 1) xs
