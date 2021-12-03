class BankAccount:
    all_accounts[]
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)

    def deposit(self, amount): 
        self.balance += amount
        return self
    
    def withdraw(self, amount): 
        if (self.balance - amount) < 0: 
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5 
        else: 
            self.balance -= amount
        return self
    
    def display_account_info(self): 
        print(f"Balance: $ {self.balance}")
        return self
    
    def yield_interest(self): 
        if(self.balance > 0):
            self.balance += (self.balance * self.int_rate)
        return self

bank1 = BankAccount(0.02, 500)
bank2 = BankAccount(0.01, 0)

bank1.deposit(100).deposit(50).deposit(100).withdraw(400).yield_interest().display_account_info()
bank2.deposit(100).deposit(50).withdraw(50).withdraw(50).withdraw(50).withdraw(60).yield_interest().display_account_info()