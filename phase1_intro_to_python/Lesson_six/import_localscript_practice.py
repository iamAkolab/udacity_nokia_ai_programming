# Quiz: Compute an Exponent
# It's your turn to import and use the math module. Use the math module to calculate e to the power of 3. print the answer.

# Refer to the math module's documentation to find the function you need!

# print e to the power of 3 using the math module
import math

print(math.exp(3))

#--------------------------------------------------------------------------------------------------------------------------------
# Quiz: Password Generator
# Write a function called generate_password that selects three random words from the list of words word_list and concatenates them into a single string. 
# Your function should not accept any arguments and should reference the global variable word_list to build the password.

# password_generator.py
# TODO: First import the `random` module
import random

# We begin with an empty `word_list`
word_file = "words.txt"
word_list = []

# We fill up the word_list from the `words.txt` file
with open(word_file,'r') as words:
	for line in words:
		# remove white space and make everything lowercase
		word = line.strip().lower()
		# don't include words that are too long or too short
		if 3 < len(word) < 8:
			word_list.append(word)

# TODO: Add your function generate_password below
# It should return a string consisting of three random words 
# concatenated together without spaces
def generate_password():
    return random.choice(word_list) + random.choice(word_list) + random.choice(word_list)



# Now we test the function
print(generate_password())

# words.txt
Alice
was
beginning
to
get
very
tired
of
sitting
by
her
sister
bank
having
nothing
Once
twice
she
had
peeped
into
the
book
her
sister
was
reading
but
it
had
no
pictures
or
conversations
in
it
and
what
is
the
use
of
a
book
thought
Alice
without
pictures
or
conversations

#--------------------------------------------------------------------------------------------------------------------------------
"""
Our favourite modules
The Python Standard Library has a lot of modules! To help you get familiar with what's available, here are a selection of our favourite Python Standard Library modules and why we use them!

csv: very convenient for reading and writing csv files
collections: useful extensions of the usual data types including OrderedDict, defaultdict and namedtuple
random: generates pseudo-random numbers, shuffles sequences randomly and chooses random items
string: more functions on strings. This module also contains useful collections of letters like string.digits (a string containing all characters which are valid digits).
re: pattern-matching in strings via regular expressions
math: some standard mathematical functions
os: interacting with operating systems
os.path: submodule of os for manipulating path names
sys: work directly with the Python interpreter
json: good for reading and writing json files (good for web work)
"""
