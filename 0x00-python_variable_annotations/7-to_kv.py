#!/usr/bin/env python3
"""Complex types - string and int/float to tuple"""

from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """takes a string k and an int OR float v as and returns a tuple

    Args:
        k (str): string
        v (int  |  float]): int or float

    Returns:
        Tuple:  The first element of the tuple is the string k.
                The second element is the square of the int/float v.
    """
    return (k, float(v**2))
