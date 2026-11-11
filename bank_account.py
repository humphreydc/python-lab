class BankAccount:
    def __init__(self, holder, balance=0.0):
        self.holder = holder
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, amount):
        if amount >= 0:
            self._balance = amount
        else:
            print("Error: Balance cannot be set to a negative value.")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount:.2f}. New balance: ${self.balance:.2f}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}")
        else:
            print("Insufficient funds or invalid amount.")

    def __add__(self, other):
        if isinstance(other, BankAccount):
            return self.balance + other.balance
        raise TypeError("Can only add two BankAccount objects.")

    def __str__(self):
        return f"Account Holder: {self.holder} - Balance: ${self.balance:.2f}"


louise = BankAccount("Louise", 100)
delcastillo = BankAccount("Delcastillo", 200)

print(louise)
print(delcastillo)

print("\nAttempting to set balance to -50:")
louise.balance = -50

print("\nPerforming transactions:")
louise.deposit(50)
delcastillo.withdraw(25)

total = louise + delcastillo
print(f"\nTotal funds in both accounts: ${total:.2f}")

print("\nBible verse:")
print("\"Ngunit sinabi niya sa akin, Ang aking biyaya ay sapat para sa iyo, sapagkat ang aking kapangyarihan ay ginagawang perpekto sa kahinaan.” – 2 Corinthians 12:9")
