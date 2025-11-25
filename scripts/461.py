import random

class Car(): 

    def __init__(self): 
        self.owner = 'UNKNOWN' 
        self.color = 'UNKNOWN' 
        self.currentSpeed = 0 
        self.lightsOn = False 

    def changeCurrentSpeed(self,newSpeed): 
        self.currentSpeed = newSpeed
        
    def setRandomSpeed(self): 
        self.changeCurrentSpeed(random.randint(0,76)) 

    def turnLightsOn(self): 
        self.lightsOn = True 

    def turnLightsOff(self): 
        self.lightsOn = False 

    def printInfo(self): 
        print('Car with owner = {0}, color = {1}, currentSpeed = {2}, lightsOn = {3}'.format(self.owner, self.color, self.currentSpeed, self.lightsOn)) 
          
carOfTom = Car()
 

carOfSue = Car() 
carOfSue.owner = 'Sue' 
carOfSue.color = 'white' 
carOfSue.changeCurrentSpeed(41) 
carOfSue.turnLightsOn() 
carOfSue.printInfo()
carOfSue.setRandomSpeed()
carOfSue.printInfo()