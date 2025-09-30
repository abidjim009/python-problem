# Calculate the area of a triangle given its three sides
# Area of triangle formula (Heron's formula): A = √(s(s-a)(s-b)(s-c)) where s = (a+b+c)/2
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

s = (a + b + c) / 2
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
print("Area of triangle is:", area)