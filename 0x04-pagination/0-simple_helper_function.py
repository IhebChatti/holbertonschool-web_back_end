#!/usr/bin/env python3
"""[summary]
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """[summary]

    Args:
        page (int): [page nmbr]
        page_size (int): [page size]

    Returns:
        Tuple[int, int]: [tuple of start and end]
    """
    return (page * page_size - page_size, page * page_size)
