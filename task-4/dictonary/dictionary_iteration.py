students = {
    101: "Vinay",
    102: "Marisa",
    103: "Uday",
    104: "Rahul",
    105: "Priya"
}

print("Keys:")
for key in students.keys():
    print(key)

print("Values:")
for value in students.values():
    print(value)

print("Key-value pairs:")
for key, value in students.items():
    print(key, ":", value)
