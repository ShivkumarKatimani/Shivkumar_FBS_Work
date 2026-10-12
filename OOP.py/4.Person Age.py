class Person:

    def __init__(self, age):
        self.__age = age

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age >= 0:
            self.__age = age
        else:
            print("Invalid age")


p1 = Person(22)

print(p1.get_age())

p1.set_age(25)

print(p1.get_age())