from array_shift.array_shift import array_shift


def test_one(): 
    actual = array_shift([3, 4, 5, 6, 7, 4], 4)
    expected = [3, 4, 5, 4, [6, 7, 4]]
    assert actual == expected

def test_two(): 
    actual = array_shift([3, 4, 5, 6, 7, 4], 2)
    expected = [3, 4, 5, 2, [6, 7, 4]]
    assert actual == expected

def test_three(): 
    actual = array_shift([3, 4, 5, 6, 7, 4], 1)
    expected = [3, 4, 5, 1, [6, 7, 4]]
    assert actual == expected

def test_four(): 
    actual = array_shift([3, 4, 5, 6, 7, 4], 9)
    expected = [3, 4, 5, 9, [6, 7, 4]]
    assert actual == expected
