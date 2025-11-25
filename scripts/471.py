class Geometry(): 

    def __init__(self, x = 0.0, y = 0.0): 
        self.x = x 
        self.y = y 

    def computeArea(self):
        pass 

    def computePerimeter(self): 
        pass 

    def move(self, deltaX, deltaY): 
        self.x += deltaX 
        self.y += deltaY 

    def __str__(self): 
        return 'Abstract class Geometry should not be instantiated and derived classes should override this method!'

import math  

class Circle(Geometry): 

	def __init__(self, x = 0.0, y = 0.0, radius = 1.0): 
		super().__init__(x,y)
		self.radius = radius 

	def computeArea(self): 
		return math.pi * self.radius ** 2 

	def computePerimeter (self): 
		return 2 * math.pi * self.radius 

	def __str__(self): 
		return f'Circle with coordinates {self.x}, {self.y} and radius {self.radius}'

class Rectangle(Geometry): 

    def __init__(self, x = 0.0, y = 0.0, width = 1.0, height = 1.0): 
        super().__init__(x,y)
        self.width = width 
        self.height = height 

    def computeArea(self): 
        return self.width * self.height 

    def computePerimeter (self): 
        return 2 * (self.width + self.height) 

    def __str__(self): 
        return f'Rectangle with coordinates {self.x}, {self.y}, width {self.width} and height {self.height}'

circle1 = Circle(10, 10, 10) 
print(circle1.computeArea()) 
print(circle1.computePerimeter()) 
circle1.move(2,2) 
print(circle1)

rectangle1 = Rectangle(15,20,4,5) 
print(rectangle1.computeArea()) 
print(rectangle1.computePerimeter()) 
rectangle1.move(2,2) 
print(rectangle1)