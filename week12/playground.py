def function_one(x):
    return x*x


def function_two(y):
    return function_one(y) + function_one(y)


text = "ABC"


def function_three(z):
    text += "DEF"


def function_four(a):
    if (text == "ABC"):
        return a
    return None

# in a pure function, the same input produces the same output


class CokeMachine():
    # why do we need private variables?
    @property
    def start_state(self):
        print("start_state getter:")
        # check for clearance
        # round to 2dp
        return self.__start_state

    @start_state.setter
    def start_state(self, value):
        print("start_state setter:")
        # this __ is REPLACED by Python into _<Classname>__<VariableName> during runtime
        self.__start_state = value

    def __init__(self, start_state):
        print("Coke Machine init")
        self.start_state = start_state


cm0 = CokeMachine(0)
cm1 = CokeMachine(1)
print(cm1.start_state)  # can but dont
