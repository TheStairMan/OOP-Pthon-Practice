# Account should have account info, Account type, account value as variables
# There should be functions that are able to be overriden in the child class, called debit and credit that change the amount in the account
class Account:
    def __init__(self, type, value, cash):
        self.type = type
        self.value = value
        self.cash = cash

    def __str__(self):
        return f"{self.type} balance: {self.value}"

    def chooseType(self):
        self.type = input("What type of card would you like? (debit/credit) : ")
        if self.type.lower()[0] == "d":
            self.type = "debit"
        else:
            self.type = "credit"
        correct = False
        while correct == False:
            print(f"{self.type}")
            yes = input("Is this the correct type? (y/n) : ")
            if yes.lower()[0] == "y":
                correct = True
            else:
                pass

    def createAccount(self):
        with open(
            f"C:/Users/majohnson/Desktop/more stuff/oopPractice/Accounts/{self.type}_Card.txt",
            "w",
        ) as file:
            file.write(f"{self.type} balance: {self.value}")
