import pytest


@pytest.mark.parametrize("first, sec, equal", [
    (1, 2, 3),
    (2, 3, 5)
])
def test_clac_plus(calculator_plus,first, sec, equal):
    assert equal == calculator_plus.func(first, sec)
