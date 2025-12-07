class BankAc:
    def __init__(self, owner):
        self.owner = owner
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        print("Баланс збільшено на", amount, '\n ваш баланс', self.balance)

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print("Успішно знято", amount, '\n ваш баланс', self.balance)
        else:
            print("Не вистачає коштів", '\n ваш баланс', self.balance)

    def show_balance(self):

        print("Власник рахунку", self.owner, "поточний баланс", self.balance)


b1 = BankAc("Іван Петрович")
b1.deposit(1000)
b1.withdraw(1500)
b1.show_balance()
print()

b2 = BankAc("Степан Іванович")
b2.deposit(1000)
b2.deposit(1500)
b2.withdraw(2000)