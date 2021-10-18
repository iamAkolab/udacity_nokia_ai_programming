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

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

q3 = months[6:9]
print(q3) # [ 'July', 'August', 'September']

first_half = months[:6]
print(first_half) # ['January', 'February', 'March', 'April', 'May', 'June']

second_half = months[6:]
print(second_half) # ['July', 'August', 'September', 'October', 'November', 'December']

print(len(months)) # 12

greeting = "Hello there"
print(len(greeting)) # 11

# You saw that we can pull more than one value from a list at a time by using slicing. When using slicing, 
# it is important to remember that the lower index is inclusive and the upper index is exclusive

'this' in 'this is a string'
# True
'in' in 'this is a string'
# True
'isa' in 'this is a string'
# False
5 not in [1, 2, 3, 4, 6]
# True
5 in [1, 2, 3, 4, 6]
# False
