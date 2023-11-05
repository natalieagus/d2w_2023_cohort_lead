from source.cs_1 import StateMachine

class Step:
    def __init__(self, action, state):
        self.action = action
        self.state = state
    
    def __eq__(self, other):
        return self.action == other.action and self.state == other.state
  
    def __str__(self):
        return f"action: {self.action:}, state: {self.state:}"

class SearchNode:
    def __init__(self, action, state, parent):
        self.state = state
        self.action = action
        self.parent = parent
  
    def path(self):
        ###BEGIN SOLUTION
        if self.parent == None:
            return [Step(self.action, self.state)]
        else:
            return self.parent.path() + [Step(self.action, self.state)]
        ###END SOLUTION
  
    def in_path(self, state):
        if self.state == state:
            return True
        elif self.parent == None:
            return False
        else:
            ###BEGIN SOLUTION 
            return self.parent.in_path(state)
            ###END SOLUTION
  
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