-- Problem 2: find the last but one element of a list. 

lastButOne []      = Nothing
lastButOne [x]     = Nothing
lastButOne [x, y]  = Just x
lastButOne (x: xs) = lastButOne xs
