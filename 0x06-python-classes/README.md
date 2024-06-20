## Python - Classes and Objects

### Learning Objectives
1. **Why Python programming is awesome**
* Being an OOP language, it provides clean and easy way to understand codes, promoting quick development

2. **What is OOP**
* A programming technique/paradigm based on the concept of `objects` which stores data.

3. **What is a class**
* One of the main aspect of OOP that defines a set of attributes and methods that the object will have.

4. **What is an object and an instance**
* Object in python is an instance of a class that represents a class and holds specific data(attributes) and methods(behavior) defined by the class.
* An instance is an individual object of a class which has unique values for its attributes

`person1 = Person("Alice", 30) #person1 is an instance of the Person class`

5. **What is the difference between a class and an object/instance**
* ***Class*** is the blueprint for creating objects. It defines the object structure and behaviors while __object/instance__ is the specific realization/implementation of a class. It represents the actual values for the attributes defined by the class.
* In an analogy of a physical library, the library can be regarded as a class and a book is an instance/object of this class.
6. **What is an attribute**

* A variable that holds data associated within a class and to specific objects. Created by joining an arbitrary name to the instance name separated by a dot `.`
```
class Person:

    pass

student = Person()
print(student.__dict__)  # Before data storage. Output: {}
student.name = "Jane Doe"

print(student.name)  #Output: Jane Doe
print(student.__dict__)  # After storing data. Output: {'name': 'Jane Doe'}
```
* If you try to access student.name, Python checks first, if "name" is a key of the student. __dict__ dictionary. If it is, thr value is retrived, if not, it checks if "name" is a key of the Person. __dict__.

* If an attribute name is not in included in either of the dictionary, the attribute name is not defined. If you try to access a non-existing attribute, python will raise an AttributeError.

7. **What are and how to use public, protected and private attributes**

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
        super().__init__(name, age):
        self.position = position
    def get_details(self):
        return(f"{self._name}, {self._age}, {self._position}")
emp = Employee("Alice", 30, "manager")
print(emp.get_details())  # Output: Alice, 30, manager
```
c. **Private attributes**:
* Are intended to be hidden from outside access and typically used to implement encapsulation. Denoted by double underscores.
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

10. **What is the special `__init__` method and how to use it**
* It is a special method used to initialize an instance. Also called a constructor in other high level programming languages.

11. **What is Data Abstraction, Data Encapsulation, and Information Hiding**

a. __Data Encapsulation__: Wrapping data and methods that work on data within a class. This restricts access to variables and methods to prevent accidental modification of data. _Setter_ are in this case used for changing data while _getters_ for retriving the data.

b. __Information Hiding__: Restricting direct access to certain details of an object, typically by using a private attribute.

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
* ***Attribute*** is variable defined in a class that holds data. It can be accessed directly while ***property*** is a special kind of attribute that allows custom access control. It is accessed like an attribute but can have getter, setter, and deleter methods to control its value.

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
[\__\getattribute\__](https://www.youtube.com/watch?v=IkWrlRei0uA&t=8s)

### References
- [Object Oriented Programming](https://python-course.eu/oop/object-oriented-programming.php)
- [Object Oriented Programming](https://python.swaroopch.com/oop.html)
- [Properties vs. Getters and Setters](https://python-course.eu/oop/properties-vs-getters-and-setters.php)
- [Python Classes and Objects](https://www.youtube.com/watch?v=apACNr7DC_s)
- [Learn to Program 9 : Object Oriented Programming](https://www.youtube.com/watch?v=1AGyBuVCTeE)
