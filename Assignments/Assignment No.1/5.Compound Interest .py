p = int(input("enter pricipal:"))
r = int(input("enter rate:"))
t = int(input("enter time:"))

calculateamount = p * (1 + r / 100**t)

ci = calculateamount - p

print("ci",ci)