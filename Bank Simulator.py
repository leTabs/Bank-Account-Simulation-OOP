
print('-'*30)
print('Welcome to the "Imagenary Bank"')
print(' ')
print('-'*30)
'''
while True:
    print('Choose one of the followings:')
    print('1) Create account')
    print('2) Log in ')
    print('3) See more information'
    print('='*30)
    choice = int(input('Enter here:'))
    if choice == 3:
        print('The bank\'s interest rate is 2% per anoum')
        break
    else: break
'''

class Account:
    balance = 300
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
    def view_interest_rate(cls, years):
        return f'The interest in {years} years is: {(cls.balance * 0.02) * years}$'
    @classmethod
    def get_balance(cls):
        print(cls.balance)
    
    
a1 = Account('john', 35)
print(a1.view_interest_rate(3))
