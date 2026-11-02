class UserProfile: # class define

    platfrom_name = "CodeConnect" # class attribute

    def __init__(self, username, email, password): #Constructor & Instance Attributes
        self.username = username
        self.email = email
        self.__password = password # Private Attribute

    def update_password(self, new_password):
        self.__password = new_password
        print(f"{self.username}'s Password has been updated securely password is :{self.__password} ")
        
    @staticmethod
    def privacy_policy():
        print("Your private data is never shared with third parties.")

UP1=UserProfile("ABC", "ABC@gmail.com", "zxcvbnm")

# print(UP1.username)
print(UserProfile.platfrom_name)
UP1.privacy_policy()
UP1.update_password("qwerty")