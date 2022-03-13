# TODO: 0: Timing Code
Implement the start_time to measure total program runtime.

## Coding within the check_images.py
## Code to Edit within Project Workspace - Timing
The comments in the program header indicated by #TODO: 0
Add your name
The date you started working on the project
Check the timing code within the main() function indicated by #TODO: 0
We have added all the code you need to time your program. Here we expect that you will test our timing code by adding different values of seconds in the sleep() function to check how the timing and formatting of time works within the code we have provided.
Expected Outcome
When completed this code will calculate the runtime of the program. Specifically, this code will measure how long each of the three algorithms will take to classify all the images in the pet_images folder.

Checking your code
Use the sleep() function to test that your timing code is working correctly.

Test the following:

Set different values of seconds in the sleep() function to check the timing and formatting of time.
Project Workspace - Timing
The next concept will have your workspace to work on #TODO: 0
Editing of check_images.py can be done within the Project Workspace - Timing
For additional information and help on #TODO: 0, please look at the information below:
Importing Time Module
Timing your program or a portion of your program's code allows one to compare the time costs associated with using different algorithms to solve a problem. Additionally, timing your code allows one to know the time costs associated with running a program using given computing resources.

To time your code In Python requires the import of the time() function from the python time module. To simulate our program running for a certain period of time, we are going to use the time module's sleep() function. It will pause the program execution for a set number of seconds.

Since we only need to use the time() and sleep() functions, we will only import these two functions and not the entire time module. Only importing the functions from the module that you need saves on memory (RAM) your program requires to execute.

Such an import would look like the following:

## Imports time() and sleep() functions from time module
from time import time, sleep
Using Time and Sleep Functions
To time your code you will need to:

First, create a variable that records the start time (start_time), the point you want to start timing your code
Next, create a variable that records the stop time (end_time), the point you want to stop timing your code
Finally, to calculate the total runtime (tot_time) by subtracting the start_time from end_time
Note: the following:
tot_time will be the total time your code ran in seconds
sleep() is used in the code below to pause the program execution for 75 seconds. To time actual code, you'd replace sleep(75) with the code that you wanted to time.
The code below demonstrates the use of time() and sleep().

## Sets start time
start_time = time()

## Replace sleep(75) below with code you want to time
sleep(75)

## Sets end time
end_time = time()

## Computes overall runtime in seconds
tot_time = end_time - start_time

## Prints overall runtime in seconds
print("\nTotal Elapsed Runtime:", tot_time, "in seconds.")
Formatting Time
Likely you will want to format your runtime into a nice format like hh:mm:ss where:

hh is two digit hours indicator
mm is two digit minutes indicator
ss is two digit seconds indicator
Recall the following regarding formatting time in seconds within python:

3600 seconds in an hour
60 seconds in a minute
/ (division operator) with int() function will return only the whole number part of a division
% (modulo operator) returns the remainder of a division
str() function converts numeric values into strings
Lesson Data Types and Operators: Arithmetic Operators and Integers and Floats will help with formatting time in python.  
Using the information above provides the following format of total runtime, as tot_time:

hours = int( (tot_time / 3600) )
minutes = int( ( (tot_time % 3600) / 60 ) )
seconds = int( ( (tot_time % 3600) % 60 ) )
 
Below you will find code that will print the runtime in the format hh:mm:ss:

## Prints overall runtime in format hh:mm:ss
print("\nTotal Elapsed Runtime:", str( int( (tot_time / 3600) ) ) + ":" +
          str( int(  ( (tot_time % 3600) / 60 )  ) ) + ":" + 
          str( int(  ( (tot_time % 3600) % 60 ) ) ) ) 
## Note
Instead of rounding to the nearest second, our code using the int() function and will truncate the value of seconds. This means if your Total Runtime: 4.519087974567, then it would be formatted to Total Runtime: 0:0:4. If you instead want to round to the nearest second, you will want to replace the int() function with the round() function in calculating the number of seconds above.
