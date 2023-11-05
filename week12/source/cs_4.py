from abc import abstractmethod
from source.cs_1 import StateMachine

class StateSpaceSearch(StateMachine):
    
    @property
    @abstractmethod
    def statemap(self):
        pass

    @property
    @abstractmethod
    def legal_inputs(self):
        pass

    @property
    def start_state(self):
        return self.__start_state
    
    @start_state.setter
    def start_state(self, value):
        self.__start_state = value

class MapSM(StateSpaceSearch):
        
    def __init__(self, start):
        self.start_state = start

    @property
    def statemap(self):
        statemap = {"S": ["A", "B"],
                    "A": ["S", "C", "D"],
                    "B": ["S", "D", "E"],
                    "C": ["A", "F"],
                    "D": ["A", "B", "F", "H"],
                    "E": ["B", "H"],
                    "F": ["C", "D", "G"],
                    "H": ["D", "E", "G"],
                    "G": ["F", "H"]}
        return statemap

    @property
    def legal_inputs(self):
        ###BEGIN SOLUTION
        maxsofar = -1
        for state, neighbours in self.statemap.items():
            count = len(neighbours)
            if count > maxsofar:
                maxsofar = count
        return set(range(maxsofar))
        ###END SOLUTION
        pass

  
    def get_next_values(self, state, inp):
        ###BEGIN SOLUTION
        neighbours = self.statemap.get(state, None)
        if neighbours != None and inp in self.legal_inputs and inp < len(neighbours):
            next_state = neighbours[inp]
            return next_state, next_state
        else:
            return state, state 
        ###END SOLUTION
        pass
            
    