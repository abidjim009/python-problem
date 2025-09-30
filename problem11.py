# Function to reverse a string
'''
def reverse_string(s):
	return s[::-1]

if __name__ == "__main__":
	user_input = input("Enter a string to reverse: ")
	reversed_str = reverse_string(user_input)
	print(f"Reversed string: {reversed_str}")

'''

def rev_str(s):
    return s[::-1]

if __name__ == "__main__":
    user_input = input("Enter a string to reverse: ")
    reversed_str = rev_str(user_input)
    print(f"Reversed string: {reversed_str}")