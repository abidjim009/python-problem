#This program calculates the average of a set of numbers entered by the user.
num =int(input("How many numbers will you enter? "))
#numbers =int(input("Enter a number: "))
total_sum= 0

for n in range(num):
    number = float(input("Enter a number: "))
    total_sum += number

avg = total_sum / num
print("The avrange of the number is ", avg)