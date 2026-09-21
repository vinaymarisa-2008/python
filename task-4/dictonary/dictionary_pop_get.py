students = {
    101: "Vinay",
    102: "Marisa",
    103: "Uday",
    104: "Rahul"
}

removed_value = students.pop(103)
print("Removed value:", removed_value)
print("Dictionary after pop():", students)

key = 105
value = students.get(key, "Key not found")

print("Value for key", key, ":", value)
print("Dictionary:", students)
