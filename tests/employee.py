class Employee:
    """Class of an employee"""
    def __init__(self, first_name, last_name, salary, salaryraise=5000):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = int(salary)
        self.salaryraise = int(salaryraise)
    
    def give_raise(self):
        self.salary = int(self.salary) + int(self.salaryraise)
        print(f"There has been given a raise of ${self.salaryraise}")
    
    def describe_salary(self):
        print(f"The salary for {self.first_name.title()} {self.last_name.title()} is {self.salary}")
