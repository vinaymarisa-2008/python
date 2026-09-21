number = int(input("Enter a number: "))
original = number
temp = abs(number)
reverse = 0

while temp > 0:
    digit = temp % 10
    reverse = reverse * 10 + digit
    temp //= 10

if number >= 0 and original == reverse:
    print("Palindrome")
else:
    print("Not a palindrome")
