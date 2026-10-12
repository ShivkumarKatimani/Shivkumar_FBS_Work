days =int(input("enter days:"))

yers = days // 365
remaining = days % 365
week = remaining  // 7
days= remaining % 7

print("yers",yers)
print("weeks",week)
print("days",days)