
from abc import ABC,abstractmethod

class BankAccount(ABC):
    def __init__(self,name,balance):
        self.name = name
        self.__balance = balance

    def diplay_balance(self):
        print(f"name of the account holder is:{self.name}")
        print(f"your balnce is: {self.__balance}")

    def get_balance(self):
        return self.__balance
    def set_balance(self,amount):
        self.__balance= amount

    @abstractmethod
    def deposit(self):
        pass
    @abstractmethod
    def withdraw(self):
        pass
class SavingAcccount(BankAccount):
    def deposit(self,amount):
        balance_after_deposit = self.get_balance()+amount
        self.set_balance(balance_after_deposit)
        print(f"deposited amount:{amount}")
        print(f"total deposited amount:{self.get_balance()}")
    def withdraw(self,amount):
        if amount > 0 :
            if amount <= self.get_balance():
                balance_after_wihdrowal= self.get_balance()-amount
                self.set_balance(balance_after_wihdrowal)
                print(f"withdrow amount:{amount}")
                print(f"reaming  total amount :{self.get_balance()}")
            else:
                print("insuficent balance")
        else:
            print("enter vaild amount")

name = input("enter your name:")
amount = int(input("enter your amount:"))

account = SavingAcccount(name,amount)

while True:
    print("\n1.deposit")
    print("2.withdrow")
    print("3.balance")
    print('4.Exit')

    choice = int(input("enter your choice:"))
    if choice == 1:
        amount = int(input("enter your deposit amount:"))
        account.deposit(amount)
    elif choice == 2 :
        amount = int(input("enter the amount you want withdraw:"))
        account.withdraw(amount)
    elif choice == 3 :
        account.diplay_balance()
    elif choice == 4:
        print("thank you for visting bank")
        break
    else:
        print("your have enter the invaild number:")






        
    

    