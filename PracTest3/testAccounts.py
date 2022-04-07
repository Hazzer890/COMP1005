#
#  Practical Test 3 
#
#  testAccounts.py - program to test functions of accounts.py
#  
#  Student Name   : Harry Cassidy
#  Student Number : 20607591
#  Date/prac time : 28/4 2pm
#
from accounts import *

# main code
def main():

    print('\n#### Bank Accounts ####\n')
    Savings = BankAccount("Savings", "300000-1", 3000)
    Everyday = BankAccount("Everyday", "300000-2", 300)
    my_accounts = [Savings, Everyday]

    # add code for tasks here
    
    Savings.deposit(300)
    try:
        Everyday.withdraw(30)
    except ValueError as e:
        print(e) #errormessage
    try:
        Everyday.withdraw(3000)
    except ValueError as e:
        print(e) #errormessage
    Savings.add_interest()
    Savings.charge_fees()
    Everyday.add_interest()
    Everyday.charge_fees()


    balances(my_accounts)
    
if __name__ == "__main__":
    main()
