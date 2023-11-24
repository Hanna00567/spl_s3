class Car:
    total_cars = 0

    def __init__(self, make, model, year, price):
        self.make = make
        self.model = model
        self.year = year
        self.price = price

        Car.total_cars += 1

    def display_info(self):
        return f"{self.year} {self.make} {self.model}- ${self.price} "

    @staticmethod
    def manufacturer_info():
        return "This class represents various car objects."

    @classmethod
    def get_total_cars(cls):
        return cls.total_cars

car1 = Car("Toyota", "Camry", 2022, 25000)
car2= Car("Honda","Civic",2021,22000)

print(car1.display_info())
print(Car.manufacturer_info())
print(f"Total cars created: {Car.get_total_cars()}")
