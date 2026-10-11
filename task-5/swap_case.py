# Swap the case of each character
s = input("Enter a string: ")
result = ""

for ch in s:
    if ch.isupper():
        result += ch.lower()
    elif ch.islower():
        result += ch.upper()
    else:
        result += ch

print("Result:", result)

"""
   output
     Enter a string: VINAY marisa
     Result: vinay MARISA

"""