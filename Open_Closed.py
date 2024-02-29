#2
# Open-Closed Principle
#The Open-Closed Principle requires that classes should be open for extension and closed to
# modification.

#Modification means changing the code of an existing class, and extension means adding
# new functionality.

#Correct
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

def calculate_area(shapes):
    return sum([shape.area() for shape in shapes])

shapes = [Circle(2), Rectangle(2, 4), Circle(4), Rectangle(4, 8)]
print(f"Total area: {calculate_area(shapes)}")