# Lists!
# Data structures are containers that organize and group data types together in different ways. 
# A list is one of the most common and basic data structures in Python.

# You saw here that you can create a list with square brackets. 
# Lists can contain any mix and match of the data types you have seen so far.

list_of_random_things = [1, 3.4, 'a string', True]\

# zero based indexing --- how far the element is from the beggining
list_of_random_things[0]
# 1

list_of_random_things[len(list_of_random_things)] 
# ---------------------------------------------------------------------------
# IndexError                                Traceback (most recent call last)
# <ipython-input-34-f88b03e5c60e> in <module>()
# ----> 1 lst[len(lst)]

# IndexError: list index out of rang
