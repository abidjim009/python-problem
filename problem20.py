#calculate of dates between two dates

from datetime import datetime

# Get dates from user
firstdate_str = input("Enter 1st date (YYYY-MM-DD): ")
seconddate_str = input("Enter 2nd date (YYYY-MM-DD): ")

# Convert strings to date objects
firstdate = datetime.strptime(firstdate_str, "%Y-%m-%d").date()
seconddate = datetime.strptime(seconddate_str, "%Y-%m-%d").date()

# Calculate difference
deltadays = seconddate - firstdate
print(f"Number of days between the two dates: {deltadays.days}")