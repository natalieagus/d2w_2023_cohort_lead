from source.cs_1 import StateMachine


class CokeMachine(StateMachine):
    # states: 0, 1
    # 0: no money inside the machine
    # 1: have 50c inside
    # every state machine HAS a starting state
    @property
    def start_state(self):
        return 0  # the vending machine begins in state 0: no $ inside

    # what is self? --> the reference to the instance calling the method. This is ALWAYS going to be the FIRST argument in methods declared in classes (python)
    # if there's no args, get_next_values() ---> error that it accepts no args, but 1 is given
    # this function computes what the NEXT STATE and OUTPUT of this SM should be, given a state and inp
    # this function is also a PURE function
    # - it does NOT compute its output based on any external variables except its arguments (state, inp)
    # - it does NOT leave side effects (it does not change anything outside of this function)
    # we need to treat this like a lookup table
    def get_next_values(_, state, inp):
        # state, inp can be anything: int, list, dict, whatever
        # output should be next_state, output (a  tuple), of any type

        # default state
        next_state = state  # remain in state
        output = (0, "--", inp)  # return the $$

        if (state == 1):
            output = (50, "--", inp)  # return the $$

        # the main logic, be careful and only write logic that is RELEVANT in the diagram, do not skip step and assume that not A is B
        if state == 0 and inp == 50:
            next_state = 1
            output = (50, "--", 0)
        elif state == 0 and inp == 100:
            next_state = 0
            output = (0, "coke", 0)
        elif state == 1 and inp == 50:
            next_state = 0
            output = (0, "coke", 0)
        elif state == 1 and inp == 100:  # do not put else here, because not of the 3 cases above, is NOT state == 1 and inp 100
            next_state = 0
            output = (0, "coke", 50)

        return next_state, output  # must be in this order
