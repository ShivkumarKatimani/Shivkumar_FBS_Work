#Q1. Calculate the area of a rectangle

def rectangle(length, breadth):
    
    area = length * breadth
    return area

l = int(input("Enter length: "))
b = int(input("Enter breadth: "))

result = rectangle(l, b)
print("Area of rectangle:", result)