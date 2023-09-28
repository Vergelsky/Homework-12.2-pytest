from utils import dicts

def test_get_val():

    assert dicts.get_val({"first": 1, "second": 2}, "first") == 1
    assert dicts.get_val({"first": 1, "second": 2}, "third") == "def"
    assert dicts.get_val({}, "first", "def") == "def"
    assert dicts.get_val({}, "first", "nope") == "nope"
