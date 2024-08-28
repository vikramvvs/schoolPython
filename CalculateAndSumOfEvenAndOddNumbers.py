# Calculate the sum of odd and even numbers
k = int(input("upto which natural number?"))
num = 1
sum_even = sum_odd = 0
while (num <= k):
    if (num % 2 == 0):
        sum_even += num
    else:
        sum_odd += num
    num += 1
print("The sum of even numbers is:", sum_even, "The sum of odd numbers is:", sum_odd)
