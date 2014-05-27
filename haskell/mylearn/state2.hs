

newtype TState s v = State { run :: s -> (s, v) }

instance Monad (TState s) where
	return v = State (\s -> (s,v))

	-- action is a functin applied to the value inside State.
	State run >>= action = State run'
		where run' st =
			let
				(st', a) = run st -- run the current state and get the (state,value) tupple
				State newState = action a  -- action applied to a  is a new function st -> (st, val) ?
			in newState st' -- apply new state transition to st'


runStateM :: TState state a -> state -> a
runStateM (State f) st = snd (f st)

--getState :: TState state state putState
getState = State (\state -> (state, state))

test :: TState Int Int
{--test = do
	x <- getState
	return  (x + 11)--}


--test = getState >>= \x -> return (x + 11)

--test = State (\state -> (state, state)) >>= \x -> State (\s -> (s, x + 11))
