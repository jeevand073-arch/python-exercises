class Bankaccount():
    def __init__(self,name,balance):
        self.name = name
        self.__balance = balance
    def details(self):
        print(f"name of account holder{self.name}")  
        print(f"balance amount of account holder{self.__balance}")
    def deposit(self,amount):
        self.__balance += amount
        print(f"amount deposited{amount}")
    def withdraw(self,amount):
        if amount > 0 :
            if amount < self.__balance :
                self.__balance -= amount
                print(f"amount withdraw {amount}")
            else:
                print("insufficent balance:")
        else:
            print("invalid amount:")
    def balance_amount(self):
        print(f"balnce amount{self.__balance}")

name = input("enter your name:")
amount = int(input("enter your amount:"))

acc = Bankaccount(name,amount)
acc.deposit(2000)
acc.withdraw(1000)
acc.balance_amount()
        
