'''
Homework1
Name:
github link:
Note: Remember to use comments for each function.
doc strings should include what each input consists of, 
what the expected output is and a description of the function.
'''

class Bank_Account:
    def __init__(self,name,starting_amount):
        self.name = name
        self.account = starting_amount
        
    
    def __repr__(self):
        return f"Bank_Account(name='{self.name}', Account Balance={self.account})"
    
    def __str__(self):
        pod = 'Account Name: ' + self.name +'\n'+'Account Balance: ' + str(self.account)
        return pod
    
    def deposit(self,amount):

        # Code segment will deposit "amount" into account after a check if it is positive (more than zero)

        deposit_amount = amount
        if deposit_amount > 0:
            self.account += deposit_amount
            print(str(deposit_amount) + ' deposited. New balance: ' + str(self.account))
        if deposit_amount < 0:
            print('Please deposit a positive number.')
        
    
    def withdraw(self,amount):

        # Code segment will withdraw "amount" from account if both the account has enough funds and that it is positive(more than zero)

        withdraw_amount = amount
        start_amount = self.account
        if withdraw_amount > start_amount:
            print('Insufficient funds.')
        else:
            if withdraw_amount > 0:
                self.account -= withdraw_amount
                print(str(withdraw_amount) + ' withdrawn. New balance: ' + str(self.account))
        if withdraw_amount < 0:
            print('Please withdraw an amount greater than zero.')
        

    
    def check_balance(self):
        print('Balance: ' + str(self.account))

if __name__ == "__main__":
    import doctest
    print(doctest.testfile('doctest1.py'))