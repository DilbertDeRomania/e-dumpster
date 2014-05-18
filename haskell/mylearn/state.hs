-- Code from yaht, just tried to understand/feel it better.
-- simple tree type
data Tree a = Leaf a | Branch (Tree a) (Tree a)

-- State is actually a function from state to (state, value) tuple
type State st val = st -> (st, val)
