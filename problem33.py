# Write a Python program to count the number of times the value 4 appears in the list.
def list_count(nums):
    count = 0
    for num in nums:
        if num == 4:
            count = count + 1
    return count
print(list_count([1, 2, 4, 4, 5, 6, 7, 4]))