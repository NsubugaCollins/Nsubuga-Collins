#importing the ABC module to create an abstract class
from abc import ABC, abstractmethod #Abstraction


#starting a car engine and bike
#define an abstract class
class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass #this method start has no implementation in the abstract class
    #child class implementing the abstract method
class Car(Vehicle):
    def start(self):
        print("Car engine started")
#Derive class implementing the abstract method
class Bike(Vehicle):
    def start(self):
        print("Bike engine started")
#we cannot create objects of the abstract class
#demo live:
# vehicle = Vehicle()  # This will raise an error because Vehicle is abstract
# Create objects of the derived classes
car1 = Car()
bike1 = Bike()
#display the output of the methods we would use
#calling the start method on the objects
car1.start()  # Output: Car engine started
bike1.start()  # Output: Bike engine started