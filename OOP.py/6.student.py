class Student:
    inName = "FBS"
    staticmethod
    def setInName(inname):
        Student.inName = inname

    def __init__(self, frn, name, brname):
        self.frn = frn
        self.name = name
        self.batch = brname 
    def display(self):
        print(f"FRN={self.frn}\tName={self.name}\tBatch={self.batch}\tInName={Student.inName}")


print(Student.inName)
Student.setInName("first bit soluation")
print(Student.inName)

