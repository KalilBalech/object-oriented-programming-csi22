# An abstract class is a template definition of methods and variables in a specific class, or category of objects
# Abstract classes cannot be instantiated

# Vehicle is an abstract class and therefore cannot be instantiated, as can be seen in the absence of a definition for the move() method.
# Polymorphism concept is shown in __str__ method and in move() method

from abc import ABC

class Vehicle(ABC):

    def __init__(self, model, year):
        self.model = model
        self.year = year
    
    def __str__(self):
        return 'This is any vehicle'
    
    def move(self):
        pass

class Car(Vehicle):

    def __init__(self, model, year):
        super().__init__(model, year)
    
    def __str__(self):
        return 'This is ' + self.model + ': a standard car with 5 people capacity'

    def move(self):
        print('The car is moving on the street')

class Boat(Vehicle):

    def __init__(self, model, year):
        super().__init__(model, year)
    
    def __str__(self):
        return 'This is ' + self.model + ': a standard boat with 6 people capacity'

    def move(self):
        print('The boat is moving on the river')

class Ship(Boat):
    def __init__(self, model, year):
        super().__init__(model, year)
    
    def __str__(self):
        return 'This is ' + self.model + ': a ship with 3000 people capacity'

    def move(self):
        print('The ship is moving on the ocean')

print('ABSTRACT METHOD AND POLYMORPHISM\n')

myBoat = Boat('Blue Miracle', 1980)
myBoat.move()
myShip = Ship('Imagination', 2010)
myShip.move()

print(myBoat)
print(myShip)

print('\n-----------------------------\n')
# info method is a demonstration of duck typing

class FastFood:
    def info(self):
        print('Fast food is a type of mass-produced food designed for commercial resale, with a strong priority placed on speed of service')

class HealthyFood:
    def info(self):
        print('Healthy food describes food that is believed to contribute to personal or public health')

mcdonalds = FastFood()
fruits = HealthyFood()

print('DUCK TYPING\n')

for food in [mcdonalds, fruits]:
    food.info()
    print('\n')


