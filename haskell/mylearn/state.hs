--import Control.Monad

-- Code from yaht, just tried to understand/feel it better.
-- simple tree type
data Tree a = Leaf a | Branch (Tree a) (Tree a)

-- State is actually a function from state to (state, value) tuple
newtype State st val = State(st -> (st, val))

-- State is partially applied (it lacks value).
instance Monad (State state) where
	return a = State (\state -> (state, a))

	-- action is a functin applied to the value inside State.
	State run >>= action = State run'
		where run' st =
			let
				(st', a) = run st -- run the current state and get the (state,value) tupple
				State newState = action a  -- action applied to a  is a new function st -> (st, val) ?
			in newState st' -- apply new state transition to st'

-- getstate and putstate

myMapList :: (a -> State s b) -> [a] -> State s [b]
myMapList f [x] = do
	b <- f x
	return [b]

myMapList f (x:xs) = do
	b <- f x
	c <- myMapList f xs
	return (b : c)


runStateM :: State state a -> state -> (state, a)
runStateM (State f) st = f st


-- runStateM (myMapList (\x -> State(\y -> (y, x + 1))) [1, 2, 3]) 1234
--mapList (\x -> State(\y -> (y, x + 1))) [1, 2, 3]

