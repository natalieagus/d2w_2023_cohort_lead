
from source.cs_1 import StateMachine
import numbers
# This is a variant of an Accumulator class
# It is not a traditional FSM  because it does not have discrete set of states that are finite (theoretically)
# It is also not a traditional infinite state machine because it doesn't work with continuous values (inp, output all depends on the precision of the computer running it)
# If we can represent the money balance theoretically an large as possible --> to infinity, then theoretically this is a Turing Machine


class SimpleAccount(StateMachine):
    @property
    def start_state(self):
        return self.__start_state

    @start_state.setter
    def start_state(self, value):
        self.__start_state = value

    def __init__(self, balance):
        # this will call the start_state SETTER, which will set its self.__start_state private variable
        self.start_state = balance

    def get_next_values(_, state, inp):
        # remember, this is a pure function
        # default return values
        next_state = state  # don't change the account balance at all
        output = state  # printout the current $$ inside the account

        # early termination, check BEFORE main logic
        # let's check everything that's illegal
        # handle the case where inp != a number
        if (not isinstance(inp, numbers.Number)):
            return next_state, output

        # do the main logic
        # if we are withdrawing
        if (inp < 0) and state < 100:
            next_state = state + inp - 5  # has penalty

        else:
            # it's a deposit
            next_state = state + inp

        # CHECK after main logic
        # finally check if this transaction causes a -ve balance? if yes, reset, and ignore
        if (next_state < 0):
            next_state = state  # reset, don't withdraw at all

        # update the output to reflect the new $$
        output = next_state

        return next_state, output
