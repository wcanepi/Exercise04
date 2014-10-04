import test_list_operations
"""
Part 1: Fundamental operations on lists
---------------------------------------

The fundamental operations on lists in Python are those that are part of the
language syntax and/or cannot be implemented in terms of other list operations:
    * List literals ([], ['hello'], [3, 1, 4, 1, 5, 9], etc.)
    * List indexing (some_list[index])
    * List indexing assignment (some_list[index] = value)
    * List slicing (some_list[start:end])
    * List slicing assignment (some_list[start:end] = another_list)
    * List index deletion (del some_list[index])
    * List slicing deletion (del some_list[start:end])

In this section you will implement functions that each use just one of the
operations. The docstring of each function describes what it should do. Consult
test_list_operations.py for concrete examples of the expected function behavior.
"""

def head(input_list):
    """Return the first element of the input list."""
    return input_list[0]
    pass

def tail(input_list):
    """Return all elements of the input list except the first."""
    return input_list[1:]
    pass

def last(input_list):
    """Return the last element of the input list."""
    return input_list.pop()
    pass

def init(input_list):
    """Return all elements of the input list except the last."""
    input_list.pop()
    return input_list
    pass

def first_three(input_list):
    """Return the first three elements of the input list."""
    return input_list[0:3]

def last_five(input_list):
    """Return the last five elements of the input list."""
    return input_list[-5:-1]
    pass

def middle(input_list):
    """Return all elements of the input list except the first two and the last
    two.
    """
    return input_list[2:-3]
    pass

def inner_four(input_list):
    """Return the third, fourth, fifth, and sixth elements of the input list."""
    return input_list[2:7]
    pass

def inner_four_end(input_list):
    """Return the sixth, fifth, fourth, and third elements from the end of the
    list, in that order.
    """
    return input_list[-6:-3] 
    pass

def replace_head(input_list):
    """Replace the head of the input list with the value 42."""
    input_list[0] = 42
    return input_list
    pass

def replace_third_and_last(input_list):
    """Replace the third and last elements of the input list with the value 37."""
    input_list[2] = 37
    input_list[-1] = 37
    return input_list
    pass

def replace_middle(input_list):
    """Replace all elements of the input list with the the values 42 and 37, in
    that order, except for the first two and last two elements.
    """
    list1 = input_list[0:2]
    list2 = [42, 37] * ((len(input_list) - 4) / 2)
    list3 = [input_list[-2]] + [input_list[-1]]
    return list1 + list2 + list3
    pass

def delete_third_and_seventh(input_list):
    """Remove the third and seventh elements of the input list."""
    del input_list[2]
    del input_list[6]
    return input_list
    pass

def delete_middle(input_list):
    """Remove all elements from the input list except for the first two and the
    last two.
    """
    del input_list[2:-2]
    return input_list
    pass

"""
Now would be a great time to ask for a code review.
"""