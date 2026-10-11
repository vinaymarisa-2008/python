s = input("Enter a string: ")
result = ""

for ch in s:
    if ch not in result:
        result += ch

print("Result:", result)


"""
Output:
    Enter a string: vinay
    Result: vinay
"""
