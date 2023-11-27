from source.cs_1 import StateMachine


class CokeMachine(StateMachine):

    # state indexes
    # 0: start state (no money state)
    # 1: 50c state (50c is entered in the machine)
    # every state machine HAS a starting state
    @property  # getter, you can call start_state WITHOUT the ()
    def start_state(self):
        return 0  # how you name your states is up to you, just select one that makes sense

    # the FIRST argument to any function declared inside a class is ALWAYS the reference to the instance calling this function
    # get_next_values is the LOGIC of the state machine
    # this is a PURE function, meaning that its output SOLELY depends on its input (state, inp), and there's no side effects (does not change ANYTHING outside of this function either)
    def get_next_values(self, state, inp):
        # write default output, next_state first
        # these are DEFAULT values, meaning that if we don't have that specific legal state+inp combo, we return these
        """
        Determines the next state and output based on the current state and input

        Args:
        - state (any): The state of the state machine.
        - inp (any): The input accepted by the state machine

        Returns:
        - tuple: A tuple containing the next state and output in the form (next_state, output).
                The output is a tuple with information about the transaction:
                - For next_state: The updated state of the state machine.
                - For output: A tuple representing the transaction details:
                            - For example: 
                            - Amount of money left in the machine (if any)
                            - Item dispensed ("coke" or "--" for no item)
                            - Change returned (if any)

        Note:
        - Default values are returned if the state and input combination doesn't match any defined rules:
            - For next_state: The default state remains unchanged, should be equal to state 
            - For output: For example: (0, "--", inp) - Represents no change in state, no item dispensed, and input as the remaining balance.
        """
        output = (0, "--", inp)  # default output
        next_state = state  # default next_state

        # this is the logic of the coke machine
        # be very careful and code out logic that are RELEVANT to your machine
        # don't use "else" without thinking
        if state == 0:
            if inp == 100:
                next_state = 0
                # balance is $0, "coke" is dispensed, and no change given
                output = (0, "coke", 0)
            elif inp == 50:
                next_state = 1
                output = (50, "--", 0)
        elif state == 1:
            if inp == 100:
                next_state = 0
                output = (0, "coke", 50)
            elif inp == 50:
                next_state = 0
                output = (0, "coke", 0)

        # if you reach here, that means you either go to one of the state, inp combi above, or still end up with default next_state, and output
        # always return a tuple in this order: next_state and output
        # return  output, next_state # this gg
        return next_state, output  # must be in this order, see step() in StateMachine ABC
