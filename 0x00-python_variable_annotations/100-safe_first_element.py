#!/usr/bin/env python3
"""Duck typing - first element of a sequence"""

from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Retrieves the first element of a sequence if it exists.

    Args:
        lst (Sequence[Any]):

    Returns:
        Union[Any, None]:
    """
    if lst:
        return lst[0]
    else:
        return None
