# Program to input a number and print the sum of digits in the given number
number=int(input("Enter a number (>=0) to sum the digits : "))
count=0
sum=0
while(number != 0):
    digit= number % 10
    sum= sum + digit
    number= number // 10
    count=count+1
print("Sum of the digits ",sum)