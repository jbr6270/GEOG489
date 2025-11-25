import math 

class Circle(): 
    def __init__(self, x = 0.0, y = 0.0, radius = 1.0): 
        self.x = x 
        self.y = y 
        self.radius = radius 

    def computeArea(self): 
        return math.pi * self.radius ** 2 

    def computePerimeter (self): 
        return 2 * math.pi * self.radius 

    def move(self, deltaX, deltaY): 
        self.x += deltaX 
        self.y += deltaY 

    def __str__(self): 
        return 'Circle with coordinates {0}, {1} and radius {2}'.format(self.x, self.y, self.radius) 

class Rectangle(): 
    def __init__(self, x = 0.0, y = 0.0, width = 1.0, height = 1.0): 
        self.x = x 
        self.y = y 
        self.width = width 
        self.height = height 

    def computeArea(self): 
        return self.width * self.height 

    def computePerimeter (self): 
        return 2 * (self.width + self.height) 

    def move(self, deltaX, deltaY): 
        self.x += deltaX 
        self.y += deltaY 

    def __str__(self): 
        return 'Rectangle with coordinates {0}, {1}, width {2} and height {3}'.format(self.x, self.y, self.width, self.height )

circle1 = Circle(10,4,3) 
print(circle1) 
print(circle1.computeArea()) 
circle1.move(3,-1) 
print(circle1)

rectangle1 = Rectangle(10,10,3,2) 
print(rectangle1) 
print(rectangle1.computeArea()) 
rectangle1.move(2,2) 
print(rectangle1)