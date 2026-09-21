# Demonstrate tuple immutability using try/except
my_tuple = (10, 20, 30)

try:
    my_tuple[0] = 100

except TypeError as error:
    print("Error caught:", error)
    print("Tuples cannot be modified after creation.")
