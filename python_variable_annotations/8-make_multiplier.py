#!/usr/bin/env python3
""" Module for function make_multiplier that takes a float
multiplier as argument and returns a function that multiplies
a float by multiplier. """
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    # Callable: Returns a func that takes a float and returns float.
    """Function that returns a function that multiplies a
       float by multiplier. """
    def function_to_return(var: float) -> float:
        return var * multiplier
    return function_to_return
