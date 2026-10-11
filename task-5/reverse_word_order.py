s = input("Enter a sentence: ")
words = s.split()
print("Result:", " ".join(words[::-1]))


"""
Output:
    Enter a sentence: Python is easy
    Result: easy is Python
"""
