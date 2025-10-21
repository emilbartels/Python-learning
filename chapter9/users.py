


class User:
    """En class for users der har informationer, og de kan blive called."""

    def __init__(self, first_name, last_name, username, email, password):
        self.username = username
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        print(f"{self.username}'s real name is {self.first_name.capitalize()} {self.last_name.capitalize()}.")
        print(f"Their email and password is the following: {self.email}, {self.password}")
    
    def greet_user(self):
        print(f"\nSup' {self.username}")
