import pytest


@pytest.mark.parametrize("first, sec, equal", [
    (1, 2, False),
    (21, 12, True)
])
def test_clac_equal(calculator_equal ,first, sec, equal):
    assert equal == calculator_equal.func(calculator_equal,first, sec)
