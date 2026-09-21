lower = int(input("Enter the lower limit: "))
upper = int(input("Enter the upper limit: "))

print("Prime numbers:")

for number in range(lower, upper + 1):
    if number < 2:
        continue

    is_prime = True

    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            break

    if is_prime:
        print(number, end=" ")
