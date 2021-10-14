#A method in Python behaves similarly to a function. Methods actually are functions that are called using dot notation. 
#For example, lower() is a string method that can be used like this, on a string called "sample string": sample_string.lower()

my_string.islower()
# True
my_string.count('a')
# 2
my_string.find('a')
# 3

# One important string method: format()
# We will be using the format() string method a good bit in our future work in Python, 
# and you will find it very valuable in your coding, especially with your print statements.

print("Mohammed has {} balloons".format(27))
# Mohammed has 27 balloons

animal = "dog"
action = "bite"
print("Does your {} {}?".format(animal, action))
#Does your dog bite?

maria_string = "Maria loves {} and {}"
print(maria_string.format("math", "statistics"))
# aria loves math and statistics

# Another important string method: split()
# This function or method returns a data container called a list that contains the words from the input string. 
# We will be introducing you to the concept of lists in the next video.

# The split method has two additional arguments (sep and maxsplit). 
# The sep argument stands for "separator". 
# It can be used to identify how the string should be split up 
# (e.g., whitespace characters like space, tab, return, newline; specific punctuation (e.g., comma, dashes)). 
# If the sep argument is not provided, the default separator is whitespace.

# True to its name, the maxsplit argument provides the maximum number of splits.
# The argument gives maxsplit + 1 number of elements in the new list, with the remaining string being returned as the last element in the list. 
# You can read more about these methods in the Python documentation too.

# A basic split method:

new_str = "The cow jumped over the moon."
new_str.split()
# Output is: ['The', 'cow', 'jumped', 'over', 'the', 'moon.']


# Here the separator is space, and the maxsplit argument is set to 3.
new_str.split(' ', 3)
# Output is: ['The', 'cow', 'jumped', 'over the moon.']


# Using '.' or period as a separator.
new_str.split('.')
# Output is: ['The cow jumped over the moon', '']


# Using no separators but having a maxsplit argument of 3.
new_str.split(None, 3)
# Output is: ['The', 'cow', 'jumped', 'over the moon.']
