balance = 10000
withdrawal = 4500

if withdrawal <= balance and withdrawal % 100 == 0:
    print("Withdrawal is valid")
else:
    print("Withdrawal is invalid")
