*""" 
Factorials with While Loops
Find the factorial of a number using a while loop.

A factorial of a whole number is that number multiplied by every whole number between itself and 1. 
For example, 6 factorial (written "6!") equals 6 x 5 x 4 x 3 x 2 x 1 = 720. So 6! = 720.

We can write a while loop to take any given number and figure out what its factorial is.

Example: If number is 6, your code should compute and print the product, 720. 
"""


# number to find the factorial of
number = 6   

# start with our product equal to one
product = 1

# track the current number being multiplied
current = 1

# write your while loop here
while number != 1:
    # multiply the product so far by the current number
    product = product * number
    
    # increment current with each iteration until it reaches number
    number = number - 1


# print the factorial of number
print(product)

#------------------------------------------------------------------------------------------------------------
"""
Factorials with For Loops
Now use a for loop to find the factorial!

It will now be great practice for you to try to revise the code you wrote above to find the factorial of a number, 
but this time, using a for loop. Try it in the code editor below!
"""
# number to find the factorial of
number = 6   

# start with our product equal to one
product = 1

# write your for loop here
for num in range(2, number + 1):
    product *= num
    
# print the factorial of number
print(product)

#------------------------------------------------------------------------------------------------------------
"""
Suppose you want to count from some number start_num by another number count_by until you hit a final number end_num. 
Use break_num as the variable that you'll change each time through the loop. 

For simplicity, assume that end_num is always larger than start_num and count_by is always positive.

Before the loop, what do you want to set break_num equal to? How do you want to change break_num each time through the loop? 
What condition will you use to see when it's time to stop looping?

After the loop is done, print out break_num, showing the value that indicated it was time to stop looping. 
It is the case that break_num should be a number that is the first number larger than end_num
"""
start_num = 20 #provide some start number
end_num = 500 #provide some end number that you stop when you hit
count_by = 40 #provide some number to count by 

# write a while loop that uses break_num as the ongoing number to 
#   check against end_num

break_num = start_num
while break_num < end_num:
    break_num += count_by

print(break_num)

#------------------------------------------------------------------------------------------------------------
"""
Count By Check
Suppose you want to count from some number start_num by another number count_by until you hit a final number end_num, 
and calculate break_num the way you did in the last quiz.

Now in addition, address what would happen if someone gives a start_num that is greater than end_num. 
If this is the case, set result to "Oops! Looks like your start value is greater than the end value. 
Please try again." Otherwise, set result to the value of break_num.
"""

start_num = 450 #provide some start number
end_num = 500 #provide some end number that you stop when you hit
count_by = 50 #provide some number to count by 

# write a condition to check that end_num is larger than start_num before looping
# write a while loop that uses break_num as the ongoing number to 
#   check against end_num
break_num = start_num
if start_num > end_num:
    result = "Oops! Looks like your start value is greater than the end value. Please try again."
else:
    while break_num < end_num:
        break_num += count_by
    result = break_num

print(result)

#-------------------------------------------------------------------------------------------------------------------------------
"""
Nearest Square
Write a while loop that finds the largest square number less than an integerlimit and stores it in a variable nearest_square. 
A square number is the product of an integer multiplied by itself, for example 36 is a square number because it equals 6*6.

For example, if limit is 40, your code should set the nearest_square to 36.
""""
limit = 40

# write your while loop here

num = 0
while (num+1)**2 < limit:
    num += 1
nearest_square = num**2

print(nearest_square)
#------------------------------------------------------------------------------------------------------------
