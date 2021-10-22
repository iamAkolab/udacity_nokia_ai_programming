## If Statement
# An if statement is a conditional statement that runs or skips code based on whether a condition is true or false. 

# Here's a simple example.
if phone_balance < 5:
    phone_balance += 10
    bank_balance -= 10

# Let's break this down.
# An if statement starts with the if keyword, followed by the condition to be checked, in this case phone_balance < 5, and then a colon. 
# The condition is specified in a boolean expression that evaluates to either True or False.

# After this line is an indented block of code to be executed if that condition is true. 
# Here, the lines that increment phone_balance and decrement bank_balance only execute if it is true that phone_balance is less than 5. 
# If not, the code in this if block is simply skipped.

## If, Elif, Else
# In addition to the if clause, there are two other optional clauses often used with an if statement. For example:

if season == 'spring':
    print('plant the garden!')
elif season == 'summer':
    print('water the garden!')
elif season == 'fall':
    print('harvest the garden!')
elif season == 'winter':
    print('stay indoors!')
else:
    print('unrecognized season')
    
# if: An if statement must always start with an if clause, which contains the first condition that is checked. 
# If this evaluates to True, Python runs the code indented in this if block and then skips to the rest of the code after the if statement.

# elif: elif is short for "else if." An elif clause is used to check for an additional condition if the conditions in the previous clauses in the if statement evaluate to False. As you can see in the example, you can have multiple elif blocks to handle different situations.

# else: Last is the else clause, which must come at the end of an if statement if used. This clause doesn't require a condition. 
# The code in an else block is run if all conditions above that in the if statement evaluate to False.
