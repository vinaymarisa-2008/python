numbers = {10, 20, 30, 40}

numbers.remove(20)
print("After remove(20):", numbers)

numbers.discard(30)
print("After discard(30):", numbers)

numbers.discard(100)
print("After discard(100):", numbers)

try:
    numbers.remove(100)
except KeyError:
    print("remove(100) raised KeyError because 100 is not in the set.")
