from source.cs_1 import StateMachine


class Step:
    # the functions with __ in front and the back are called
    # dunder methods
    # They are special methods that have specific functionalities when used within classes, and they are called in a SPECIAL way
    # __init__ is called using the ClassName(...)
    def __init__(self, action, state):
        # self.__score = 0  # private custom variable
        self.action = action
        self.state = state

    # overriding the default eq dunder method with custom implementation bc we don't want to compare references (address) anymore but we want to compare its action and state to decide equality
    # is called using == between two instances of this class
    def __eq__(self, other):
        return self.action == other.action and self.state == other.state

    # called when we do print(class_instance)
    def __str__(self):
        return f"action: {self.action:}, state: {self.state:}"


class SearchNode:
    def __init__(self, action, state, parent):
        self.state = state
        self.action = action
        # composition (has-a)
        # a SearchNode instance has a SearchNode instance as its parent
        # what is this datatype? what instance should this be? it should be another instance of SearchNode
        self.parent: SearchNode = parent

    # return a LIST of Step instances from this Node, to its origin (root)
    # A --> B
    # B.path() --> B has a parent, so B will call A.path()
    #   A is a root node, so it will return [Step(a.action,a)] to B (its caller)
    #   B receives [Step(a.action,a)]  and THEN append it with [Step(b.action, b)] BECAUSE B has NOT finish (return) yet
    #   finally, B returns [Step(a.action,a), Step(b.action,b)] to its caller (us)
    def path(self):
        # be careful when creating a new list inside a chain of recursive functions because we want its effect to last down the chain, and up back to the first caller
        # output = []  # a mistake, because empty list is always recreated at every level, this list if must be used should be placed either outside of the function, or passed as an argument to this function

        # check if this SearchNode is a root node, if yes, just create Step representing this node
        if self.parent is None:
            return [Step(self.action, self.state)]
        else:
            # output.append([Step(self.action, self.state)])  # mistake too
            # return output.append(self.parent.path())  # mistake too
            return self.parent.path() + [Step(self.action, self.state)]

    # A --> B ---> C
    #       B ---> D
    # D.in_path(A) --> True
    # C.in_path(D) --> False
    # C.in_path(C) --> True
    # this function checks of given state is this instance's ancestor
    # EXAMPLE

    # D.in_path(A) calls B.in_path(A) calls A.in_path(A), which returns True
    #   A.in_path(A) returns True to B.in_path(A)
    #   B.in_path(A) just pass what A.in_path(A) returns, and then returns True to D.in_path(A)
    def in_path(self, state):
        if self.state == state:
            return True
        elif self.parent == None:
            return False
        else:
            # call the function in_path on this instance's parent
            return self.parent.in_path(state)

    def __eq__(self, other):
        # if we do: self == other, will call the eq func by default, that is checking the memory address equality (or reference equality) so it will always return False given that youre not doing node_1 == node_1

        # need to check if we are comparing to another instance of SearchNode or not
        # maybe it's better to just check of self or other is instance of SearchNode
        # because other can be not None, but not a SearchNode
        if self is None and other is None:
            return True
        elif self is None:
            return False
        elif other is None:
            return False
        else:
            # check if the other state has an action or a parent
            # this might be throwing an error if other.parent is None because we cant compare == with a None
            # it's possible for x.parent to be None because it's a root Node
            # it's also possible for x.action to be None because it's a final Node (finish state)
            return self.state == other.state and self.parent == other.parent and \
                self.action == other.action
