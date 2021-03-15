#!/usr/bin/env python3
"""[element_length]
"""
from typing import List, Iterable, Tuple, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """[element_length]

    Args:
        lst (Iterable[Sequence]): [list]

    Returns:
        List[Tuple[Sequence, int]]: [list]
    """
    return [(i, len(i)) for i in lst]
