from source.cs_4 import StateSpaceSearch, MapSM

def test_cs_4():
    mapSM = MapSM("S")
    mapSM.start()
    ans = mapSM.transduce([0, 1, 1, 2, 0])
    assert ans == ["A", "C", "F", "G", "F"]
    assert mapSM.legal_inputs == set(range(4))
