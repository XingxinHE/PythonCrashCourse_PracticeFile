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

class Admin(User):
    
    def __init__(self,first_name,last_name):
        super().__init__(first_name,last_name)
        
        self.privileges = Privileges()
    
            
class Privileges():
    
    def __init__(self):
        self.privileges = ['can add post','can delete post','can ban user']
    
    def show_privileges(self):
        for privilege in self.privileges:
            print("This account "+privilege+".")

newAdmin = Admin('Xingxin','HE')
newAdmin.privileges.show_privileges()
