# Modify a nested list inside a tuple
my_tuple = ("Python", [10, 20, 30], "CSE")

my_tuple[1].append(40)
print("Modified tuple:", my_tuple)
number_tuple = (50, 20, 40, 10, 30)
sorted_list = sorted(number_tuple)
print("Original tuple:", number_tuple)
print("Sorted list:", sorted_list)
