# The parent person should have first name last name, address, DOB, social security,
# with functions to change any of these values,
# This should be done with 1 primary function that gets called seperatly for each value,
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
            f"C:/Users/majohnson/Desktop/more stuff/oopPractice/Accounts/{self.firstName}_{self.lastName}_User_Info.txt",
            "w",
        ) as file:
            file.write(
                f"{self.firstName}\n{self.lastName}\n{self.address}\n{self.dateOfBirth}\n{self.socialSecurity}"
            )
