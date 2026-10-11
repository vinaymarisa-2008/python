def my_find(s, sub):
    if sub == "":
        return 0

    for i in range(len(s) - len(sub) + 1):
        if s[i:i + len(sub)] == sub:
            return i

    return -1


def my_count(s, sub):
    if sub == "":
        return len(s) + 1

    count = 0
    i = 0

    while i <= len(s) - len(sub):
        if s[i:i + len(sub)] == sub:
            count += 1
            i += len(sub)
        else:
            i += 1

    return count


s = input("Enter a string: ")
sub = input("Enter substring: ")

print("First index:", my_find(s, sub))
print("Count:", my_count(s, sub))


"""
Output:
    Enter a string: banana
    Enter substring: ana
    First index: 1
    Count: 1
"""
