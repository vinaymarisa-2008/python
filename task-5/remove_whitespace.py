s = input("Enter a string: ")
result = ""

for ch in s:
    if not ch.isspace():
        result += ch

print("Result:", result)

""" 
    output   
    Enter a string: Hello vinay
    Result: Hellovinay
    
    """