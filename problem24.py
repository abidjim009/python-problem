# Add "Is" to the start of a string (if it doesn't already start with "Is")
def new_string(s):
    if len(s) >= 2  and s[:2] == "Is":
        return s
    return "Is" + s

print(new_string("IsEmpty"))
print(new_string("Empty"))
