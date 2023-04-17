## Mini Bank application

class Customer:
    '''This class developed by Durga and describes bank operations'''
    Bank_name = "DURGABANK" #static variables
    def __init__(self,name,balance=0.0):   # balance = 0.0 is a default arguments #constructor
        self.name = name
        self.balance = balance
    
    def deposit(self,amount):
        self.balance = self.balance + amount
        print("After deposit, balance:",self.balance)
    
    def withdraw(self,amount):
        if amount > self.balance:
            print("Insufficient funds........ Cant perform this operation.")
        else:
            self.balance = self.balance - amount
            print("After withdraw, balance:",self.balance)

print("Welcome to:",Customer.Bank_name)
name = input("Enter your name:")
C = Customer(name)
while True:
    print('d - Deposit /n w - Withdrawal /n e - Exit')
    option = input("Choose your option: ")
    if option.lower() == 'd':
        amount = float(input("Enter amount to depoist: "))
        C.deposit(amount)
    elif option.lower() == 'w':
        amount = float(input("Enter amount to depoist: "))
        C.withdraw(amount)
    elif option.lower() == 'e':
        print("Thanks for Banking")
        break
    else:
        print('your option is invalid.... Please choose valid option!')