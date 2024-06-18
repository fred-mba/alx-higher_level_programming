#!/usr/bin/python3

MagicClass = __import__('103-magic_class').MagicClass

magic = MagicClass(7)
print("Radius:", magic._MagicClass__radius) # Accessing the private attribute for demonstration
print("Area:", magic.area())
print("Circumference:", magic.circumference())
