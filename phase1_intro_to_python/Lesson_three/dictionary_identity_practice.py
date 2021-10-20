# Define a Dictionary, population,
# that provides information
# on the world's largest cities.
# The key is the name of a city
# (a string), and the associated
# value is its population in
# millions of people.

#   Key     |   Value
# Shanghai  |   17.8
# Istanbul  |   13.3
# Karachi   |   13.0
# Mumbai    |   12.5

population = {"Shanghai":  17.8, "Istanbul":  13.3, "Karachi": 13.0,  "Mumbai": 12.5}

#-------------------------------------------------------------------------------------

# A KeyError occurs. It would be cool if Python could search the Internet for the answer to any question, 
# but if Python were that smart the world wouldn't need programmers! 
# The other two options are possible with a bit more programming, but they are not how dictionaries work on their own.

#-----------------------------------------------------------------------------------------
>>> elements.get('dilithium')
None
>>> elements['dilithium']
KeyError: 'dilithium'
>>> elements.get('kryptonite', 'There\'s no such element!')
"There's no such element!"

##=-------------------------------------------------------------------------------------------------------------------------------------

a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a == b)
print(a is b)
print(a == c)
print(a is c)

That's correct! List a and list b are equal and identical. List c is equal to a (and b for that matter) since they have the same contents. 
But a and c (and b for that matter, again) point to two different objects, i.e., they aren't identical objects. 
That is the difference between checking for equality vs. identity
