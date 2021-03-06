"""
Quiz: Population Density Function
Write a function named population_density that takes two arguments, population and land_area, and returns a population density calculated from those values.
I've included two test cases that you can use to verify that your function works correctly. Once you've written your function, use the Test Run button to test your code.
"""

# write your function here
def population_density(population, land_area):
    return population/land_area



# test cases for your function
test1 = population_density(10, 1)
expected_result1 = 10
print("expected result: {}, actual result: {}".format(expected_result1, test1))

test2 = population_density(864816, 121.4)
expected_result2 = 7123.6902801
print("expected result: {}, actual result: {}".format(expected_result2, test2)
      


#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
 """
 Quiz: readable_timedelta
Write a function named readable_timedelta. The function should take one argument, an integer days, and return a string that says how many weeks and days that is. For example, calling the function and printing the result like this:

print(readable_timedelta(10))
should output the following:

1 week(s) and 3 day(s).
"""
      
# write your function here
def readable_timedelta(days):
    week = 0
    day = 0
    
    if days < 7:
        week = 0
        day = days
    else:
        week = int(days / 7)
        day = days - (week * 7)
    return str(week) + ' week(s) and ' + str(day) + ' days' 

# test your function
print(readable_timedelta(1))
print(readable_timedelta(6))
print(readable_timedelta(7))
print(readable_timedelta(9))
print(readable_timedelta(14))
      
# Alternatively
def readable_timedelta(days):
    # use integer division to get the number of weeks
    weeks = days // 7
    # use % to get the number of days that remain
    remainder = days % 7
    return "{} week(s) and {} day(s).".format(weeks, remainder)

# test your function
print(readable_timedelta(10))

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------      
# QUIZ QUESTION
# Read through this code snippet:

egg_count = 0

def buy_eggs():
    egg_count += 12 # purchase a dozen eggs

buy_eggs()
      
# What is the result of running this code? If you aren't sure, try running it on your own computer!
# This causes an UnboundLocalError, since Python doesn't allow functions to modify variables that are outside the function's scope.
# A better way would be to pass the variable as an argument and reassign it outside the function. See more on this in the next page.
      
 """
 Note that it is not passed as an argument into the function, so the function assumes the egg_count being referred to is the global variable.

In the last video, you saw that within a function, we can print a global variable's value successfully without an error. 
This worked because we were simply accessing the value of the variable. If we try to change or reassign this global variable, 
however, as we do in this code, we get an error. Python doesn't allow functions to modify variables that aren't in the function's scope.

A better way to write this would be:
"""
egg_count = 0

def buy_eggs(count):
    return count + 12  # purchase a dozen eggs

egg_count = buy_eggs(egg_count)
