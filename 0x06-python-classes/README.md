## Python - Classes and Objects## Python - Classes and Objects

### Learning Objectives
1. Why Python programming is awesome
* Being an OOP, it provides clean and easy to understand, promoting quick development

2. What is OOP
* A programming technique/paradigm based on the concept of `objects` which stores data.

3. What is a class
* One of the main aspect of OOP that defines a set of attributes and methods that the object will have.

4. What is an object and an instance
* Object in python is an instance of a class that represents a class and holds specific data(attributes) and methods(behavior) defined by the class.
* An instance is an individual object of a class which has unique values for its attributes
 
	person1 = Person("Alice", 30) #person1 is an instance of the Person class

5. What is the difference between a class and an object/instance
* __Class__ is the blueprint for creating objects. It defines the object structure and behaviors while __object/instance__ is a specific realization/implementation of a class. It represents the actual values for the attributes defined by the class.

6. What is an attribute

* A variable that holds data associated with a class and to specific objects.

	class Person:
	def __init__(self, name, age):
		self.name = name  # name is an attribute
		self.age = age  # age is an attribute

7. What are and how to use public, protected and private attributes

a. **Public attributes**:
* Are accessible from outside the class. Defined within `__init__` method without any underscores.

	def __init__(self, name):
		self.name = name  # Public attribute
	person1 = Person("Alice")
	print(person1.name) # Accesible: Output: Alice

b. **Protected attributes**:
* Intended to be accessed within the classand its subclasses. Denoted by prefixing single underscore '_'.

	class Person:
		def __init__(self, name, age):
			self._name = name
			self._age = age
	class Employee(Person):
		def __init__(self, name, age, position):
			super().__init__(name, age):
			self.position = position
		def get_details(self):
			return(f"{self._name}, {self._age}, {self._position}")
	emp = Employee("Alice", 30, "manager")
	print(emp.get_details())  # Output: Alice, 30, manager

c. **Private attributes**:
* Are intended to be hidden from outside access and typically used to implement encapsulation. Denoted by double underscores '__'
* Can be accessed/modified indirectly within the class through methods

	class Person:
		def __init__(self, age):
			self.__age = age
		def get_age(self):
			return self.__age
		person1 = Person(30)
		print(person1.get_age)  # Accessible through method: Output: 30

	
8. What is self
* Allows an object to refer to itself just as 'my'. Used to access variables and methods within the instance.

9. What is a method
* Function defined within a class that describes the behavior of an object.

10. What is the special `__init__` method and how to use it
* It is a special method that initializes the object's attributes with the given values. Also called a constructor in other high level programming languages.

- What is Data Abstraction, Data Encapsulation, and Information Hiding
- What is a property
- What is the difference between an attribute and a property in Python
- What is the Pythonic way to write getters and setters in Python
- How to dynamically create arbitrary new attributes for existing instances of a class
- How to bind attributes to object and classes
- What is the `__dict__` of a class and/or instance of a class and what does it contain
- How does Python find the attributes of an object or class
- How to use the getattr function

### References
- [Object Oriented Programming](https://python.swaroopch.com/oop.html)
- [Properties vs. Getters and Setters](https://python-course.eu/oop/properties-vs-getters-and-setters.php)
- [Python Classes and Objects](https://www.youtube.com/watch?v=apACNr7DC_s)
- [Learn to Program 9 : Object Oriented Programming](https://www.youtube.com/watch?v=1AGyBuVCTeE)

