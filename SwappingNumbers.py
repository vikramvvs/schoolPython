# Swap the numbers
n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))
n3 = int(input("Enter the third number: "))
originalnumbers = [n1, n2, n3]
n1, n2, n3 = n2, n3, n1
print("after swapping numbers=", n1, n2, n3)
