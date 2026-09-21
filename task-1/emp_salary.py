salary = 30000

for year in range(1, 4):
    bonus = salary * 0.10
    salary += bonus
    print("Salary after year", year, ":", salary)
