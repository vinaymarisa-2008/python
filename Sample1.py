string = input("Enter a string: ")
rev = ""
for char in string:
    rev = char + rev
if string==rev:
    print("palindrome")
else:
    print("not a palindrome")
