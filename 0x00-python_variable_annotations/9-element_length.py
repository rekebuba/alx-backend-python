#!/usr/bin/env python3
""" Let's duck type an iterable object """

from typing import List, Tuple, Iterable, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Computes the length of a list of sequences.

    Args:
        lst (Iterable[Sequence]):

    Returns:
        List[Tuple[Sequence, int]]:
    """
    return [(i, len(i)) for i in lst]
