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
