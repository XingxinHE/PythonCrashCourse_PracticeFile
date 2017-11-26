class User():
    """This is a class for user."""
    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0
    
    def describe_user(self):
        print("\nThe follow is the information of this user: ")
        print("First Name: "+self.first_name)
        print("Last Name: "+self.last_name)
    
    def greet_user(self):
        print("Hello! "+self.first_name+" "+self.last_name+".")
    
    def increment_login_attempts(self):
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        self.login_attempts = 0