# The final class should implement __str__() to override the to string of python so that if I type print(thePerson) it should print it out nicely
# Put this class inside a seperate .py file, then in a new py file call the class file and import the class. Then instantiate an object of the
# class and show examples of the value being changed and the social security changing. As well as a final call that shows the implementation of __str__


# Class that manages account money and type
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
            f"C:/Users/majohnson/Desktop/more stuff/OOP-PTHON-PRACTICE/Accounts/{self.type}_Card.txt",
            "w",
        ) as file:
            file.write(f"{self.type} balance: {self.value}")


# Class that manages account info
class Info:
    def __init__(self, firstName, lastName, address, dateOfBirth, socialSecurity):
        self.firstName = firstName
        self.lastName = lastName
        self.address = address
        self.dateOfBirth = dateOfBirth
        self.socialSecurity = socialSecurity

    def __str__(self):
        return f"Your name is '{self.firstName} {self.lastName}' \nyour address is '{self.address}' \nyour date of birth is '{self.dateOfBirth}' \nyour SSN is '{self.socialSecurity}"

    # creates a file with all the user info
    def createAccount(self):
        with open(
            f"C:/Users/majohnson/Desktop/more stuff/OOP-PTHON-PRACTICE/Accounts/{self.firstName}_{self.lastName}_User_Info.txt",
            "w",
        ) as file:
            file.write(
                f"{self.firstName}\n{self.lastName}\n{self.address}\n{self.dateOfBirth}\n{self.socialSecurity}"
            )


# Prompts the user to give their information
class BankInfo(Info, Account):

    def __init__(self):
        firstName = input("What is your First Name? : ")
        lastName = input("What is your Last Name? : ")
        address = input("What is your Address? (Street, city, state): ")
        dateOfBirth = input("What is your Date of Birth? (mm/dd/year): ")
        socialSecurity = input("What is your SSN? : ")
        super().__init__(firstName, lastName, address, dateOfBirth, socialSecurity)

    # def updateInfo(self):
    #     return {
    #         "firstName": input("What is your First Name? : "),
    #         "lastName": input("What is your Last Name? : "),
    #         "address": input("What is your Address? (Street, city, state): "),
    #         "dateOfBirth": input("What is your Date of Birth? (mm/dd/year): "),
    #         "socialSecurity": input("What is your SSN? : "),
    #     }

    def getCard(self):
        card = Account(type=str(""), cash=float("0"), value=float("0"))
        return card

    def createNewAccount(self):
        affirm = input("Would you like to create a new bank account? (y/n) : ")
        if affirm.lower()[0] == ("y"):
            information = self.getInfo()
        else:
            return
        # Conforming if the information is correct
        print(information)
        affirm = input("is your information correct?")
        while affirm.lower()[0] == ("n"):
            information = self.getInfo()
            print(information)
            affirm = input("is your information correct?")
        # Choosing card type
        card = self.getCard()
        card.chooseType()
        # Putting Money in the card
        card.cash = float(input("How much cash will you put in your card? : $"))
        correct = False
        while correct == False:
            if card.type == "debit":
                if card.value + card.cash > 0:
                    card.value += card.cash
                else:
                    print("Error: Not enough Balance")
            else:
                card.value += card.cash
            print(card)
            yes = input("Would you like to add more? (y/n) : ")
            if yes.lower()[0] == "n":
                correct = True
            else:
                card.cash = float(input("How much cash will you put in your card? : $"))
        print(card)

        # Creates a file for account information
        card.createAccount()
        information.createAccount()
        print("Thank you for your Time! :)")
