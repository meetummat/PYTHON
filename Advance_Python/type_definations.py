# Type Definitions / Type Hints in Python

n: int = 5
# This tells us that n is expected to contain an integer.
# It also helps the IDE understand the type of n and provide suggestions.
# Type hints do not force Python to use that type at runtime.

name: str = "Meet"
# name is expected to contain a string.


# Using type hints in a function
def sum(a: int, b: int) -> int:
    # a and b are expected to be integers.
    # -> int means the function is expected to return an integer.
    return a + b

print(sum(2, 4))


# We can also import types from the typing module
# and use them for more specific type hints.
from typing import List, Tuple, Dict, Union

# List of integers
numbers: List[int] = [1, 2, 3, 4, 5]
# This means numbers is expected to be a list containing integers.

# Tuple containing a string and an integer
person: Tuple[str, int] = ("Alice", 30)
# The first value is expected to be a string
# and the second value is expected to be an integer.

# Dictionary with string keys and integer values
scores: Dict[str, int] = {"Alice": 90, "Bob": 85}
# Keys are expected to be strings and values are expected to be integers.

# Union type for a variable that can contain multiple types
identifier: Union[int, str] = "ID123"
# identifier can contain either an integer or a string.

identifier = 12345
# This is also valid because identifier is allowed to contain int or str.