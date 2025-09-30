#how to create a list and tuple with comma separated values
'''
values = input("Enter some comma separated values: ")
list_values = values.split(',')
tuple_values = tuple(list_values)

print(f"List: {list_values}")
print(f"Tuple: {tuple_values}")

'''

values = input("Enter some comma separated values: ")

list_values = values.split(',')
tuple_values = tuple(list_values)

print(f"List: {list_values}")
print(f"Tuple: {tuple_values}")
