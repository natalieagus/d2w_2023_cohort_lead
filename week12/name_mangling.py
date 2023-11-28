class SimpleAccount:
    @property
    def start_state(self):
        print("value from property getter:")
        return 0

    @start_state.setter
    def start_state(self, value):
        # any instance attribute declared with __ in front will be RENAMED to be
        # _<ClassName>__<varName>
        self.__start_state = value

    def __init__(self, balance, name):
        self._name = name
        self.start_state = balance


# instantiate an account
JohnAccount = SimpleAccount(100, "John")
JaneAccount = SimpleAccount(200, "Jane")

# this prints out 100, but via start_state method (property)
print(JaneAccount.start_state)
print(JohnAccount.start_state)
print(JohnAccount._name)
# force access __start_state, but with appending the classname in front
# python does NAME MANGLING ---> try its best to protect accessing JaneAccount.__start_state
print(JaneAccount._SimpleAccount__start_state)
