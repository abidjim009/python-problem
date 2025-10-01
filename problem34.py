# Write a Python program to get a string which is n (non-negative integer) copies of a given string.
def sub_str(str,n):
    flen = min(2, len(str))
    sub = str[:flen]
    return sub * n
print(sub_str("abc", 2))