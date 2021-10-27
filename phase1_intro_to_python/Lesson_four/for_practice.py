"""
Use a for loop to take a list and print each element of the list in its own line.

Example:

sentence = ["the", "quick", "brown", "fox", "jumped", "over", "the", "lazy", "dog"]
Output:

the
quick
brown
fox
jumped
over
the
lazy
dog

"""

sentence = ["the", "quick", "brown", "fox", "jumped", "over", "the", "lazy", "dog"]

# Write a for loop to print out each word in the sentence list, one word per line
for i in sentence:
    print(i, end ="\n")
    
-----------------------------------------------------------------------------------------------------------------    
"""
Practice: Multiples of 5
Write a for loop below that will print out every whole number that is a multiple of 5 and less than or equal to 30.

This should output:

5
10
15
20
25
30
# Write a for loop using range() to print out multiples of 5 up to 30 inclusive
"""

for i in range(5, 35, 5):
    print(i)


  
