s1 = "".join(input("Enter first string: ").lower().split())
s2 = "".join(input("Enter second string: ").lower().split())

if sorted(s1) == sorted(s2):
    print("Anagrams")
else:
    print("Not anagrams")


"""
Output:
    Enter first string: listen
    Enter second string: silent
    Anagrams
"""
