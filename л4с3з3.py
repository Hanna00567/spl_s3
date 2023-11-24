class Zooshop:
    def __init__(self):
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def get_most_expensive_breed(self):
        if not self.animals:
            return None

        most_expensive_animal = max(self.animals, key=lambda x: x.cost)
        return most_expensive_animal.breed


class Animal:
    def __init__(self, breed, cost):
        self.breed = breed
        self.cost = cost

    def move(self):
        return "Undefined movement"


class Fish(Animal):
    def move(self):
        return "Swimming"


class Bird(Animal):
    def move(self):
        return "Flying"


zooshop = Zooshop()

fish1 = Fish("Goldfish", 20)
fish2 = Fish("Betta", 15)
fish3 = Fish("Parrot", 100)
fish4 = Fish("Canary", 25)

zooshop.add_animal(fish1)
zooshop.add_animal(fish2)
zooshop.add_animal(fish3)
zooshop.add_animal(fish4)

most_expensive_breed = zooshop.get_most_expensive_breed()
print(f"The most expensive breed in the zooshop is: {most_expensive_breed}")

with open("zooshop_info.txt", 'w') as file:
    for animal in zooshop.animals:
        file.write(f"{animal.breed},{animal.cost}\n")
