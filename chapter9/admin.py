class User:
    """En class for users der har informationer, og de kan blive called."""

    def __init__(self, first_name, last_name, username, email, password,):
        self.username = username
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.logins_attempted = 0

    def describe_user(self):
        print(f"{self.username}'s real name is {self.first_name.capitalize()} {self.last_name.capitalize()}.")
        print(f"Their email and password is the following: {self.email}, {self.password}")
    
    def greet_user(self):
        print(f"\nSup' {self.username}")

#Ny login_attempt method
    def increment_logins_attempted(self):
        self.logins_attempted += 1
        if self.logins_attempted == 1:
            print(f'There has been {self.logins_attempted} attempt to login to your account')
        else:
            print(f'There has been {self.logins_attempted} attempts to login on your account')

#set login_attempts
    def set_login(self, set_logins):
        self.logins_attempted = set_logins

#reset logins_attempted
    def reset_logins_attempted(self):
        self.logins_attempted = 0
        print(f'You resetted your account login attempt history')


class Admin(User):
    def __init__(self, first_name, last_name, username, email, password, priviliges=None):
        super().__init__(first_name, last_name, username, email, password)
        self.priviliges = priviliges
        if self.priviliges == None:
            self.priviliges = []
            

    def show_priviliges(self):
        print(f'The {self.username} has following priviliges: ')
        for privligie in self.priviliges:
            print(f'- {privligie}')