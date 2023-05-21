class Calculator:
    def __init__(self):
        self.func = None

    def set_function(self, func):
        self.func = func


def fn_plus(self, a, b):
    assert self.__class__.__name__ == 'Calculator'
    return a + b


def fn_multiplied(self, a, b):
    assert self.__class__.__name__ == 'Calculator'
    return a * b


