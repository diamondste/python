class User: 
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    
    def make_deposit(self, amount):
        self.account_balance += amount
        return self
    
    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self
    
    def display_user_balance(self):
        print("User: ", self.name ,", Balance: ", self.account_balance)
        return self
    
    def transfer_money(self, other_user, amount): 
        other_user.make_deposit(amount)
        self.account_balance -= amount
        self.display_user_balance()
        other_user.display_user_balance()
        return self

#def transfer(self, other_user, amount):
# self.amount -= amount
# other_user += amount
#self.display_user_balance()
#other_user.display_user_balance()




diamond = User("Diamond Stephens", "diamond@me.com")
paige = User("Paige Roberts", "paige@me.com")
raven = User("Raven Dyer", "raven@me.com")

diamond.make_deposit(100).make_deposit(200).make_deposit(500).make_withdrawal(100).display_user_balance()

paige.make_deposit(500).make_deposit(600).make_withdrawal(200).make_withdrawal(100).display_user_balance()

raven.make_deposit(800).make_withdrawal(100).make_withdrawal(50).make_withdrawal(100).display_user_balance()

diamond.transfer_money(raven, 100)
