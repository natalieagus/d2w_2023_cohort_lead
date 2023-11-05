from source.cs_5 import SearchNode, Step 

def test_cs_5():
    s = SearchNode(None, "S", None)
    a = SearchNode(0, "A", s)
    b = SearchNode(1, "B", s)
    s1 = SearchNode(0, "S", a)
    c = SearchNode(1, "C", a)
    d1 = SearchNode(2, "D", a)
    s2 = SearchNode(0, "S", b)
    d2 = SearchNode(1, "D", b)
    e = SearchNode(2, "E", b)
    a1 = SearchNode(0, "A", s1)
    b1 = SearchNode(1, "B", s1)
    a2 = SearchNode(0, "A", c)
    f1 = SearchNode(1, "F", c)
    a3 = SearchNode(0, "A", d1)
    b2 = SearchNode(1, "B", d1)
    f2 = SearchNode(2, "F", d1)
    h1 = SearchNode(3, "H", d1)
    a4 = SearchNode(0, "A", s2)
    b3 = SearchNode(1, "B", s2)
    a5 = SearchNode(0, "A", d2)
    b4 = SearchNode(1, "B", d2)
    f3 = SearchNode(2, "F", d2)
    h2 = SearchNode(3, "H", d2)
    b5 = SearchNode(0, "B", e)
    h3 = SearchNode(1, "H", e)

    assert s.parent == None
    assert a.state == "A" and a.parent == s and a.action == 0
    assert b.state == "B" and b.parent == s and b.action == 1
    assert h3.state == "H" and h3.parent == e and h3.action == 1
    assert a5.path() == [Step(None, "S"), Step(1, "B"), Step(1, "D"), Step(0, "A")]
    assert b5.in_path("B")
    assert b5.in_path("S")
    assert b5.in_path("E")

