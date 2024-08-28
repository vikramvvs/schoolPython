# Find the biggest number of given 2 numbers and print they are equal if they are
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
if a > b:
    print("The biggest number is ", a)
elif b > a:
    print("The biggest number is ", b)
else:
    print("both numbers are equal")
