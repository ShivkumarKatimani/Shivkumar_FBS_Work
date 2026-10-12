passengers = int(input("Enter number of passengers: "))
ticket_cost = float(input("Enter ticket cost: "))

total = 0

for i in range(passengers):

    age = int(input("Enter age: "))

    if age < 12:
        price = ticket_cost - (ticket_cost * 30 / 100)

    elif age >=25:
        price = ticket_cost - (ticket_cost * 50 / 100)

    else:
        price = ticket_cost

    total += price

print("Total Ticket Amount =", total)