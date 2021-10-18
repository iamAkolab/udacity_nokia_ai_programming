# Nice, that was a little tricky! A data type is just a type that classifies data. 
# This can include primitive (basic) data types like integers, booleans, and strings, as well as data structures, such as lists.

#Data structures are containers that organize and group data types together in different ways. 
# For example, some of the elements that a list can contain are integers, strings, and even other lists!


# Useful Functions for Lists I

# len() returns how many elements are in a list.

# max() returns the greatest element of the list. How the greatest element is determined depends on what type objects are in the list. 
# The maximum element in a list of numbers is the largest number. The maximum elements in a list of strings is element that would occur last if the list were sorted alphabetically.
# This works because the the max function is defined in terms of the greater than comparison operator. 
# The max function is undefined for lists that contain elements from different, incomparable types.

# min() returns the smallest element in a list. min is the opposite of max, which returns the largest element in a list.

# sorted() returns a copy of a list in order from smallest to largest, leaving the list unchanged. 
# set reverse = True from largest to smallest

#Join is a string method that takes a list of strings as an argument, and returns a string consisting of the list elements joined by a separator string.


new_str = "\n".join(["fore", "aft", "starboard", "port"])
print(new_str)

#fore
#aft
#starboard
#port

name = "-".join(["García", "O'Kelly"])
print(name)

# García-O'Kelly

# append method is an helpful method called append adds an element to the end of a list.

letters = ['a', 'b', 'c', 'd']
letters.append('z')
print(letters)

# ['a', 'b', 'c', 'd', 'z']


names = ["Carol", "Albert", "Ben", "Donna"]
print(" & ".join(sorted(names)))

# "Albert", "Ben", "Carol", "Donna"

