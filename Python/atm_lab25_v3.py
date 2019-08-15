class Atm:
    def __init__(self, balance = 0, transactions = []):
        self.balance = balance
        self.transactions = transactions

    def check_balance(self):
        return (f'Current balance is ${self.balance}')
        
    def deposit(self, amount):
        self.balance += float(amount)
        self.transactions.append(f'User deposited ${amount}.')
        print(f'User deposited ${amount}')

    def check_withdrawal(self, amount):
        result = self.balance - float(amount)
        if result >= 0:
            return True
        return False

    def withdraw(self, amount):
        if self.check_withdrawal(True):
            self.balance -= float(amount)
            self.transactions.append(f'User withdrew ${amount}.')
            print(f'User withdrew ${amount}')
        else:
            print(f'Sorry!  You don\'t have enough to cover that withdrawal.')

    def print_transactions(self):
        result = self.transactions
        print(result)


print(f'######## WELCOME TO YOUR ACCOUNT ON THE ATM ########\n')
print('Actions: ')
print(f'Check Balance')
print(f'Deposit')
print(f'Withdraw')
print(f'History')
print(f'Exit')

atm = Atm()
while True:
    choice = input(f'\nWhat would you like to do? ').lower()

    # atm = Atm()
    if choice == 'exit':
        print('Thanks for using the ATM!')
        break
    elif choice == 'check balance':
        print(atm.check_balance())
    elif choice == 'deposit':
        amount = float(input('How much would you like to deposit? '))
        atm.deposit(amount)   
    elif choice == 'withdraw':
        amount = float(input('How much would you like to withdraw?'))
        print(atm.withdraw(amount))
    elif choice == 'history':
        atm.print_transactions()

