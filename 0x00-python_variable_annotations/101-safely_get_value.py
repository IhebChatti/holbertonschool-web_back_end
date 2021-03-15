#!/usr/bin/env python3
"""[safely_get_value]
"""
from typing import Union, Mapping, Any, TypeVar

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any, default: Union[T, None] = None) -> Union[Any, T]:
    """[safely_get_value]

    Args:
        dct (Mapping): [typing mapping]
        key (Any): [any type]
        default (Union[T, None], optional): [default]. Defaults to None.

    Returns:
        Union[Any, T]: [union of any type and typevar T]
    """
    if key in dct:
        return dct[key]
    else:
        return default
