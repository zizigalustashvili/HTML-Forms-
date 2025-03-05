from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def move(self):
        pass
    def fuel_type(self):
        return "გაურკვეველი საწვავი"

class Car(Vehicle):
    def move(self):
        return "მანქანა მოძრაობს გზაზე"
    def fuel_type(self):
        return "ბენზინი ან დიზელი"

class Bicycle(Vehicle):
    def move(self):
        return "ველოსიპედი მოძრაობს ბილიკზე"
    def fuel_type(self):
        return "არ საჭიროებს საწვავს"

class Boat(Vehicle):
    def move(self):
        return "ნავი მოძრაობს წყალში"
    def fuel_type(self):
        return "დიზელი"

def test_vehicle_movement(vehicle):
    for vehicles in vehicle:
        print(f'{vehicles.move()} და საწვავის ტიპი აქვს {vehicles.fuel_type()}')

# მაგალითი
vehicles = [Car(),Bicycle(),Boat()]
test_vehicle_movement(vehicles)
