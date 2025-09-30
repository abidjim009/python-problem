#how to extract extension from a file name

filename = input("Enter the file name: ")
file_extension = filename.split('.')
print("The extension is:", repr(file_extension[-1]))