-- Problem 7: Flatten a nested list structure.
-- I tried to write an onverloaded functon for [x] and [[x]] but I haven't succeeded.
-- I tried with class and instance, see:
--     http://stackoverflow.com/questions/6119225/overloading-function-signatures-haskell
--     http://www.haskell.org/haskellwiki/Ad-hoc_polymorphism#Ad-hoc_polymorphism



module Problem7 (myFlatten) where

data NestedList a = Elem a | List [NestedList a]

myFlatten :: (NestedList a) -> [a]
myFlatten (Elem x) = [x]
myFlatten (List xs) = foldr (++) [] (map myFlatten xs)
