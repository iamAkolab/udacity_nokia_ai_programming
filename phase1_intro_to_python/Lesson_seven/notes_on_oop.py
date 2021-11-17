
### Set and get methods

# The last part of the video mentioned that accessing attributes in Python can be somewhat different than in other programming languages like Java and C++. 
# This section goes into further detail.

# The Shirt class has a method to change the price of the shirt: shirt_one.change_price(20). In Python, you can also change the values of an attribute with the following syntax:

shirt_one.price = 10
shirt_one.price = 20
shirt_one.color = 'red'
shirt_one.size = 'M'
shirt_one.style = 'long_sleeve'

# This code accesses and changes the price, color, size, and style attributes directly. Accessing attributes directly would be frowned upon in many other languages, but not in Python. 
# Instead, the general object-oriented programming convention is to use methods to access attributes or change attribute values. 
# These methods are called set and get methods or setter and getter methods.

# A get method is for obtaining an attribute value. A set method is for changing an attribute value. If you were writing a Shirt class, you could use the following code:

class Shirt:

    def __init__(self, shirt_color, shirt_size, shirt_style, shirt_price):
        self._price = shirt_price

    def get_price(self):
      return self._price

    def set_price(self, new_price):
      self._price = new_price
      
# Instantiating and using an object might look like the following code:

shirt_one = Shirt('yellow', 'M', 'long-sleeve', 15)
print(shirt_one.get_price())
shirt_one.set_price(10)

"""
In the class definition, the underscore in front of price is a somewhat controversial Python convention. In other languages like C++ or Java, 
price could be explicitly labeled as a private variable. This would prohibit an object from accessing the price attribute directly like shirt_one._price = 15.
Unlike other languages, Python does not distinguish between private and public variables. Therefore, there is some controversy about using the underscore convention 
as well as get and set methods in Python. Why use get and set methods in Python when Python wasn't designed to use them?

At the same time, you'll find that some Python programmers develop object-oriented programs using get and set methods anyway. Following the Python convention, 
the underscore in front of price is to let a programmer know that price should only be accessed with get and set methods rather than accessing price directly
with shirt_one._price. However, a programmer could still access _price directly because there is nothing in the Python language to prevent the direct access.

To reiterate, a programmer could technically still do something like shirt_one._price = 10, and the code would work. But accessing price directly, in this case, 
would not be following the intent of how the Shirt class was designed.

One of the benefits of set and get methods is that, as previously mentioned in the course, you can hide the implementation from your user. Perhaps, originally, 
a variable was coded as a list and later became a dictionary. With set and get methods, you could easily change how that variable gets accessed. Without set and get methods, 
you'd have to go to every place in the code that accessed the variable directly and change the code.

You can read more about get and set methods in Python on this Python Tutorial site. https://python-course.eu/oop/properties-vs-getters-and-setters.php """


### 
