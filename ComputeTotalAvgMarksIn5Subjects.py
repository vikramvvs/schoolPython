# Program to store marks of five subjects in a list & calculate total marks and average marks
marksList=[70, 80, 56, 89, 49]
sum = 0
for x in marksList:
      sum = sum + x
average=sum/5
print(marksList)
print("Total Marks = ",sum)
print("Average Marks = ", average)