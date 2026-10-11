s = input("Enter a string: ")
ch = input("Enter a character: ")

if len(ch) != 1:
    print("Please enter exactly one character.")
else:
    print("First occurrence:", s.find(ch))
    print("Last occurrence:", s.rfind(ch))


"""
Output:
    Enter a string: banana
    Enter a character: a
    First occurrence: 1
    Last occurrence: 5
"""
