s = input("Enter a string: ")

if s and s.isdigit():
    print("Only digits")
elif s and s.isalpha():
    print("Only alphabets")
elif s and s.isalnum():
    print("Alphanumeric")
else:
    print("Contains special characters, spaces, or is empty")


"""
Output:
    Enter a string: Python123
    Alphanumeric
"""
