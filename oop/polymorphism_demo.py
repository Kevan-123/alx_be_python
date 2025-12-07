import math


class Shape:
    """Base Shape class."""

    def area(self):
        """Method to be overridden by subclasses."""
        raise NotImplementedError("Subclasses must implement the area() method.")


class Rectangle(Shape):
    """Rectangle class inheriting from Shape."""

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


class Circle(Shape):
    """Circle class inheriting from Shape."""

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)
