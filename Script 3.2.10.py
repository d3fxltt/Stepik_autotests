def test_abs1():
    assert abs(-42) == 42, "Should be absolute value of a number"

def add(a, b):
    c = a + b
    return c
    assert add(a, b) == c

if __name__ == "__main__":
    test_abs1()
    add(2, 4)
    print("All tests passed!")