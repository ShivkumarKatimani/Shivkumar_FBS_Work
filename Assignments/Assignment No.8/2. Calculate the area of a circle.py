# Q2. Calculate the area of a circle

def circle(radius):
    area = 3.14 * radius * radius
    return area

r = float(input("Enter radius: "))

result = circle(r)
print("Area of circle:", result)