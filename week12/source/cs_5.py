from source.cs_1 import StateMachine


class Step:
    def __init__(self, action, state):
        self.action = action  # this is action taken to reach this state
        self.state = state

    # dunder method (special method)
    # overrides default equality check of reference
    def __eq__(self, other):
        return self.action == other.action and self.state == other.state

    # overrides default print of memory loc
    def __str__(self):
        return f"action: {self.action:}, state: {self.state:}"


class SearchNode:
    def __init__(self, action, state, parent):
        self.state = state
        # this is action taken to reach this state
        self.action = action
        # this is an instance of searchnode
        self.parent: SearchNode = parent

    # should return a list of STEP instances that should be taken from the ROOT to arrive at this node
    # S --> B --> D
    # d = SearchNode(bd, D, B)
    # d.path() -->
    #        has a parent, so go to else case
    #        b.path()  --->
    #               has a parent, so go to else case
    #        s.path() --->
    #               has no parent, so returns Step(None, S) to b.path()
    #       b.path assembles return val of s.path() with [Step(sb, B)] --> [Step(None, S), Step(sb, B)]
    #       b.path returns to d.path
    #       d.path assembles b.path return value with [Step(bd, D)] --> [Step(None, S), Step(sb, B), Step(bd, D)]
    def path(self):
        # base case
        if self.parent is None:
            return [Step(self.action, self.state)]
        else:
            return self.parent.path() + [Step(self.action, self.state)]

    # returns a boolean (true or false)
    # that indicates whether a given state is in the path of this current SearchNode to the root
    # e.g: S, B, D, H, G, F, SearchNode(gf, F, G)
    # E is in path? --> False
    # D is in path? --> True
    def in_path(self, state):
        # base case 1
        if self.state == state:
            return True
        # base case 2
        elif self.parent == None:
            return False
        else:
            return self.parent.in_path(state)

    def __eq__(self, other):
        if self is None and other is None:
            return True
        elif self is None:
            return False
        elif other is None:
            return False
        else:
            return self.state == other.state and self.parent == other.parent and \
                self.action == other.action
