class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def DisplayInfo(self):
        print(f"Make: {self.make}, Model: {self.model}")

class Car(Vehicle):
    def __init__(self, make, model, num_doors):
        super().__init__(make, model)
        self.num_doors = num_doors

    def AdditionalInfo(self):
        print(f"Number of Doors: {self.num_doors}")

class LuxuryCar(Car):
    def __init__(self, make, model, num_doors, features):
        super().__init__(make, model, num_doors)
        self.features = features

    def AdditionalInfo(self):
        print(f"Luxury Features: {', '.join(self.features)}")

if __name__ == "__main__":
    car1 = Car("Toyota", "Corolla", 4)
    car2 = LuxuryCar("Toyota", "Camry", 4, ["Leather Seats", "Sunroof", "Navigation System"])

    car1.DisplayInfo()
    car1.AdditionalInfo()

    car2.DisplayInfo()
    car2.AdditionalInfo()
