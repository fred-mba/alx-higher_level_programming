## Python - Classes and Objects

### Learning Objectives
1. **What is an object and an instance**
* An Object in python is an instance of a class that represents a class and holds specific data(attributes) and behavior(methods) defined by the class.

**Characteristics if Objects**  
i. _State_: represented by attributes(data)  
ii. _Behavior_: represented by methods(functions)  
iii. _Identity_: Unique name or identifier for an object  

* An instance is an individual object of a class which has unique values for its attributes

```
class Dog:
    def __init__(self, name):
        self.name = name # name is an attribute(state)
    def bark(self):   # behavior(method)
        print(f"{self.name} says woof!")

Example:
    my_dog = Dog("Buddy") # my_dog is an object of the Dog class
    another_dog = Dog("Buddy")
    print(another_dog == my_dog) # prints False since despite the two dog objects have same name, they are two different instances
```

2. **What is OOP**
* A programming technique/a way to structure programs by combining data(attributes) and behavior(methods) into objects.
* It enhances enhances code reusability through inheritance and makes it easier to manage and maintain large codebases.

3. **First-Class everything**
* The principle means that everything in Python - functions, classes, modules, and even instances - are treated as objects
- This means you:  
a) Can _assign_ functions and classes to variables  
b) Pass them as _arguments_ to other functions  
c) Can _return_ them from functions  
d) Can _store_ them in data structures like lists and dictionaries  

4. **What is a class**
* A class is a blueprint/recipe for creating objects, defining the shared attributes(variables) and behaviors(methods) that all objects of that class will have.
* It encapsultes data and behavoir into a single unit, providing modularity and reusability..

5. **What is the difference between a class and an object/instance**
* ***Class*** is the blueprint for creating objects. It defines the object structure and behaviors while __object/instance__ is the specific realization/implementation of a class. It represents the actual values for the attributes defined by the class.
* In an analogy of a physical library, the library can be regarded as a class and a book is an instance/object of this class.
6. **What is an attribute**

* A variable that stores data associated within a class or specific objects.

**Types of Attributes**  
i) _Instance Atrributes_: Defined in the `__init__` constructor. Each instance has unique values.  
ii) _Class Attributes_: Defined outside `__init__` constructor, belongs to the class itself, and shared across all objects.  
```
class Car:
    wheels = 4  # class attribute

    def __init__(self, brand, model):
        self.brand = brand  # instance attribute
        self.model = model  # instance attribute

car1 = Car("Toyota", "Corolla")
car2 = Car("Honda", "Civic")
print(car1.brand)  # Output: Toyota
print(car2. model) # Output: Civic

print(car1.wheels) # Output: 4
print(car2.wheels) # Output: 4

```

7. **What are and how to use public, protected and private attributes**

| Attribute type | Syntax            | Access Level |
|----------------|:-------------------:|--------------|
| Public         | `self.attribute`  | Can be accessed and modified anywhere       |
| Protected      | `self._attribute` | Should be treated as internal but can still be accessed       |
| Private        | `self.__attribute`| Cannot be accessed directly outside the class       |

a. **Public attributes**:
* Are accessible from outside the class. Defined within `__init__` method without any underscores.
```
def __init__(self, name):
    self.name = name  # Public attribute
person1 = Person("Alice")
print(person1.name) # Accesible: Output: Alice
```
b. **Protected attributes**:
* Intended to be accessed within the class and its subclasses. Denoted by prefixing single underscore.
```
class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age
class Employee(Person):
    def __init__(self, name, age, position):
        super().__init__(name, age)
        self._position = position
    def get_details(self):
        return(f"{self._name}, {self._age}, {self._position}")
emp = Employee("Alice", 30, "manager")
print(emp.get_details())  # Output: Alice, 30, manager
```
c. **Private attributes**:
* Are intended to hide certain data or methods from outside access and typically used to implement strict encapsulation. Denoted by double underscores.
* They are not even accessible to subclasses.
* Can be accessed/modified through public or protected methods(e.g getters and setters)
* Can be accessed/modified indirectly within the class through methods
```
class Person:
    def __init__(self, age):
        self.__age = age
    def get_age(self):
        return self.__age
person1 = Person(30)
print(person1.get_age)  # Accessible through method: Output: 30
```
	
8. **What is self**
* Allows an object to refer to itself just as "my". Used to access variables and methods within the instance.

9. **What is a method**
* These are special functions defined within a class which controls the access to the data protected by a shell.
**Types of methods**

| Method Type     | Definition                                                  | Example                        |
|----------------|-------------------------------------------------------------|--------------------------------|
| Instance Method | Operates on a specific object using `self`.                | `def greet(self):`            |
| Class Method    | Works at the class level, not an instance. Uses `@classmethod` and `cls`. | `def from_string(cls, data):` |
| Static Method   | A function inside a class, but doesn’t use `self` or `cls`. Uses `@staticmethod`. | `def utility_function():` |

10. **What is the special `__init__` method and how to use it**
* It is a special method used to initialize an instance.
* Called automatically when you create an instance of the class.

11. **What is Data Abstraction, Data Encapsulation, and Information Hiding**

a. __Data Encapsulation__: Wrapping data and methods that work on data within a class. This restricts access to variables and methods to prevent accidental modification of data.
* When you create a class in Python, you are actually implementing encapsulation.

b. __Information Hiding__: It is the specific aspect of encapsulation that focuses on restricting direct access to certain details of an object, typically by using a private attribute.

c. __Data Abstraction__: The concept of providing only essentials and hiding the implementation details. For example, in a banking application, you might interact with an account object through methods like deposit() and withdraw(), without knowing how the system manages these processes internally.  

`Data Abstraction = Data Encapsulation + Data Hiding`

12. **What is a property**
* A special kind of an attribute that define methods in a class, define custom when accessing, modifying, or deleting instance data. They are used to encapsulate and validate data and maintain the existing code. Properties help us access methods like an [attribute](https://www.youtube.com/watch?v=jCzT9XFZ5bw) without breaking the code.
```
class MyClass:
    def __init__(self):
        self._x = 0
    
    @property
    def x(self):
        print("Getting x")
        return self._x
    
    @x.setter
    def x(self, value):
        if value < 0:
            raise ValueError("Value must be non-negative")
        print("Setting x")
        self._x = value
    
    @x.deleter
    def x(self):
        print("Deleting x")
        del self._x

```

```
class Employee:
    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary

    @property
    def employee_salary(self):
        return self.__salary

    @employee_salary.setter
    def employee_salary(self, amount):
        if amount >= 0:
            self.__salary = amount
        else:
            raise ValueError("Salary must be positive")

emp = Employee("John", 50000) # setting John and 50000
print(emp.employee_salary)  # Access as an attribute: Output: 50000
emp.employee_salary = 60000  # Modify using setter method
print(emp.employee_salary)  # Output: 60000
```
13. **What is the difference between an attribute and a property in Python**
| Feature       | Attribute                              | Property                                        |
|--------------|--------------------------------------|------------------------------------------------|
| Definition   | A variable stored in an object      | A special method controlling access to an attribute |
| Access       | Direct (`obj.attribute`)            | Accessed like an attribute but internally calls getter and setter methods (`obj.property`) |
| Modification | Directly assignable (`obj.attribute = value`) | Uses `@property` and `@property.setter` to control modifications |


14. **How to dynamically create arbitrary new attributes for existing instances of a class**
* You can add new attributes to an instance at runtime as in this example:
```
class Car:
    def __init__(self, brand):
        self.brand = brand
my_car = Car("Toyota")
print(my_car.__dict__)` # Output: {'brand': 'Toyota'}
my_car.color = "Red"
print(my_car.__dict__)` # Output after adding color attribute: {'brand': 'Toyota', 'color': 'Red'}
```
15. **How to bind attributes to object and classes**
* Attributes are bind to objects and classes using '.'
```
class Car:
    wheels = 4  # Class attribute

    def __init__(self, brand):
        self.brand = brand  # Instance attribute

my_car = Car("Toyota")
your_car = Car("Honda")

print(Car.wheels)  # Access class attribute: Output: 4
print(my_car.brand)  # Access instance attribute: Output: Toyota
print(your_car.brand)  # Access instance attribute: Output: Honda

```
16. **What is the `__dict__` of a class and/or instance of a class and what does it contain**
* The `__dict__` attribute in Python is a dictionary that stores an object's/class's writable attributes

17. **How does Python find the attributes of an object or class**
* Python uses a lookup mechanism that searches through the class's `__dict__`, the instance's `__dict__`, and any parent classes in the method resolution order (MRO) to find attributes and methods.

```
class A:
    x = 5

class B(A):
    pass

b = B()
print(b.x)  # Output: 5, found in class A through inheritance
```
18. [How to use the getattr function](https://www.digitalocean.com/community/tutorials/python-getattr)
* If the attribute is found through the normal mechanism, 'get attribute' is not called, instead python calls a special attribute, 
[\_\_getattribute\_\_](https://www.youtube.com/watch?v=IkWrlRei0uA&t=8s)

18. **Why Python programming is awesome**
* Being an OOP language, it provides clean and easy way to understand codes, promoting quick development

### References
- [Object Oriented Programming](https://python-course.eu/oop/object-oriented-programming.php)
- [Object Oriented Programming](https://python.swaroopch.com/oop.html)
- [Properties vs. Getters and Setters](https://python-course.eu/oop/properties-vs-getters-and-setters.php)
- [Python Classes and Objects](https://www.youtube.com/watch?v=apACNr7DC_s)
- [Learn to Program 9 : Object Oriented Programming](https://www.youtube.com/watch?v=1AGyBuVCTeE)
