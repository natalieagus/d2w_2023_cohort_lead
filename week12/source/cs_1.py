from abc import ABC, abstractmethod

# In abstract classes (template classes), there are three types of methods
# 1. standard implemented methods: these methods are already implemented, will be shared among ALL subclasses (start, step, transduce), subclass should NOT touch these things
# 2. optional methods: may or may not be implemented, it may or may not be relevant for the subclass (done)
# 3. abstract methods: these are methods that are NOT implemented yet, but MUST be implemented by the subclass (start_state, get_next_values)


class StateMachine(ABC):
    # contains a SET of functions that are COMMON to a state machine
    # this is so that we DON'T have to write these stuffs OVER and OVER for various state machine
    # any machine we want to turn into a state machine should just inherit this class

    # this function STARTS the state machine
    # it should set its CURRENT state into the start_state
    # e.g: switch it on
    def start(self):
        self.state = self.start_state

    # this function FEEDS inp to the state machine (running it)
    # it should COMPUTE its NEXT STATE and OUTPUT, given an inp from user
    # step is NOT a pure function because it changes VARIABLES outside of this function, and its output depends on OTHER things, not just inp
    # this function ASSUMES that the SM is already started,
    # do NOT call self.start()
    # typically used on live programs
    def step(self, inp):
        # compute the supposed next state and output
        next_state, output = self.get_next_values(self.state, inp)
        # change current state (side effect)
        self.state = next_state
        # return output
        return output

    # STARTS and RUN the state machine in ONE shot
    # typically used for simulation or testing
    def transduce(self, inp_list):
        # calls STEP function REPEATEDLY given a list of inp values
        output = []
        # start the state machine
        self.start()
        idx = 0
        # with for-loop
        # for input_value in inp_list:
        #     output.append(self.step(input_value))
        #     if (self.is_done()):
        #         break

        # go through ALL the inputs
        while (idx < len(inp_list) and not self.is_done()):
            output.append(self.step(inp_list[idx]))
            idx += 1
        return output

    # @abstractmethod decorator tells the subclass to IMPLEMENT these methods
    @property
    @abstractmethod
    def start_state(self):
        pass

    @abstractmethod
    def get_next_values(self, state, inp):
        pass

    # this should be modified in the subclass if that subclass SM has a "end state"
    def done(self, state):
        return False

    def is_done(self):
        return self.done(self.state)
