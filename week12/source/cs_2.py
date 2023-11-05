from source.cs_1 import StateMachine

class CokeMachine(StateMachine):

    @property
    def start_state(self):
        ###BEGIN SOLUTION
        return 0
        ###END SOLUTION
        pass

    def get_next_values(self, state, inp):
        ###BEGIN SOLUTION
        if state == 0:
            if inp == 100:
                next_state = 0
                output = (0, "coke", 0)
            elif inp == 50:
                next_state = 1
                output = (50, "--", 0)
            else:
                next_state = 0
                output = (0, "--", inp)
        else:
            if inp == 50:
                next_state = 0
                output = (0, "coke", 0)
            elif inp == 100:
                next_state = 0
                output = (0, "coke", 50)
            else:
                next_state = 1
                output = (50, "--", inp)
        ###END SOLUTION
        return next_state, output