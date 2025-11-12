class bank:
    #constractor for the bank class
    def __init__(self, withdraw, deposit):
        #this is a private variable, it can only be accessed in this class
        self.withdraw=withdraw
        self.deposit=deposit
        # This asks the user how much money they have and prints it

    def money(self):
        money=int(input("how much money do you have in your account"))
        print(f"you have {self.money} in your account ")
# This method asks the user how much money they have

account=bank(20, 100)
#Created a bank account with withdraw = 20 and deposit = 100
print(account.withdraw)
print(account.deposit)
#Printed the withdraw and deposit values
def __str__(self):
    return f"{self.name} has balance {self.balence}"
