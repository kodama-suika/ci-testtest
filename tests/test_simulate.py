from main.simulate import my_sqrt, my_times

def test_my_sqrt():
    assert my_sqrt(4) == 2

def test_my_times():
    assert my_times(5, 3) == 15