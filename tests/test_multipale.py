import pytest


@pytest.mark.parametrize("first, sec, equal", [
    (1, 2, 2),
    (2, 3, 6)
])
def test_clac_multiplied(calculator_multiplied,first, sec, equal):
    assert equal == calculator_multiplied.func(first, sec)
