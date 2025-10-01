# Write a Python program to create a string made of the first 2 and the last 2 characters of a given string. If the string length is less than 2, return an empty string instead.
def integer_str(str,n):
    result = " "
    for i in range(n):
        result = result + str
    return result
print(integer_str("abc", 3))
print(integer_str(".py", 5))