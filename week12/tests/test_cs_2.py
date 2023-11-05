from source.cs_2 import CokeMachine

def test_cs_2():
    cm = CokeMachine()
    cm.start()
    assert cm.state == 0
    out = cm.step(50)
    assert out == (50, "--", 0) and cm.state == 1
    out = cm.transduce([50, 50, 100, 10, 50, 100, 10])
    assert out == [(50, '--', 0), (0, 'coke', 0), (0, 'coke', 0), (0, '--', 10), (50, '--', 0), (0, 'coke', 50), (0, '--', 10)]