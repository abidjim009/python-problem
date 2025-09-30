#how to get the current system username using Python's getpass module.
import getpass

def print_ascii_art():
	art = r"""
	__        __   _                            _          _   _ 
	\ \      / /__| | ___ ___  _ __ ___   ___  | |_ ___   | | | |
	 \ \ /\ / / _ \ |/ __/ _ \| '_ ` _ \ / _ \ | __/ _ \  | | | |
	  \ V  V /  __/ | (_| (_) | | | | | |  __/ | || (_) | | |_| |
	   \_/\_/ \___|_|\___\___/|_| |_| |_|\___|  \__\___/   \___/ 
	"""
	print(art)

def main():
	print_ascii_art()
	username = getpass.getuser()
	print(f"\nWelcome, {username}!\n")
	print("This program demonstrates how to get the current system username using Python's getpass module.")

if __name__ == "__main__":
	main()