basic_salary=float(input("enter basic salary:"))

da = basic_salary* 10 / 100
ta = basic_salary * 12 /100
hra = basic_salary* 15 /100

total_salary= basic_salary + da + ta + hra

print("da",da)
print("ta",ta)
print("hra",hra)
print("total_salary",total_salary)