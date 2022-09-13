import pytest

#int
def test_1():
    assert(type(1)) == int
    assert (type(-1)) == int
    assert (type(int('41241'))) == int


@pytest.mark.parametrize(
    "value1,value2,excepted",
    [(-100, 2, 0), (100, 2, 0), (0, 2, 0)])
def test_2(value1, value2, excepted):
    assert value1 % value2 == excepted


def test_3():
    try:
        assert sorted(2)
    except TypeError:
        pass


#float
def test_4():
    assert type(1.0) == float
    assert type(-1.0) == float



@pytest.mark.parametrize(
    "value1,value2,excepted",
    [(-100, 2, -50.0), (100, 2, 50.0), (-1, 1, -1.0)])
def test_5(value1, value2, excepted):
    assert value1 / value2 == excepted


def test_6():
    try:
        assert (0 / 1) == float
    except AssertionError:
        pass