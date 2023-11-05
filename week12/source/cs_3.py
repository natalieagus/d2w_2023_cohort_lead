
from source.cs_1 import StateMachine


class SimpleAccount(StateMachine):
    @property
    def start_state(self):
        return self.__start_state
    
    @start_state.setter
    def start_state(self, value):
        self.__start_state = value

    def __init__(self, balance):
        ###BEGIN SOLUTION
        self.start_state = balance
        ###END SOLUTIOn
        pass

    def get_next_values(self, state, inp):
        ###BEGIN SOLUTION
        if inp < 0 and state < 100:
            next_state = state + inp - 5
        else:
            next_state = state + inp
        
        output = next_state
        ###END SOLUTION
        return next_state, output