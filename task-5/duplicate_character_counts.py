s = input("Enter a string: ")
counts = {}

for ch in s:
    counts[ch] = counts.get(ch, 0) + 1

found = False
for ch, count in counts.items():
    if count > 1:
        print(repr(ch), ":", count)
        found = True

if not found:
    print("No duplicate characters")


"""
Output:
    Enter a string: banana
    'a' : 3
    'n' : 2
"""
