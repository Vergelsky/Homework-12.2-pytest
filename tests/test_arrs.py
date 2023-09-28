from utils import arrs
import pytest

@pytest.fixture
def get_simple_array():
    return [1, 2, 3]


def test_get(get_simple_array):
    assert arrs.get(get_simple_array, 1, "test") == 2
    assert arrs.get([], 0, "test") == "test"


def test_slice(get_simple_array):
    assert arrs.my_slice(get_simple_array, 1, 3) == [2, 3]
    assert arrs.my_slice(get_simple_array, 1) == [2, 3]
    assert arrs.my_slice(get_simple_array) == [1, 2, 3]
    assert arrs.my_slice([], 1) == []