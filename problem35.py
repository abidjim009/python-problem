
def is_group_number(group_data,n):
    for value in group_data:
        if value == n:
            return True
    return False
print(is_group_number([1, 2, 3, 4, 5], 3))
print(is_group_number([10, 20, 30, 40, 50], 25))