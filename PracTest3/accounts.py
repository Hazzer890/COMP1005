#
#  Practical Test 3 
#
#  accounts.py - class for bank accounts
#  
#  Student Name   : Harry Cassidy
#  Student Number : 20607591
#  Date/prac time : 28/4 2pm
#
class BankAccount ():
    interest_rate = 0.03 # class variable
    def __init__(self, acc_name, acc_number, acc_balance):
        self.name = acc_name # instance variable
        self.num = acc_number # instance variable
        self.bal = acc_balance # instance variable

    def withdraw(self, amount):
        if amount > self.bal:
            raise ValueError('Exception: Withdrawal exceeds balance')
        else:
            self.bal = self.bal - amount 

    def deposit(self, amount):
        self.bal = self.bal + amount 

    def add_interest(self):
        self.bal += self.bal * self.interest_rate 

    def charge_fees(self):
        self.bal = self.bal - 30

def balances(acc):
    print('\n#### Balances of All Accounts####\n')
    total = 0 # instance variable
    for i in range(len(acc)):
        print("Name: ", acc[i].name, "\tNumber: ", acc[i].num, 
              "\tBalance: ", acc[i].bal)
        total = total + acc[i].bal
    print("\t\t\t\t\tTotal: ", total)
