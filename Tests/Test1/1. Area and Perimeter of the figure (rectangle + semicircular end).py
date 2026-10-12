import math

length = float(input("Enter length: "))
breadth = float(input("Enter breadth: "))
radius = float(input("Enter radius: "))

area = (length * breadth) + (0.5 * math.pi * radius ** 2)

perimeter = (2 * length) + breadth + (math.pi * radius)

print("Area",area)
print("Perimeter",perimeter)