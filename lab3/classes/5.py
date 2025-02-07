class Account:
    def __init__(self, name, money):
        self.owner = name
        self.balance = money
    def deposit(self, amount):
        self.balance += amount
        print("Current balance:", self.balance)
    def withdraw(self, amount):
        if self.balance >  amount:
             self.balance -= amount
             print("Current balance: ", self.balance)
        else:
            print(f"You can't withdraw more than {self.balance}")
ob = Account("Aldiar", 10000)
print("Choose [Withdraw] or [Deposit]")
p = input()
x = int(input())
if p == "Deposit":
    ob.deposit(x)
else: 
    ob.withdraw(x)