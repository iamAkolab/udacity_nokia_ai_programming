Traceback means "What was the programming doing when it broke"! 
This part is usually less helpful than the very last line of your error. 
Though you can dig through the rest of the error, 
looking at just the final line ZeroDivisionError, and the message says we divided by zero. 
Python is enforcing the rules of arithmetic!

Traceback (most recent call last):
  File "/tmp/vmuser_tnryxwdmhw/quiz.py", line 1, in <module>
    print(5/0)

ZeroDivisionError: division by zero

 
 In general, there are two types of errors to look out for

Exceptions
Syntax
An Exception is a problem that occurs when the code is running, 
but a 'Syntax Error' is a problem detected when Python checks the code before it runs it. 
For more information, see the Python tutorial page on Errors and Exceptions
  (https://docs.python.org/3/tutorial/errors.html).
  
  PEP 8 -- Style Guide for Python Code
  https://www.python.org/dev/peps/pep-0008/
