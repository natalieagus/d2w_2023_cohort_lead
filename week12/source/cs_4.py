from abc import abstractmethod
from source.cs_1 import StateMachine

# abstract class can inherit other abstract class so we can stack them all up


class StateSpaceSearch(StateMachine):

    @property
    @abstractmethod
    def statemap(self):
        pass

    @property
    @abstractmethod
    def legal_inputs(self):
        pass

    @property  # implementing StateMachine abstract method
    def start_state(self):
        return self.__start_state

    @start_state.setter
    def start_state(self, value):
        self.__start_state = value


class MapSM(StateSpaceSearch):

    def __init__(self, start):
        self.start_state = start

    @property
    # hardcode the statemap of this search "engine"
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

    # find out a set of possible inputs that are accepted in this machine, for this statemap, D can receive the most # of variation in inp: 0, 1, 2, 3, so this function should return a set: {0, 1, 2, 3}
    @property
    def legal_inputs(self):
        # one liner answer
        # return set(max([len(neighbours) for _, neighbours in self.statemap.items()]))

        max_so_far = -1  # because len(neighbours) are always >= 0

        # loop through all elements of statemap
        for _, neighbours in self.statemap.items():
            number_of_neighbours = len(neighbours)
            if (number_of_neighbours > max_so_far):
                max_so_far = number_of_neighbours
        # range(max_so_far) will return a list, then we convert to a set as per req of this question
        return set(range(max_so_far))

    def get_next_values(self, state, inp):
        # return the state that we can go to, given current state (state) and inp (0 or 1, or 2, etc)

        # default return values (in case inp is illegal)
        next_state = state  # remain in state
        output = state  # report the state as is

        # do the main logic first
        neighbours = self.statemap.get(state)
        if (neighbours is None):
            return next_state, output

        # neighbours can be None if the statemap does not contain state
        # we also need to check if inp in list of legal inputs in this machine
        # finally, check if inp < len(neighbours)

        # alternative check without using legal_inputs()
        # if isinstance(inp, int) and inp >= 0 and inp < len(neighbours):
        if inp in self.legal_inputs and inp < len(neighbours):
            # obtain the state we can go to with this inp
            next_state = neighbours[inp]
            output = next_state  # display updated state

        return next_state, output
