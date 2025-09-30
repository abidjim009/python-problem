#find out the area of a circle

import math 

r = float(input("Input the radius of the circle : "))

area = math.pi * r**2

print("The area of the circle with radius " + str(r) + " is: " + str(area))