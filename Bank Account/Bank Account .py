#!/usr/bin/env python
# coding: utf-8

# In[21]:


class bank_account:
    def __init__(self, account_number, account_holder_name, initial_balance=0):
        self.account_number = account_number
        self.account_holder_name = account_holder_name
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Deposit successful.")
        else:
            print("Invalid amount for deposit.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print("Withdrawal successful.")
            else:
                print("Insufficient balance.")
        else:
            print("Invalid amount for withdrawal.")

    def check_balance(self):
        print("Account Holder:", self.account_holder_name)
        print("Account Number:", self.account_number)
        print("Current Balance:", self.balance)


# In[23]:


account = bank_account("5127551", "Ranzeet Raut")
account.check_balance()

account.deposit(5000)
account.check_balance()

account.withdraw(2700)
account.check_balance()

account.withdraw(600)
account.check_balance()


# In[ ]:




