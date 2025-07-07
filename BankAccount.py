# The final class should implement __str__() to override the to string of python so that if I type print(thePerson) it should print it out nicely
# Put this class inside a seperate .py file, then in a new py file call the class file and import the class. Then instantiate an object of the
# class and show examples of the value being changed and the social security changing. As well as a final call that shows the implementation of __str__

from PersonInfo import Info
from AccountInfo import Account


# Prompts the user to give their information
def getInfo():
    information = Info(
        firstName=input("What is your First Name? : "),
        lastName=input("What is your Last Name? : "),
        address=input("What is your Address? (Street, city, state): "),
        dateOfBirth=input("What is your Date of Birth? (mm/dd/year): "),
        socialSecurity=input("What is your SSN? : "),
    )
    return information


def getCard():
    card = Account(type=str(""), cash=float("0"), value=float("0"))
    return card


def createNewAccount():
    affirm = input("Would you like to create a new bank account? (y/n) :")
    if affirm.lower()[0] == ("y"):
        information = getInfo()
    else:
        return
    # Conforming if the information is correct
    print(information)
    affirm = input("is your information correct?")
    while affirm.lower()[0] == ("n"):
        information = getInfo()
        print(information)
        affirm = input("is your information correct?")
    # Choosing card type
    card = getCard()
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


createNewAccount()
