class Account():
    
    def __init__ (self, owner, balance):
        self.owner=owner
        self.balance=balance
        print("Owner is {self.owner} and balance is {self.balance}")

    def deposit(self):
        add=int(input("how much money u wanna add: "))
        print(f'{add} tenge were added to {self.owner}\'s balance')
        self.balance+=add
        print(f'your balance is {self.balance}')

    def withdraw(self):
        take=int(input("how much money you wanna withdraw: "))

        if take<=self.balance:
            self.balance-=take
            print(f"Your balance is {self.balance} tenge")

        else:
            print("you dont have enough money")
owner=input("Tvoe imya: ")
balance=int(input("balance: "))
cash=Account(owner, balance)

while True:
    action=input("deposit or withdraw")
    if action=='deposit':
        cash.deposit()
    if action=="withdraw":
        cash.withdraw()