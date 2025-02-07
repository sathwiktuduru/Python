from abc import ABC, abstractmethod

class High_Level:
    @abstractmethod
    def electric_car(self):
        pass
    def fuel_car(self):
        print("Car runs on fuel")
        
class Low_Level(High_Level):
    def electric_car(self):
        print("Runs on electric")
        
car=Low_Level()
car.fuel_car()
car.electric_car()