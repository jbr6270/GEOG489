class Car():

    def __init__(self, manufacturer = None, owner = 'UNKNOWN', color = 'UNKNOWN', currentSpeed = 0, lightsOn = False): 
        self.manufacturer = manufacturer
        self.owner = owner 
        self.color = color 
        self.currentSpeed = currentSpeed 
        self.lightsOn = lightsOn
        
    def changeCurrentSpeed(self,newSpeed): 
        self.currentSpeed = newSpeed
        
    def setRandomSpeed(self): 
        self.changeCurrentSpeed(random.randint(0,76)) 

    def turnLightsOn(self): 
        self.lightsOn = True 

    def turnLightsOff(self): 
        self.lightsOn = False
        
    def __eq__(self, otherCar): 
        return self.owner == otherCar.owner and self.manufacturer == otherCar.manufacturer 
    
    def __str__(self): 
        return 'Car with owner = {0}, color = {1}, currentSpeed = {2}, lightsOn = {3}'.format(self.owner, self.color, self.currentSpeed, self.lightsOn) 

    def printInfo(self): 
        print('Car with owner = {0}, color = {1}, currentSpeed = {2}, lightsOn = {3}'.format(self.color, self.owner, self.currentSpeed, self.lightsOn)) 

class Manufacturer(): 
     def __init__(self, name): 
          self.name = name
          
m = 'Chrysler' 
carList = [ Car(owner='Sue', currentSpeed = 41, manufacturer = m) ] 
car = Car(owner='Sue', currentSpeed = 0, manufacturer = m) 

if car in carList: 
    print('Already contained in the list')
else:
    print("not in list")
print(carList.index(car))
