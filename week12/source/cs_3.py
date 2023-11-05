
from source.cs_1 import StateMachine


class SimpleAccount(StateMachine):
    @property
    def start_state(self):
        return self.__start_state
    
    @start_state.setter
    def start_state(self, value):
        self.__start_state = value

    def __init__(self, balance):
        ## TODO 
        pass

    def get_next_values(self, state, inp):
        ## TODO 
        pass