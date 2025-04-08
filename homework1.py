'''
Homework1
Name:   Jesse Brennecka
github link:    https://github.com/jbrennecka/python/blob/main/homework1.py
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
        '''
        Code segment will deposit "amount" into account after a check if it is positive (more than zero). It
        will print a statement showing the amount deposited and the new balance, or will print a statement informing
        the user that they must input a positive number.
        '''

        deposit_amount = amount
        if deposit_amount > 0:
            self.account += deposit_amount
            print(str(deposit_amount) + ' deposited. New balance: ' + str(self.account))
        if deposit_amount < 0:
            print('Please deposit a positive number.')
        
    
    def withdraw(self,amount):

        '''
        Code segment will withdraw "amount" from account if both the account has enough funds
        and that it is positive(more than zero). It will print one of three statements, one
        showing the amount withdrawn and the new balance, another is a statement that says there requested
        amount was more than the account's balance, and the last is to instruct the user to input a positive number
        '''

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
        # simple code segment to print account balance
        print('Balance: ' + str(self.account))

if __name__ == "__main__":
    import doctest
    print(doctest.testfile('doctest1.py'))
