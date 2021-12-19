# Make test for pytest

import dta
import pytest

def test_dict_check():
    sample = {'a': 1, 'b': 2, 'c': 3}
    assert dta.Attr2Dict(dta.Dict2Attr(sample)) == sample

class Dummy():
    pass

def test_attr():
    sample = Dummy()
    sample.a = 1
    sample.b = 2
    sample.c = 3
    assert dta.Dict2Attr({'a': 1, 'b': 2, 'c': 3}).__dict__ == sample.__dict__

def test_function_amount():
    assert len(dta.__all__) == 3
    print(len(dta.__all__))

def test_error():
    with pytest.raises(TypeError):
        dta.Dict2Attr(1)
    with pytest.raises(TypeError):
        dta.Attr2Dict(1)