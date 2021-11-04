## Documentation
# Documentation is used to make your code easier to understand and use. Functions are especially readable because they often use documentation strings, or docstrings. 
# Docstrings are a type of comment used to explain the purpose of a function, and how it should be used. Here's a function for population density with a docstring.


def population_density(population, land_area):
    """Calculate the population density of an area. """
    return population / land_area
  
# Docstrings are surrounded by triple quotes. The first line of the docstring is a brief explanation of the function's purpose. 
# If you feel that this is sufficient documentation you can end the docstring at this point; single line docstrings are perfectly acceptable, as in the example above.


def population_density(population, land_area):
    """Calculate the population density of an area.

    INPUT:
    population: int. The population of that area
    land_area: int or float. This function is unit-agnostic, if you pass in values in terms
    of square km or square miles the function will return a density in those units.

    OUTPUT: 
    population_density: population / land_area. The population density of a particular area.
    """
    return population / land_area

def sq(n):
    """
    Return the square of n, accepting all numeric types:

    >>> sq(10)
    100

    >>> sq(10.434)
    108.86835599999999

    Raises a TypeError when input is invalid:

    >>> sq(4*'435')
    Traceback (most recent call last):
      ...
    TypeError: can't multiply sequence by non-int of type 'str'

    """
    return n*n
  
# If you think that a longer description would be appropriate for the function, you can add more information after the one-line summary. 
# In the example above, you can see that we wrote an explanation of the function's arguments, stating the purpose and types of each one. 
# It's also common to provide some description of the function's output.

# Every piece of the docstring is optional, however, docstrings are a part of good coding practice. 
# You can read more about docstring conventions here (https://www.python.org/dev/peps/pep-0257/
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Numpy Docstring Standard
def func(arg1, arg2):
    """Summary line.

    Extended description of function.

    Parameters
    ----------
    arg1 : int
        Description of arg1
    arg2 : str
        Description of arg2

    Returns
    -------
    bool
        Description of return value

    See Also
    --------
    otherfunc : some related other function

    Examples
    --------
    These are written in doctest format, and should illustrate how to
    use the function.

    >>> a=[1,2,3]
    >>> print [x + 3 for x in a]
    [4, 5, 6]
    """
    return True

# alternativeky
"""
My numpydoc description of a kind
of very exhautive numpydoc format docstring.

Parameters
----------
first : array_like
    the 1st param name `first`
second :
    the 2nd param
third : {'value', 'other'}, optional
    the 3rd param, by default 'value'

Returns
-------
string
    a value in a string

Raises
------
KeyError
    when a key error
OtherError
    when an other error
"""
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# The Google style guide
def square_root(n):
    """Calculate the square root of a number.

    Args:
        n: the number to get the square root of.
    Returns:
        the square root of n.
    Raises:
        TypeError: if n is not a number.
        ValueError: if n is negative.

    """
    pass
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Write a docstring for the readable_timedelta function you defined earlier! Remember the way you write your docstrings is pretty flexible! Look through Python's docstring conventions here and check out this Stack Overflow page for some inspiration!
# Quiz Solution: readable_timedelta
# Here's some ways you could've written your docstring!

def readable_timedelta(days):
    """Return a string of the number of weeks and days included in days."""
    weeks = days // 7
    remainder = days % 7
    return "{} week(s) and {} day(s)".format(weeks, remainder)

def readable_timedelta(days):
    """Return a string of the number of weeks and days included in days.

    Args:
        days (int): number of days to convert
    """
    weeks = days // 7
    remainder = days % 7
    return "{} week(s) and {} day(s)".format(weeks, remainder)

def readable_timedelta(days):
    """
    Return a string of the number of weeks and days included in days.

    Parameters:
    days -- number of days to convert (int)

    Returns:
    string of the number of weeks and days included in days
    """
    weeks = days // 7
    remainder = days % 7
    return "{} week(s) and {} day(s)".format(weeks, remainder)
