from abc import abstractmethod
from source.cs_1 import StateMachine

# we can inherit abstract classes to create a new subclass that is also abstract


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
        # this is just this question's construct
        statemap = {"S": ["A", "B"],  # from S, we can go to A by taking move 0, and to B by taking move 1
                    # from A, we can go to S by taking move 0, or go to C by taking move 1, or to D by taking move 2
                    "A": ["S", "C", "D"],
                    "B": ["S", "D", "E"],
                    "C": ["A", "F"],
                    # at D, I can receive 4 different inputs to land me in 4 different states --> I can represent the set of legal inputs at D to be simply 3: 0, 1, 2, 3
                    "D": ["A", "B", "F", "H"],
                    "E": ["B", "H"],
                    "F": ["C", "D", "G"],
                    "H": ["D", "E", "G"],
                    "G": ["F", "H"]}
        return statemap

    @property
    # returns a list of numbers that represents INPUTs that can be "processed" by the state machine
    # whats the use of this function again?
    def legal_inputs(self):
        # this returns a list of inputs that can be taken in all states in this FSM
        max_so_far = -1  # assume at first we don't have any neighbours, and can't make any move from this state
        # loop through my statemap  (unpack automatically)
        for state, neighbours in self.statemap.items():
            number_of_neighbours = len(neighbours)
            if (number_of_neighbours > max_so_far):
                max_so_far = number_of_neighbours

        # e.g: max_so_far is 4 (from state D), so this returns [0,1,2,3]
        return set(range(max_so_far))  # what does this do?

    # e.g: state is "B", inp is 2
    # get_next_values should return "E" as next_state, and also "E" as output
    def get_next_values(self, state, inp):
        # default values
        output = state  # imagine this is displaying that we are at the same state
        # imagine that we are given some illegal input and we don't want to mess up our current state
        next_state = state

        # get the neighbours of this given state
        neighbours = self.statemap.get(state)

        # check if this state exists?
        if neighbours is None:
            return next_state, output

        # check if inp is in the list of legal inputs for this machine and that this state ACCEPTS that input
        # why do we need to check if inp is in self.legal_inputs?
        # cos legal_inputs is computed from self.statemap
        # and neighbours is also obtained from self.statemap
        # so isn't is sufficient to just check of inp<len(neighbours) ie: accepted in this state?
        if inp in self.legal_inputs and inp < len(neighbours):
            next_state = neighbours[inp]
            output = next_state  # output should "display next_state"
            return next_state, output

        # if we reach here, then our input is illegal or our input is not accepted by this state
        return next_state, output
