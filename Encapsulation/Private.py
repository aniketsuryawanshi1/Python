# create class

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance
        
    def get_balance(self):
        return self.__balance
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f'Deposited: {amount}., Now your current balance is {self.__balance}')
        else:
            print('Deposit amount must be positive.')
            
# create object 

account = BankAccount(1000)
account.deposit(500)  # Deposit 500
print('Current balance:', account.get_balance())  # Access balance using public method.
# account.__balance = 2000  # This will raise an AttributeError
# account.__balance  # This will raise an AttributeError