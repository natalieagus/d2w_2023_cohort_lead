from source.cs_1 import StateMachine

class Test(StateMachine):
    @property
    def start_state(self):
        return 0

    def get_next_values(self, state, inp):
        next_state = state + inp
        output = next_state
        return next_state, output

    def done(self, state):
        if state == -1:
            return True
        else:
            return False

class NoImplement(StateMachine):
    pass
    
def test_cs_0():
    t1 = Test()
    t1.start()
    assert t1.state == 0
    out = t1.step(2)
    assert t1.state ==2 and out == 2

    t2 = Test()
    out = t2.transduce([1,2,3,4])
    assert out == [1, 3, 6, 10]

    t3 = Test()
    out = t3.transduce([1, -2, 3])
    assert out == [1, -1]

    try:
        t4 = NoImplement()
        raise AssertionError
    except TypeError:
        pass