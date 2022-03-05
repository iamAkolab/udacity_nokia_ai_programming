# Why Object-Oriented Programming
"""
Object-oriented programming has a few benefits over procedural programming, which is the programming style you first learned.
      Object-oriented programming allows you to create large, modular programs that can easily expand over time.
       Object-oriented programs hide implementation from the end-user.
       
       
Consider Python package like scikit-learn, pandas, or numpy. These are all Python libraries built with object-oriented programming. 
Scikit-learn, for example, is a relatively large and complex package built with object-oriented programming. 
This package has expanded over the years with new functionality and new algorithms
Consider Python package like scikit-learn, pandas, or numpy. These are all Python libraries built with object-oriented programming. 
Scikit-learn, for example, is a relatively large and complex package built with object-oriented programming. 
This package has expanded over the years with new functionality and new algorithms
"""

##Object-oriented programming (OOP) vocabulary
"""
Class: A blueprint consisting of methods and attributes.
Object: An instance of a class. It can help to think of objects as something in the real world like a yellow pencil, a small dog, or a blue shirt.
However, as you'll see later in the lesson, objects can be more abstract.
Attribute: A descriptor or characteristic. Examples would be color, length, size, etc. These attributes can take on specific values like blue, 3 inches, large, etc.
Method: An action that a class or object could take.
OOP: A commonly used abbreviation for object-oriented programming.
Encapsulation: One of the fundamental ideas behind object-oriented programming is called encapsulation: you can combine functions and data all into a single entity. In object-oriented programming, this single entity is called a class. 
Encapsulation allows you to hide implementation details, much like how the scikit-learn package hides the implementation of machine learning algorithms.
"""

# Object-oriented programming syntax
""""
Function versus method
A function and a method look very similar. They both use the def keyword. They also have inputs and return outputs. 
The difference is that a method is inside of a class whereas a function is outside of a class.
Finally, you'll write your own class.
"""
class Shirt:
  def __init__(self, shirt_color, short_size, shirt_style, shirt_price):
    self.color = shirt_color
    self.size = shirt_size
    self.style = shirt_style
    self.price = shirt_price
    
  def change_price(self, new_price):
    self.price = new_price
    
  def discount(self, discount):
    return self.price * (1 - discount)
  
"""
What is self?
If you instantiate two objects, how does Python differentiate between these two objects?
shirt_one = Shirt('red', 'S', 'short-sleeve', 15)
shirt_two = Shirt('yellow', 'M', 'long-sleeve', 20)
That's where self comes into play. If you call the change_price method on shirt_one, how does Python know to change the price of shirt_one and not of shirt_two?
shirt_one.change_price(12)
Behind the scenes, Python is calling the change_price method:
    def change_price(self, new_price):
        self.price = new_price
Self tells Python where to look in the computer's memory for the shirt_one object. Then, Python changes the price of the shirt_one object. When you call the change_price method, shirt_one.change_price(12), self is implicitly passed in.
The word self is just a convention. You could actually use any other name as long as you are consisten, but you should use self to avoid confusing people.
"""
