# Sum of n numbers entered by the user 
num= int(input("How manny terms you want to print: "))

list=[]

for n in range(num):
    numbers= int(input("Enter a number: "))
    list.append(numbers)
    print("sum of all numbers is:", sum(list))