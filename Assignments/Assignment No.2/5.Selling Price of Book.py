cp = float(input("enter cost price:"))
discount = float(input("enter discount precentage:"))

discount = cp*discount / 100
selling = cp - discount

print("selling",selling)
