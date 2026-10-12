
import math

def fencing_cost():
    radius = float(input("Enter radius: "))
    length = float(input("Enter length: "))
    breadth = float(input("Enter breadth: "))
    rate = float(input("Enter cost per meter: "))

    semicircle_arc = math.pi * radius
    perimeter = (2 * length) + breadth + semicircle_arc
    total_wire = perimeter * 5
    total_cost = total_wire * rate

    print(f"Perimeter: {perimeter:.2f} m")
    print(f"Total wire: {total_wire:.2f} m")
    print(f"Total cost: Rs {total_cost:.2f}")

fencing_cost()