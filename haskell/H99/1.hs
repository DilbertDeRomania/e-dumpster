-- Problem 1: find the last element of a list. 

last_elem [] = Nothing
last_elem [x] = Just x
last_elem (x:xs) = last_elem xs
