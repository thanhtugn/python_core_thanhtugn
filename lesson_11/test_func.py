import pytest
from unit_test_practice import *

def test_capital_str():
    assert capital_str('python07') == 'Python07'
	
def test_validation_input():
    with pytest.raises(TypeError):
        capital_str(8)