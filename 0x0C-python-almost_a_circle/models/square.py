#!/usr/bin/python3
"""Square model"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value

    def __str__(self):
        """Return human readable Square value"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"

    def update(self, *args, **kwargs):
        """Assigns attributes to args and kwargs"""
        attributes = ["id", "size", "x", "y"]

        for i, arg in enumerate(args):
            if i < len(attributes):
                setattr(self, attributes[i], arg)

        if not args:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)
