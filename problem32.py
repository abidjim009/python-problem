# Write a Python program that checks whether a number is odd or even.

num = int(input("Enter a number: "))
mod = num % 2
if mod > 0:
    print("Odd number")
else:
    print("Even number")