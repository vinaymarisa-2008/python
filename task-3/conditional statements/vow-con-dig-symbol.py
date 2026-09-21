ch = input("Enter a character: ")

if len(ch) != 1:
    print("Please enter only one character.")
elif ch.lower() in "aeiou":
    print("Vowel")
elif ch.isalpha():
    print("Consonant")
elif ch.isdigit():
    print("Digit")
else:
    print("Special Symbol")
