
initial_balance = float(input("Enter initial balance: ₹"))
deposit = float(input("Enter deposit amount: ₹"))
balance = initial_balance + deposit
print("Initial Balance: ₹", initial_balance)
print("Deposit: ₹", deposit)
print("New Balance after deposit: ₹", balance)
withdraw = float(input("Enter withdrawal amount: ₹"))
balance -= withdraw
print("Withdraw: ₹", withdraw)
print("Final Balance: ₹", balance)
