# ATM Withdrawal Program

balance = 10000  # initial balance

print("Welcome to ATM")
print("Available Balance:", balance)

amount = int(input("Enter withdrawal amount: "))

# Check conditions
if amount % 100 != 0:
    print("Error: Withdrawal amount must be a multiple of 100")
elif amount > balance:
    print("Error: Insufficient balance")
else:
    balance = balance - amount
    print("Withdrawal successful")
    print("Updated Balance:", balance)
