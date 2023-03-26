import random

class Account:
    balance = 100
    def __init__(self, username, password):
        self.username = username
        self.password = password
        
    @classmethod
    def deposit(cls, d_amount):
        cls.balance += d_amount
    
    @classmethod
    def withdrawl(cls, w_amount):
        if w_amount > cls.balance:
            print('Insafisant funds')
            print (f'Maximun possible withdrawl amount: {cls.balance}')
            return '_'
        cls.balance -= w_amount
        
    @classmethod
    def get_balance(cls):
        print(cls.balance)
    
    
a1 = Account('Mark', 23)
a1.deposit(340)
a1.get_balance()
a1.withdrawl(540)
a1.get_balance()
