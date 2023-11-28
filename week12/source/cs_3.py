
from source.cs_1 import StateMachine
import numbers
# this is not a traditional state machine because it doesn't have a set of DISCRETE states
# the SimpleAccount represents a stateful system where a single state (balance) is continuously updated based on inputs, but it's not a traditional FSM
# not infinite state machine either because: (physical system) ---> denomination of $ is discrete, (digital system) ---> there's a limit in floating pt precision


class SimpleAccount(StateMachine):
    @property
    def start_state(self):
        return self.__start_state

    @start_state.setter
    def start_state(self, value):
        self.__start_state = value

    def __init__(self, balance):
        self.start_state = balance
        pass

    def get_next_values(self, state, inp):
        # this still HAS to be a pure function
        # do NOT change any vars outside of this func
        # do NOT rely on any vars outside of this func apart from state and inp
        # default values (if inp is illegal)
        next_state = state  # balance remains the same
        output = state  # output is the "display" of new balance

        # check if inp is a digit or a number (int/float/double)
        if (not isinstance(inp, numbers.Number)):
            return next_state, output  # return default values

        # if we reach here, inp is a number
        # check if there's withdrawal penalty
        if (inp < 0) and state < 100:
            next_state = state + inp - 5
        else:  # safe to do this
            next_state = state + inp  # this is a deposit or withdrawal without penalty
        output = next_state
        return next_state, output  # return updated values
