## SDSS Computing Studies Python Assignment
### Assignment #130 Class Methods

Objectives:
* Create a class using class methods
* Use class variables

Classes that are created with only static methods are great for organizing.  You don't have to worry about conflicting variable names from other parts of your code, because all of the methods/functions that are defined in the class are confined to the class.

Classes are more than just organizers, they are data structures themselves, and they can have their own variables (called class properties) as well.  Take a look at the example1.py file to see how class properties are defined and used within a class.

Note that class methods are defined using the @classmethod identifier. 
One thing that sets them apart from static methods is that any class method must include a parameter of "cls" as the first parameter in a function/method.  This lets the method know that it needs to include all of the properties of the class within each methods scope.

Class variables and class methods can be accessed within the class using the "cls" dot prefix.

Also, note that class methods and properties can be accessed outside of the class scope by using the dot prefix that includes the class name.



