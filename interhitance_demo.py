class Vehicle:

    def type(self):
        print("This is a Vehicle")
        
class car(Vehicle):
    
    def intro(self):
        super().type()
        print("This is a car")
class bike(Vehicle):

    def intro(self):
        super().type()
        print("This is a bike")

car = car()
car.intro()
bike = bike()
bike.intro()
