# Strings
# Strings in Python are shown as the variable type str.
# You can define a string with either double quotes " or single quotes '

# You can also include a \ in your string to be able to include one of these quotes:

this_string = 'Simon\'s skateboard is in the garage.'
print(this_string)

# There are a number of other operations you can use with strings as well. In this video you saw a few:

first_word = 'Hello'
second_word = 'There'
print(first_word + second_word)

# HelloThere

print(first_word + ' ' + second_word)

# Hello There

print(first_word * 5)

# HelloHelloHelloHelloHello

print(len(first_word))

# 5

# Unlike the other data types you have seen so far, you can also index into strings. 
# Here is a small example. Notice Python uses 0 indexing 

# len() is a built-in Python function that returns the length of an object, like a string. 
# The length of a string is the number of characters in the string. This will always be an integer.

print(len("ababa") / len("ab"))
#2.5
