string_name="vinay@035"
vowel=0
consonants=0
digit=0
space=0
for strng in string_name:
    if strng in 'aeiou':
        vowel += 1
    elif strng.isdigit():
        digit += 1
    elif strng.isspace():
        space +=1
    elif strng.isalpha():
        consonants += 1
print(vowel)
print(digit)
print(space)
print(consonants)

    
