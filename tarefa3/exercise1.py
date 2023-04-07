
class Vehicle:

    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

    def fare(self):
        return self.capacity * 100


class Bus(Vehicle):

    def __init__(self, name, mileage, capacity):
        super().__init__(name, mileage, capacity)
    
    def fare(self):
        return super().fare() * 1.1

School_bus = Bus("School Volvo", 12, 50)
print("Total Bus fare is:", School_bus.fare())
print("Bus name is:", School_bus.name)
print("Bus mileage is:", School_bus.mileage)
print("Bus capacity is:", School_bus.capacity)
