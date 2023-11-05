from abc import ABC, abstractmethod

class StateMachine(ABC):
    
    def start(self):
        ## TODO 
        pass

    def step(self, inp):
        ## TODO 
        pass
        
    def transduce(self, inp_list):
        ## TODO 
        pass

    @property
    @abstractmethod
    def start_state(self):
        pass 

    @abstractmethod
    def get_next_values(self, state, inp):
        pass

    def done(self, state):
        return False

    def is_done(self):
        return self.done(self.state)

    