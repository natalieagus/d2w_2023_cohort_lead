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
    def get_next_values(_, state, inp):
        """
        Determines the next state and output based on the current state and input.

        Parameters:
        _ : Unused parameter.
        state : Current state, can be of any type.
        inp : Input value, can be of any type.

        Returns:
        Tuple: (next_state, output)
            - next_state: Updated state after processing input.
            - output: Output tuple based on state and input.
                Format: (value, description, additional_info)
                - e.g: (0, "coke", 50) represents 0$ in the machine, "coke" being dispensed, and 50c of change. 
                - This depends on implementation

        Note:
        - State and input can be any type.
        - The function follows specific logic based on state and input combinations.
        - Handles transitions between states and generates appropriate outputs.
        - The order of return values in the tuple is (next_state, output).
        """
        pass

    # this is an optional method, you can override it in subclass if your SM has a done state
    def done(self, state):
        return False

    def is_done(self):
        return self.done(self.state)


# class SpriteMachine(StateMachine):

#     # override done method in parent's
#     # because we have specific implementation for this SpriteMachine
#     def done(self, state):
#         if (state == 1):
#             return True
#         return False
#     # other methods


# spriteMachine = SpriteMachine()
# # this is going to call is_done in StateMachine, then it's going to call done in SpriteMachine (the "youngest" version)
# spriteMachine.is_done(1)
