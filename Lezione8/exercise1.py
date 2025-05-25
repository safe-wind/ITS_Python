
from abc import ABC, abstractmethod

class Shape:

    @abstractmethod
    def area(self)-> None:
        pass

    @abstractmethod
    def perimeter(self) -> None:
        pass

class Circle(Shape):
    def __init__(self, radius:float) -> None:
        super().__init__()
        self.radius = radius
    
    def perimeter(self) :
        print(f"Perimeter: {2*3.14*self.radius:.2f}cm")
    
    def area(self):
        print(f"Area: {(3.14*self.radius)**2:.2f}cm^2")
    
    def __str__(self)-> str:
        return "CIRCLE"

class Rectangle(Shape):
    
    def __init__(self, b:float, h:float) -> None:
        super().__init__()
        self.b = b
        self.h = h
    
    def perimeter(self) ->None:
        print(f"Perimeter: {2*(self.b+self.h)}cm")
    
    def area(self)-> None:
        print(f"Area: {self.b*self.h}cm^2")

    def __str__(self)-> str:
        return "RECTANGLE"
    

rect1 = Rectangle(10, 5)
circle= Circle(5)

print(rect1)
rect1.perimeter()
rect1.area()
print()
print(circle)
circle.perimeter()
circle.area()



