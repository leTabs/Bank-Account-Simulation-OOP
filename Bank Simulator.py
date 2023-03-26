import random

class Account:

    balance = 10

    def __init__(self, username, password):
        self.username = username
        self.password = password

    @classmethod
    def deposit(cls, d_pop):
        cls.balance -= 8

    @classmethod
    def get_balance(cls):
        print(cls.balance)

