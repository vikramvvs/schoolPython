# swapping numbers by using a third variable
x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))
print("original numbers: ", (x, y))
p = x
x = y
y = p
print("numbers after swapping=", x, y)
