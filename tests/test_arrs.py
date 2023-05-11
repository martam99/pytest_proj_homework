from utils import arrs


def test_get():
    assert arrs.get([1, 2, 3], 1, "test") == 2
    assert arrs.get([1, 2, 3, 4, 5], 0, "test") == 1
    assert arrs.get([1, 2, 3, 4, 5], 7, "test") == "test"
    assert arrs.get([1, 2, 3], 9) == None


def test_slice():
    assert arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
    assert arrs.my_slice([1, 2, 3], 1) == [2, 3]
