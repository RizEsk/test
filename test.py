def first(x):
    return x + 1

def test(a, b):
    assert first(a) == b


test(1, 2)
test(3, 4)
test(5, 6)