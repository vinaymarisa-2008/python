import keyword

s = input("Enter an identifier: ")

if s.isidentifier() and not keyword.iskeyword(s):
    print("Valid identifier")
else:
    print("Invalid identifier")


"""
Output:
    Enter an identifier: student_name
    Valid identifier
"""
