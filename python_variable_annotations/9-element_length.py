#!/usr/bin/env python3
""" Module for function element_lenght that return
values with the appropriate types """
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Function that finds element length."""
    return [(i, len(i)) for i in lst]
