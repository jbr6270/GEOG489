import sys 
from PyQt5 import QtGui, QtWidgets 
from PyQt5.QtCore import Qt, QPoint

class GeometryDrawingWidget(QtWidgets.QWidget): 

     def __init__(self, objects): 
         super(GeometryDrawingWidget,self).__init__() 
         self.objectsToDraw = objects 

     def paintEvent(self, event): 
         qp = QtGui.QPainter() 
         qp.begin(self) 
         for obj in self.objectsToDraw: 
             obj.paint(qp) 
         qp.end()

class MyMainWindow(QtWidgets.QMainWindow): 

    def __init__(self, objects): 
        super().__init__()
        self.resize(300,300) 
        self.setCentralWidget(GeometryDrawingWidget(objects))

class Geometry(): 
     
    def __init__(self, x = 0.0, y = 0.0, color = Qt.black): 
        self.x = x 
        self.y = y
        self.color = color 
        
    def printClassInfo(): 
        print( "So far, {0} geometric objects have been created".format(Geometry.counter) )
        
    def computeArea(self):
        pass 

    def computePerimeter(self): 
        pass
    def paint(self, painter): 
        pass

    def move(self, deltaX, deltaY): 
        self.x += deltaX 
        self.y += deltaY 

    def __str__(self): 
        return 'Abstract class Geometry should not be instantiated and derived classes should override this method!'

import math  

class Circle(Geometry): 

    def __init__(self, x = 0.0, y = 0.0, radius = 1.0, color = Qt.black): 
        super().__init__(x,y,color)
        self.radius = radius 

    def computeArea(self): 
        return math.pi * self.radius ** 2 

    def computePerimeter (self): 
        return 2 * math.pi * self.radius

    def paint(self, painter): 
        painter.setPen(QtGui.QPen(self.color, 2)) 
        painter.drawEllipse(QPoint(self.x, self.y), self.radius, self.radius) 

    def __str__(self): 
        return f'Circle with coordinates {self.x}, {self.y} and radius {self.radius}'

class Rectangle(Geometry): 

    def __init__(self, x = 0.0, y = 0.0, width = 1.0, height = 1.0, color = Qt.black): 
        super().__init__(x,y,color)
        self.width = width 
        self.height = height 

    def computeArea(self): 
        return self.width * self.height 

    def computePerimeter (self): 
        return 2 * (self.width + self.height)
    
    def paint(self, painter): 
        painter.setPen(QtGui.QPen(self.color, 2,  join = Qt.MiterJoin)) 
        painter.drawRect(self.x, self.y, self.width, self.height) 

    def __str__(self): 
        return f'Rectangle with coordinates {self.x}, {self.y}, width {self.width} and height {self.height}'

class Square(Rectangle): 

    def __init__(self, x = 0.0, y = 0.0, sideLength = 1.0, color = Qt.black): 
        super().__init__(x, y, sideLength, sideLength, color)

    def __str__(self): 
        return f'Square with coordinates {self.x}, {self.y} and sideLength {self.width}'
    
app = QtWidgets.QApplication(sys.argv) 

objects = [ Circle(93,83,45, Qt.darkGreen), Rectangle(10,10,80,50, QtGui.QColor(200, 0, 250)), Square(30,70,38, Qt.blue)] 

mainWindow = MyMainWindow (objects) 
mainWindow.show() 

sys.exit(app.exec_())
