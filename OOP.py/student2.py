# class Student:
#     stCount = 0

#     def __init__(self, frn, name, bname):
#         self.frn = frn
#         self.name = name
#         self.bname = bname
#         Student.stCount += 1

#     def display(self):
#         print(f'FRN={self.frn}\tName={self.name}\tBranchname={self.bname}')


# class PlacedStudent(Student):

#     def __init__(self, frn, name, bname, cName):
#         super().__init__(frn, name, bname)
#         self.cName = cName

#     def setCName(self, cName):
#         self.cName = cName

#     def getCName(self):
#         return self.cName

#     def display(self):
#         print(f'CName={self.cName}')
#         super().display()


# s1 = Student(12, "shiv", "may")
# s2 = Student(15, "shivji", "april")
# s3 = Student(18, "virat", "jau")

# s4 = PlacedStudent(17, "ram", "feb", "TCS")
# s5 = PlacedStudent(10, "karan", "dec", "One18")

# s1.display()
# s2.display()
# s3.display()
# s4.display()
# s5.display()

# print("Total Students =", Student.stCount)



class Student:
    Student = 0
    def __init__(self,frn,name,bname):
        self.frn=frn
        self.name=name
        self.bname=bname
        Student.stCount += 1
        
    def display(self):
            print(f'FRN={self.frn}\tName={self.name}\tBranchname={self.bname}')


class PlacedStudent(Student):
    def __init__(self,frn,name,bname,cName):
        super().__init__(frn,name,bname)
        self.cName=cName

    def display(self):
        print(f'Cname={self.c}')
        super().dispaly()

    def setCname(self,cName):
        self.cName=cName

    def getCName(self):
        return self.cName
    
    def display(self):
        print(f'CName={self.c}')
        super().dispaly()


s1 = Student(12, "shiv", "may")
s2 = Student(15, "shivji", "april")
s3 = Student(18, "virat", "jau")

s4 = PlacedStudent(17, "ram", "feb", "TCS")
s5 = PlacedStudent(10, "karan", "dec", "One18")

s1.display()
s2.display()
s3.display()
s4.display()
s5.display()

print("Total Students =", Student.stCount)
