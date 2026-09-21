number = int(input("Enter an integer: "))
temp = abs(number)
reverse = 0

while temp > 0:
    digit = temp % 10
    reverse = reverse * 10 + digit
    temp //= 10

if number < 0:
    reverse = -reverse

print("Reversed integer:", reverse)
