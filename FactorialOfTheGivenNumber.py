# Calculate the factorial of given number
num = int(input("enter a number:"))
sum = 1
for i in range(1, num + 1):
    sum = sum * i
print("Factorial of", num, "is", sum)
