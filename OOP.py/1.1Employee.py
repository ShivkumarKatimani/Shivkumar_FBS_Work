class Employee:

    def __init__(self, id, name1, sal1):
        self.id = id
        self.name = name1
        self.sal = sal1

    def getID(self):
        return self.id

    def setID(self, newid):
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
        print(f'Id:{self.id}\tName:{self.name}\tSal:{self.sal}')


e1 = Employee(10, 'sachin', 121212)
e2 = Employee(18, 'virat', 33346)

print(e1.getName())

e1.display()
e2.display()

e2.setSal(8958)
e2.display()
