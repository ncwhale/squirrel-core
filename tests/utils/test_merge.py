import pytest

def test_dict_deep_merge():
    from squirrel_core.utils.merge import dict_deep_merge

    # Test 1: Merge two dictionaries.
    a = {'a': {'b': {'c': {'d': 1, 'l': [1, 2, 3]}}}}
    b = {'a': {'b': {'c': {'e': 2, 'l': [4, 5, 6]}}}}
    c = dict_deep_merge(dict(a), b)
    assert c == {'a': {'b': {'c': {'d': 1, 'e': 2, 'l': [1, 2, 3, 4, 5, 6]}}}}

    # Test 2: Merge two dictionaries with some key is not dict.
    a = {'a': {'b': {'c': {'d': 1, 'l': {'x': 1, 'y': 2, 'z': 3}}}}}
    b = {'a': {'b': {'c': {'e': 2, 'l': [1, 2, 3]}}}}
    with pytest.raises(ValueError):
        c = dict_deep_merge(dict(a), b)
