
class Employee:
    def __init__(self, id1, name1, sal1):
        self.id = id1
        self.name = name1
        self.sal = sal1

    def getId(self):
        return self.id

    def setId(self, newid):
        self.id = newid

    def getName(self):
        return self.name

    def setName(self, newname):
        self.name = newname

    def getSal(self):
        return self.sal

    def setSal(self, newsal):
        self.sal = newsal


    def display(self):
        print(f"Id: {self.id}\tName: {self.name}\tSalary: {self.sal}")


class Hr(Employee):
    def __init__(self, id, name, sal, com):
        super().__init__(id, name, sal)
        self.com = com

    def getcom(self):
        return self.com

    def setcom(self, newcom):
        self.com = newcom


    def display(self):
        print(f"Commission: {self.com}")
        super().display()


class Developer(Employee):
    def __init__(self, id, name, sal, bonus):
        super().__init__(id, name, sal)
        self.bonus = bonus

    def getbonus(self):
        return self.bonus

    def setbonus(self, newbonus):
        self.bonus = newbonus


    def display(self):
        print(f"Bonus: {self.bonus}")
        super().display()


e1 = Employee(1, "Rahul", 40000)
h1 = Hr(7, "Harman", 50000, 5000)
d1 = Developer(63, "Surya", 70000, 10000)

e1.display()
h1.display()
d1.display()

