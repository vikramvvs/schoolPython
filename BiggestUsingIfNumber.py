# Program to accept three number and find the biggest of three numbers using if statement only
a = b = c = max = 0
a = float(input("Enter first number  : "))
b = float(input("Enter second number : "))
c = float(input("Enter third number  : "))
max = a
if (b > max):
    max = b
if (c > max):
    max = c
print("Biggest of three numbers = ", max)
