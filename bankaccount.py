class bank:
    def __init__(self, withdraw, deposit):
        self.withdraw=withdraw
        self.deposit=deposit

    def money(self):
        money=int(input("how much money do you have in your account"))
        print(f"you have {self.money} in your account ")

account=bank(20, 100)
print(account.withdraw)
print(account.deposit)

