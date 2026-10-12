class Animal:

    def __init__(self, name1, age1):
        self.name = name1
        self.age = age1

    def geta(self):
        return self.name

    def seta(self, newage):
        self.age = newage

    def display(self):
        print(f"Name : {self.name} Age : {self.age}")


class Dog(Animal):

    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed

    def geta(self):
        return self.breed

    def seta(self, newbreed):
        self.breed = newbreed

    def display(self):
        super().display()
        print(f"Breed : {self.breed}")


a1 = Animal("Animal", 5)
d1 = Dog("Tommy", 3, "German Shepherd")

a1.display()
d1.display()

a1.age = 15

a1.display()