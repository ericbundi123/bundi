class BankAccount:
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance
    def deposit(self,amount):
        self.balance += amount

def withdraw(self,amount):
             if self.balance >= amount:
              self.balance -= amount
              else:
      print("Insufficient balance")

  def get_balance(self):
        return self.balance
 #object
 account=BankAccount("eric",85)
account.deposit(100)
account.withdraw(50)
print("balance" , account.balance())

