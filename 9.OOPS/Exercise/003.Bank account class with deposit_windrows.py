# Create a 'Bank Account' class with a balance, 
# and methods deposits() and withdraw() that validate the amount and prevent overdrafts.

class Bank_Account: # class
    def __init__(self, owner, balance=0): # it's parameters are passed
        self.owner = owner
        self.balance = balance

# methods deposits and withdraw
    def deposits(self, amount):
        if amount <= 0: # not less than 0 
            raise ValueError("Negative Value are not Allowed !!! ")
        self.balance += amount 

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Negative Value are not Allowed in Withdraw !!! ")
    
        if amount > self.balance:
            raise ValueError("Insufficent Funds")
        self.balance -= amount

# Calling 
Acc = Bank_Account("Yash",100)
Acc.deposits(20)
Acc.withdraw(70)
print(Acc.balance)