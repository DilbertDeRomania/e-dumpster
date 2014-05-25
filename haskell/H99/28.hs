-- Problem 28: sorting a list of lists according to length of sublists.
module Problem28 (mySortList) where

import Data.List
import Data.Function


mySortList :: Ord a => [[a]] -> [[a]]
mySortList = sortBy (compare `on` length)

-- ["abc","de","fgh", "", "xyzt", "de","ijkl","mn","o"]
