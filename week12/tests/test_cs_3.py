from source.cs_3 import SimpleAccount

def test_cs_3():
    acct = SimpleAccount(110)
    out = acct.transduce([10, -25, -10, -5, 20, 20])
    assert out == [120, 95, 80, 70, 90, 110]    