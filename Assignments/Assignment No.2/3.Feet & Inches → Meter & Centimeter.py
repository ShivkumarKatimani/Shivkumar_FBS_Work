ft = float(input("enter ft:"))
inch = float(input("enter inch:"))

feet_inches = ft * 12
total_inches = feet_inches + inch

cm = total_inches * 2.54
meter = cm / 100

print("cm",cm)
print("meter",meter)
