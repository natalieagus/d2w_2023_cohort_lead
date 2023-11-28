from abc import ABC, abstractmethod

# This a template class, cannot be instantiated on its own, because it has unimplemnted @abstractmethod
# Three types of methods in abstract class
# 1. Regular methods:  these methods are ALREADY implemented, useful for ALL kinds of State machine (start, step, transduce, is_done)
# 2. Abstract methods: MUST be implemented by the subclass, otherwise, error (get_next_values, start_state)
# 3. Optional methods: these methods are there as "helpers", some subclass MIGHT override it (declare the method with the same name without calling super()), but some might not (done)


class StateMachine(ABC):
    # Contains a SET of functions that are COMMON to a state machine
    # this is so that we dont have to write these stuffs OVER AND OVER for all state machines in our project
    # any machine we wanna turn to a state machine should just inherit this class

    # this function STARTS the SM
    # it should set its CURRENT state into the start_state defined in the subclass
    def start(self):
        # we are confident that start_state variable EXISTS because the function start_state is an abstract method
        self.state = self.start_state

    # this function RUNS the state machine
    # it takes in an inp, compute next state and output, UPDATE the CURRENT state, and return the output
    def step(self, inp):  # not a pure function
        # we assume that get_next_values is IMPLEMENTED by the subclass
        # get_next_values is an abstract method
        next_state, output = self.get_next_values(self.state, inp)
        # change its current state (update)
        self.state = next_state  # side effect
        return output

    # this function STARTS and RUNS the machine in one shot
    # usually its used for testing or simulation
    # this method uses step(inp)
    def transduce(self, inp_list):
        output = []
        # start the state machine
        self.start()
        for input_value in inp_list:
            output.append(self.step(input_value))
            # check if the FSM is done
            if (self.is_done()):
                break

        return output

    @property
    # to tell subclass inheriting this class to implement this method (because we are using it in start())
    @abstractmethod
    def start_state(self):
        pass

    @abstractmethod  # implement in subclass
    def get_next_values(self, state, inp):
        pass

    # this is an optional method, you can override it in subclass if your SM has a done state
    def done(self, state):
        return False

    def is_done(self):
        return self.done(self.state)
