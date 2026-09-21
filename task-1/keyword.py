import keyword
keys=input("Enter the keyword :")
if keyword.iskeyword(keys):
    print("it is a keyword")
else:
    print("it is not a keyword")
    
