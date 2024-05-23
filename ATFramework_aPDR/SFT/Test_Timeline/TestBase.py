from typing import Any


class TestBase:

    @staticmethod
    def check(a: Any, b: Any, boolean: bool = True):
        if boolean:
            if not a == b:
                raise ValueError(f'Checking failed {a} is not equal to {b}')
        else:  # not bool
            if a == b:
                raise ValueError(f'Checking failed {a} should not be equal to {b}')

