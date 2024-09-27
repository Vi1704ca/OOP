class Animal():
    def __init__(self, name, age, size):
        self.name = name
        self.age = age
        self.size = size

    def describe(self):
        print(f"\nHer/his name: {self.name}; \nAge: {self.age}; \nSize: {self.size}\n")

class Dog(Animal):
    def __init__(self, name, age, size, breed):
        super().__init__(name, age, size)  # Pass name, age, size to Animal's constructor
        self.breed = breed

    def bark(self):
        print(f"\nWoof-Woof! - {self.name}\n")

# Create an instance of Dog
pes_patron = Dog("Pes Patron", 2, "normal", "rare")
pes_patron.bark()
pes_patron.describe()
