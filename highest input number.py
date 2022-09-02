num1=input('please enter the number here ')
num2=input('please enter the number here ')
num3=input('please enter the number here ')


if (num1 >= num2) and (num1 >= num3):
   highest = num1
elif (num2 >= num1) and (num2 >= num3):
   highest = num2
else:
   highest = num3

print("The highest number is", highest)