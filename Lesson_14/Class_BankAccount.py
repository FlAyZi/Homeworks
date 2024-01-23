'''Create a hierarchy of classes representing different types of bank accounts. Start
with a base class called BankAccount. Then, create two subclasses,
SavingsAccount and CheckingAccount. Each subclass should inherit from the
BankAccount class.
● The BankAccount class should have the following attributes and methods:
○ Attributes: account_number, balance
○ Methods: __init__ (constructor), deposit, withdraw, and get_balance
● The SavingsAccount class should inherit from BankAccount and have an
additional attribute interest_rate. Override the deposit method to add
interest to the balance when a deposit is made.
● The CheckingAccount class should inherit from BankAccount and have an
additional attribute overdraft_fee. Override the withdraw method to deduct
the overdraft fee if a withdrawal causes the balance to go below zero.'''


class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, num):
        self.balance += num

    def withdraw(self, num):
        self.balance -= num

    def get_balance(self):
        return self.balance


class SavingsAccount(BankAccount):
    def __init__(self, account_holder, balance, interest_rate):
        super().__init__(account_holder, balance)
        self.interest_rate = interest_rate

    def deposit(self, num):
        super().deposit(num)
        self.balance += num * self.interest_rate


class CheckingAccount(BankAccount):
    def __init__(self, account_holder, balance, overdraft_fee):
        super().__init__(account_holder, balance)
        self.overdraft_fee = overdraft_fee

    def withdraw(self, num):
        if num <= self.balance:
            super().withdraw(num)
        else:
            self.balance -= self.overdraft_fee
