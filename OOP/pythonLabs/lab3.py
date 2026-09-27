from abc import ABC, abstractmethod


#########OPTION A - BANK ACCOUNT ##################




class Account(ABC):
    def __init__(self, balance, account_number):
        self._balance=balance
        self._account_number = account_number

    @property
    def balance(self):
        return self._balance
    @property
    def account_number(self):
        return self._account_number

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")

        self._balance += amount
    def withdraw(self, amount):
        if amount <=0:
            raise ValueError("Amount must be positive")
        if self._balance < amount:
            raise ValueError("Cant withdraw more than in balance")
        self._balance -= amount

    @abstractmethod
    def account_type(self):
        pass

class SavingsAccount(Account):
    def account_type(self):
        return "This is SavingsAccount"

    def add_interest(self, rate ):
        self._balance +=self._balance * rate

class CheckingAccount(Account):
    def __init__(self, balance, account_number, overdraft_limit):
        super().__init__(balance, account_number)
        self.overdraft_limit= overdraft_limit

    def account_type(self):
        return "This is CheckingAccount"

    def withdraw(self, amount):
        if(amount <= 0):
            raise ValueError("Amount must be positive")

        if(self._balance - amount < -self.overdraft_limit):
            raise ValueError("Overdraft limit exceeded")

        self._balance -= amount

def show_account_type(account):
    print(account.account_type())





savings = SavingsAccount(1000, "S001")
checking = CheckingAccount(500, "C001", 100)
print("savings")
print(savings.balance)
savings.deposit(200)
print(savings.balance)

savings.add_interest(0.05)
print(savings.balance)

print("checking")
checking.withdraw(5500)
print(checking.balance)

show_account_type(savings)
show_account_type(checking)

# OUTPUTS
# savings
# 1000
# 1200
# 1260.0
# checking
# -50
# This is SavingsAccount
# This is CheckingAccount