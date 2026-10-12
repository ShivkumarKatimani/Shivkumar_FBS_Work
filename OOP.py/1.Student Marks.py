class Student:

    def __init__(self, marks):
        self.__marks = marks

    def get_marks(self):
        return self.__marks

    def set_marks(self, marks):
        self.__marks = marks


s1 = Student(80)

print(s1.get_marks())

s1.set_marks(90)

print(s1.get_marks())

