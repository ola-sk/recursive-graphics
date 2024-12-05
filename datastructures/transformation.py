"""
This file contains the Transformation enum class.
Key Points:
Enums define a limited set of values that a variable can take.
Members of an enum are constants and immutable.
You can use enums for cleaner and more readable code when dealing with a finite set of options.
"""
from enum import Enum

class Transformation(Enum):
    SYMMETRIC = 1
    ASYMMETRIC = 2