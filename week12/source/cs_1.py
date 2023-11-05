from abc import ABC, abstractmethod

class StateMachine(ABC):
    
    def start(self):
        ###BEGIN SOLUTION
        self.state = self.start_state
        ###END SOLUTION
        pass

    def step(self, inp):
        ###BEGIN SOLUTION
        ns, o = self.get_next_values(self.state, inp)
        self.state = ns
        return o
        ###END SOLUTION
        pass
        
    def transduce(self, inp_list):
        ###BEGIN SOLUTION
        output = []
        self.start()
        idx = 0
        while idx < len(inp_list) and not self.is_done():
            output.append(self.step(inp_list[idx]))
            idx += 1
        return output
        ###END SOLUTION
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

    