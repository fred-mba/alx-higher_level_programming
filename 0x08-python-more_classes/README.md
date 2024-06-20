## Python - More Classes and Objects

### Learning Objectives

- What is the difference between `__str__` and `__repr__`
* `__str__`: used to provide a pretty or human readable string representation of an object.
* `__repr__`: used to provide a more detailed and ambigous representation of an object, useful for debugging and development. Ideally, __repr__ should return a string that is copied to [eval()](), would recreate the original object.
* __str__ is called by the 'str()' fuction and 'print()' function
* __repr__ is called by the 'repr()' function and by the interactive intepreter when you type the object directly
- What is a static method
* These are special methods that belong to a class rather than an instance of the class(instance methods). They do not require an instance([self](../0x06-python-classes/README.md)) or a reference to the class itself(`cls`). This method can't access or modify utility fuctions that relate to the class.
* If '__str__' is not defined in a class, Python falls back to '__repr__' when the 'str()' or 'print()' is called
* If neither '__str__' nor '__repr__'is defined, Python uses the default mechanism by the [base class]().

```
class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __repr__(self):
        return f"Book(title='{self.title}', author='{self.author}', year={self.year})"

    def __str__(self):
        return f"'{self.title}' by {self.author}, published in {self.year}"

# Create a Book instance
my_book = Book("1984", "George Orwell", 1949)

# Using __repr__
print(repr(my_book))  # Output: Book(title='1984', author='George Orwell', year=1949)

# Using __str__
print(str(my_book))   # Output: '1984' by George Orwell, published in 1949

# Interactive interpreter (or just typing the object in a script)
my_book  # Output: Book(title='1984', author='George Orwell', year=1949)

# Using print, which calls __str__ implicitly
print(my_book)  # Output: '1984' by George Orwell, published in 1949

``` 
Class Method vs Static Method
* Class method can access or modify the class state while a static method can't
* Class methods take `cls` as the first parameter
* Class methods are used to create factory methods that return class objects.
* Static methods are used to create utility functions.
```
"""use of class method and static method""".
from datetime import date


class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age

	# a class method to create a Person object by birth year.
	@classmethod
	def fromBirthYear(cls, name, year):
		return cls(name, date.today().year - year)

	# a static method to check if a Person is adult or not.
	@staticmethod
	def isAdult(age):
		return age > 18


person1 = Person('James', 21)
person2 = Person.fromBirthYear('James', 1996)

print(person1.age)
print(person2.age)

# print the result
print(Person.isAdult(22))
```
