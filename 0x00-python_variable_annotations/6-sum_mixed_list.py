#!/usr/bin/env python3
""" Complex types - mixed list"""

from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """takes a list of mixed integers and floats

    Args:
        mxd_list (List[int  |  float]): takes integer or floats

    Returns:
        float: their sum as a float
    """

    return sum(mxd_list)
