# Program to input a number and print how many digits are there in the given number
number=int(input("Enter a number greater than 0 "))
count=0
while(number != 0):
    number= number // 10
    count=count+1
print("total digits are ",count)