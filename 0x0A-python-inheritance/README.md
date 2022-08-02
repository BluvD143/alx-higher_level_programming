# PYTHON - INHERITANCE

Inheritance allows us to define a class that inherits all the methods and properties from another class.

Parent class is the class being inherited from, also called base class.

Child class is the class that inherits from another class, also called derived class.

Inheritance is a powerful feature in object oriented programming.

It refers to defining a new class with little or no modification to an existing class. The new class is called derived (or child) class and the one from which it inherits is called the base (or parent) class.

Python has two built-in functions that work with inheritance:

- Use `isinstance()` to check an instance’s type: `isinstance(obj, int)` will be `True` only if `obj.__class__` is `int` or some class derived from `int`.

- Use  `issubclass()` to check class inheritance: `issubclass(bool, int)` is `True` since bool is a subclass of int. However, issubclass(float, int) is `False` since `float` is not a subclass of `int`.


# In this project, I learnt:
- Why Python programming is awesome
- What is a superclass, baseclass or parentclass
- What is a subclass
- How to list all attributes and methods of a class or instance
- When can an instance have new attributes
- How to inherit class from another
- How to define a class with multiple base classes
- What is the default class every class inherit from
- How to override a method or attribute inherited from the base class
- Which attributes or methods are available by heritage to subclasses
- What is the purpose of inheritance
- What are, when and how to use isinstance, issubclass, type and super built-in functions


# Resources
- [w3schools.com](https://www.w3schools.com/python/python_inheritance.asp)
- [python documentation](https://docs.python.org/3/tutorial/classes.html#inheritance)
- [analyticsvidhya.com](https://www.analyticsvidhya.com/blog/2020/10/inheritance-object-oriented-programming/#:~:text=super()%20function-,What%20is%20Inheritance%20in%20Object%20Oriented%20Programming%3F,known%20as%20the%20Parent%20class.)
- [youtube](https://www.youtube.com/watch?v=d8kCdLCi6Lk)
- [programiz](https://www.programiz.com/python-programming/inheritance)
