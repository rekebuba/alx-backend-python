#!/usr/bin/env python3
"""Complex types - functions"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """takes a float multiplier as argument and returns a function

    Args:
        multiplier (float):

    Returns:
        Callable[[float], float]: function multiplies a float by multiplier.
    """
    return lambda x: x * multiplier
