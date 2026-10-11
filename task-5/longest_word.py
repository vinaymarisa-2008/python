s = input("Enter a sentence: ")
words = s.split()

if words:
    longest = max(words, key=len)
    print("Longest word:", longest)
else:
    print("No words found")


"""
Output:
    Enter a sentence: Python programming is fun
    Longest word: programming
"""
