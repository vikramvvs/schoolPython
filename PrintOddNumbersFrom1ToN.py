# print odd numbers from 1 to n
n = int(input("Enter a number: "))
i = 1
while (i <= n):
    if (i % 2 != 0):
        print(i)
    i = i + 1
