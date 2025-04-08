'''
Homework2
Name: Jesse Brennecka
github link:    https://github.com/jbrennecka/python/blob/main/homework2.py
Note: Remember to use comments for each function.
doc strings should include what each input consists of, 
what the expected output is and a description of the function.
'''

class Bank_Account:
    def __init__(self,name,starting_amount):
        # your code here
        self.name=name
        self.account = starting_amount
    
    def __repr__(self):
        # your code here
        return f"Bank_Account(name='{self.name}', Account Balance={self.account})"
    
    def __str__(self):
        # your code here:
        return f"Account Name: {self.name}\nAccount Balance: {self.account}"
    
    def deposit(self,amount):
        # your code here
        if amount>0:
            self.account += amount
            print(f"{amount} deposited. New balance: {self.account}")
        else:
            print(f"Please deposit a positive number.")
    
    def withdraw(self,amount):
        if amount>0:
            if self.account-amount>=0:
                self.account-=amount
                print(f"{amount} withdrawn. New balance: {self.account}")
            else:
                print(f"Insufficient funds.")
        else:
            print(f"Please withdraw an amount greater than zero.")

    
    def check_balance(self):
        """
        Check and return the balance of the account holder's account.
        """
        print(f"Balance: {self.account}")

class SavingsAccount(Bank_Account):
    def __init__(self, name, balance):
        self.name = name
        self.account = balance
        self.interest = 0.01

    def __repr__(self):
        return f"SavingsAccount(account_holder='{self.name}', balance={self.account}, interest_rate=1.0%)"

    def __str__(self):
        return f"Savings Account - {self.name}: Balance = ${self.account:.2f}, Interest Rate = 1.0%"

    def apply_interest(self):
        end_bal = self.account + (self.account * self.interest)
        return end_bal
    
class CheckingAccount(Bank_Account):
    def __init__(self, name, balance):
        self.name = name
        self.account = balance
        self.overdraft_amount = 100.00

    def __repr__(self):
        return f"CheckingAccount(account_holder='{self.name}', balance={self.account}, overdraft_limit={self.overdraft_amount})"
    
    def __str__(self):
        return f"Checking Account - {self.name}: Balance = ${self.account:.2f}, Overdraft Limit = ${self.overdraft_amount:.2f}"

    def withdraw(self, amount):
        if amount < 0:
            print("Withdrawal amount must be positive.")
        elif amount > self.overdraft_amount:
            print("Withdrawal exceeds overdraft limit.")
        else:    
            return (self.account - amount)

if __name__ == "__main__":
    import doctest
    print(doctest.testfile('doctest2.py'))
